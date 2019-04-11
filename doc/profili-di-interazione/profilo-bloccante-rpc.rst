Profilo bloccante RPC
=====================

Scenario
--------

Lo sviluppo di una interfaccia bloccante di tipo RPC si richiede nei
casi in cui:

-  L’esecuzione del metodo ``M`` è poco onerosa computazionalmente e può
   essere portata immediatamente a termine dall’erogatore.

-  Il contesto rende complessa l’implementazione delle modalità non
   bloccanti. Ad esempio, non è possibile
   per il fruitore esporre una propria interfaccia di servizio ed il fruitore non può farsi carico di mantenere il
   contesto necessario ad effettuare attesa attiva.

Descrizione
-----------

.. mermaid::
   :caption: Interazione bloccante RPC
   :alt: interazione bloccante RPC

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F


In questo profilo si ha una risposta da parte dell’erogatore contestuale
alla richiesta del fruitore. La figura mostra lo schema di questa
interazione.

Interfaccia REST
----------------

Nel caso di implementazione tramite tecnologia REST, DEVONO essere
seguite almeno le seguenti indicazioni:

-  La specifica dell’interfaccia DEVE dichiarare tutti i codici di stato
   HTTP restituiti con relativo schema della risposta, oltre che ad
   eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare lo schema della
   richiesta insieme ad eventuali header HTTP richiesti;

-  Al passo (1) il fruitore DEVE utilizzare come verbo HTTP per
   l’esecuzione della chiamata a procedura il verbo HTTP POST su un URL
   contenente gli ID interessati ed il nome del metodo;

-  Al passo (2) il fruitore DEVE utilizzare :httpstatus:`200` a meno che
   non si verifichino errori.

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Al termine del processamento della richiesta, l’erogatore DEVE fare uso
dei codici di stato HTTP rispettandone la semantica [1]_. In
particolare, al ricevimento della richiesta da parte del fruitore,
l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso di
   dati errati DEVE restituire :httpstatus:`400` Bad Request fornendo
   nel body di risposta dettagli circa l’errore;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVE restituire :httpstatus:`404` Not Found, indicando nel body di
   risposta quale degli ID è mancante;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi ed indicando
   nel body di risposta il motivo dell’errore;

-  In caso di successo DEVE restituire :httpstatus:`200` OK, riempiendo il
   body di risposta con il risultato dell’operazione.

Esempio
~~~~~~~
**Specifica Servizio**
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/RESTblocking.yaml

.. literalinclude:: ../media/rest-blocking.yaml
    :language: yaml

Di seguito un esempio di chiamata al metodo ``M``.


**Http Operation**
POST

**Endpoint**
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M

(1) Request Body

.. code-block:: JSON

    {
     "a": {
       "a1s": [1,2],
       "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
       },
       "b": "Stringa di esempio"
    }


(2) Response Body (HTTP Status Code 200 OK)

.. code-block:: JSON

    {
      "c" : "risultato"
    }

(2) Response Body (HTTP Status Code 500 Internal Server Error)

.. code-block:: JSON

    {
        "type": "https://apidoc.example.com/probs/operation-too-long",
        "status": 500,
        "title": "L'operazione dura troppo.",
        "detail": "Il sistema non e' riuscito a completare in tempo l'operazione prevista.",
    }


(2) Response Body (HTTP Status Code 400 Bad Request)

.. code-block:: JSON

    {
        "type": "https://apidoc.example.com/probs/invalid-a",
        "status": 400,
        "title": "L'attributo `b` ha un valore non valido.",
        "detail": "L'attributo `b` dev'essere una stringa di lunghezza inferiore a 32 caratteri.",
    }

(2) Response Body (HTTP Status Code 404 Not Found)

.. code-block:: JSON

    {
        "status": 404,
        "title": "Risorsa non trovata.",
    }

Interfaccia SOAP
-----------------

Se il profilo viene implementato con tecnologia SOAP, a differenza del
caso REST, il metodo invocato non è specificato nell’endpoint chiamato,
poichè viene identificato all’interno del body. Inoltre tutti gli ID
coinvolti DEVONO essere riportati all’interno del body. DEVE essere rispettata le seguente regola:

-  La specifica dell'interfacciad ell’erogatore DEVE
   dichiarare tutti i metodi esposti con relativi schemi dei messaggi di
   richiesta e di ritorno. Inoltre le interfacce devono specificare
   eventuali header SOAP richiesti;

.. _regole-di-processamento-rpc-soap-1:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire :httpstatus:`500` fornendo dettagli
   circa l’errore utilizzando il meccanismo della SOAP fault;

-  Nel caso in cui qualcuno degli ID nel body non esista,
   DEVE restituire :httpstatus:`500` indicando tramite la SOAP fault
   quale degli ID è mancante;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire il
   codice HTTP 500, indicando il motivo dell’errore nella SOAP fault;

-  In caso di successo restituire :httpstatus:`200`, riempiendo il
   body di risposta con il risultato dell’operazione.

.. _esempio-rpc-soap-1:

Esempio
~~~~~~~

**Specifica Servizio**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1?wsdl

.. literalinclude:: ../media/soap-blocking.wsdl
   :language: xml

A seguire un esempio di chiamata al metodo ``M``.


**Endpoint**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1

**Method**
M

1. Request Body

.. code-block:: XML

    
    <soap:Envelope 
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio" >
        <soap:Header>
            <!--Autenticazione-->
        </soap:Header>
        <soap:Body>
        <m:MRequest>
            <M>
                <oId>1234</oId>
                <a>
                    <a1s><a1>1</a1>...<a1>2</a1></a1s>
                    <a2>RGFuJ3MgVG9vbHMgYXJlIGNvb2wh</a2>
                </a>
                <b>Stringa di esempio</b>
            </M>
        </m:MRequest> 
        </soap:Body>
    </soap:Envelope>

2. Response Body (HTTP status code 200 OK)

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio" >

        <soap:Body>
        <m:MRequestResponse>
          <return>
            <m:c>OK</m:c>
          </return>
        </m:MRequestResponse>
    </soap:Body>

    </soap:Envelope>

2. Response Body (HTTP status code 500 Internal Server Error)

.. code-block:: XML

    <soap:Envelope 
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio" >
        <soap:Body>
          <soap:Fault>
             <soap:Code>
                <soap:Value>soap:Receiver</soap:Value>
             </soap:Code>
             <soap:Reason>
                <soap:Text xml:lang="en">Error</soap:Text>
             </soap:Reason>
             <soap:Detail>
                <m:ErrorMessageFault>
                   <customFaultCode>1234</customFaultCode>
                </m:ErrorMessageFault>
             </soap:Detail>
          </soap:Fault>
        </soap:Body>
    </soap:Envelope>

.. [1]
   http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
