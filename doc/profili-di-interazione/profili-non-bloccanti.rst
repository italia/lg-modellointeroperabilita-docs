Profili non bloccanti
=====================

Nel seguito del capitolo verranno mostrati i profili di interazione
non bloccante, in cui un fruitore sottomette una richiesta e questa
viene solo presa in carico immediatamente, mentre il suo soddisfacimento
può avvenire in maniera differita.

Gli approcci non bloccanti vengono utilizzati nei casi in cui i tempi
per l’erogazione di una risposta da parte del fruitore sono lunghi
perché

- la richiesta è onerosa in termini temporali;

- il fruitore non può farsi immediatamente carico dell’erogazione del servizio.

Al fine di collegare le richieste con le risposte si farà uso, sia nelle
implementazioni SOAP che in quelle REST, di meta-informazioni specifiche
(quali il correlation ID ed l’endpoint per le callback). Queste sono
estranee solitamente alla business logic del servizio, ma è necessario
definirle a livello di interfaccia di servizio ai fini
dell’interoperabilità. A tal fine verranno definiti header(HTTP nel
caso REST ed envelope nel caso SOAP) utili a contenere queste
informazioni.

In alcuni casi, una interfaccia di servizio viene creata al fine di
automatizzare o semplificare un servizio già offerto dalla pubblica
amministrazione. In una moltitudine di casi questi servizi sono
asincroni (non bloccanti) per natura, e consistono di richieste a cui
vengono allegati degli identificativi (es. numeri di protocollo) che
accompagnano la richiesta.
In questi casi, il correlation ID può essere sostituito da questi
identificativi già previsti dal servizio.

.. _paragrafo-nonbloccante-1:

Profili non bloccante RPC PUSH (basato su callback)
---------------------------------------------------

.. _scenario-nonbloccante-1:

Scenario
~~~~~~~~

Questo caso particolare, denominato RPC PUSH, è utilizzabile nel caso in
cui il fruitore abbia a sua volta la possibilità di esporre una interfaccia
di servizio per la ricezione delle risposte.

.. _descrizione-nonbloccante-1:

Descrizione
~~~~~~~~~~~

.. mermaid::
   :caption: Interazione non bloccante tramite callback
   :alt: interazione non bloccante tramite callback

    sequenceDiagram
        participant F as Fruitore
        participant E as Erogatore
        activate F
        F ->> E: 1. Request(Callback EndPoint)
        activate E
        E -->> F: 2. CorrelationID
        deactivate F
        deactivate E
        activate F
        E ->> F: 3. Replay(CorrelationID)
        activate E
        F -->> E: 4. Ack
        deactivate F
        deactivate E


In questo scenario (vedi figura), la richiesta del fruitore contiene
un riferimento al servizio da chiamare al momento della risposta. Si
suppone infatti che i fruitori espongano a loro volta delle interfacce
con segnatura standard. Al momento del ricevimento della richiesta
(passo (1)), l’erogatore risponde (passo (2)) riconoscendo l’avvenuta
ricezione (acknowledgement o in breve ack) ed indica un correlation ID
(ID di correlazione), generato lato erogatore, che permetta al fruitore,
una volta ricevuta la risposta, di accoppiarla alla richiesta originale.
Quando il processamento è terminato infatti, l’erogatore (passo (3))
chiama il fruitore (invertendo quindi i ruoli chiamato/chiamante)
riportando l’esito ed indicando il correlation ID. Il fruitore riconosce
(sempre mediante un messaggio di ack) la ricezione della risposta (passo
(4)).

.. _interfaccia-rest-nonbloccante-1:

Interfaccia REST
~~~~~~~~~~~~~~~~

Nel caso in cui il profilo venga implementato con tecnologia REST,
DEVONO essere rispettate le seguenti indicazioni:

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare tutti i codici di stato HTTP restituiti con relativo
   schema della risposta, oltre che ad eventuali header HTTP restituiti;

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare gli schemi delle richieste insieme ad eventuali header
   HTTP richiesti;

-  La specifica dell’interfaccia dell’erogatore deve dichiarare tramite
   il formalismo specifico [1]_ il formato delle callback; questa
   specifica deve essere rispettata dall’interfaccia esposta dal
   fruitore, e quindi nella rispettiva specifica;

-  Al passo (1), il fruitore DEVE indicare l’endpoint della callback
   utilizzando l’header HTTP custom X-ReplyTo; Il verbo HTTP utilizzato
   deve essere POST;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, il correlation ID utilizzando l’header HTTP
   custom X-Correlation-ID; Il codice HTTP di stato DEVE essere :httpstatus:`202`
   a meno che non si verifichino errori;

-  Al passo (3), l’erogatore DEVE riutilizzare lo stesso correlation ID
   fornito al passo (2) sempre utilizzando l’header HTTP custom
   X-Correlation-ID; Il verbo HTTP utilizzato deve essere POST;

-  Al passo (4), il fruitore DEVE riconoscere tramite un messaggio di
   acknowledgement il ricevimento della risposta; Il codice HTTP di
   stato DEVE essere :httpstatus:`200` a meno che non si verifichino errori.

.. _regole-di-processamento-nonbloccante-2:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Al termine del processamento delle richieste, l’erogatore ed il fruitore
DEVONO fare uso dei codici di stato HTTP rispettandone la
semantica [2]_.
Friutore ed erogatore:

-  DEVONO verificare la validità sintattica dei dati in ingresso. In caso di
   dati errati DEVONO restituire :httpstatus:`400` fornendo
   nel body di risposta dettagli circa l’errore;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVONO restituire :httpstatus:`404`, indicando nel body di
   risposta quale degli ID è mancante;

-  In caso di errori non dipendenti dalla richiesta, DEVONO restituire
   HTTP status 5XX rispettando la semantica degli stessi ed indicando
   nel body di risposta il motivo dell’errore;

-  Al momento della ricezione della richiesta, l’erogatore DEVE restituire
   :httpstatus:`202`. In caso di ricezione corretta della risposta,
   il fruitore DEVE restituire :httpstatus:`200`, riempiendo il body di
   risposta con un acknowledgement dell’avvenuta ricezione. Nel caso di
   errore al momento di ricezione della risposta da parte del fruitore,
   è possibile utilizzare meccanismi specifici per la ritrasmissione della
   risposta o della richiesta.

.. _esempio-nonbloccante-2:

Esempio
^^^^^^^

 **Specifica Servizio Server**
 https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/RESTCallbackServer.yaml

 .. literalinclude:: ../media/rest-callback-server.yaml
    :language: yaml

----

 **Specifica Servizio Client**
 https://api.indirizzoclient.it/rest/v1/nomeinterfacciaservizio/RESTCallbackClient.yaml

 .. literalinclude:: ../media/rest-callback-client.yaml
    :language: yaml

Di seguito un esempio di chiamata al metodo M con la presa in carico da
parte dell’erogatore.


**HTTP Operation**
POST


**Endpoint**
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M

1\) Request Header & Body

.. code-block:: http

        POST /rest/v1/nomeinterfacciaservizio/resources/1234/M HTTP/1.1
        Content-Type: application/json
        X-ReplyTo: https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

        {
          "a": {
            "a1": [1,...,2],
            "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
          },
          "b": "Stringa di esempio"
        }


2\) Response Header & Body (:httpstatus:`202`)

.. code-block:: http

        HTTP/1.1 202 Accepted
        Content-Type: application/json
        X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d

        {
          "result" : "ACK"
        }


Di seguito un esempio di risposta da parte dell’erogatore verso il fruitore.

**HTTP Operation**
POST

**Endpoint**
https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

3\) Request Header & Body

.. code-block:: http

        POST /rest/v1/nomeinterfacciaclient/Mresponse HTTP/1.1
        X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d

        {
           "c": "OK"
        }

4\) Response Header & Body (:httpstatus:`200`)

.. code-block:: http

        HTTP/1.1 200 Success
        Content-Type: application/json

        {
          "result" : "ACK"
        }

.. _interfaccia-soap-nonbloccante-1:

Interfaccia SOAP
~~~~~~~~~~~~~~~~

Nel caso di implementazione mediante tecnologia SOAP, l’endpoint di
callback ed il correlation ID, vengono inseriti all’interno dell’header
SOAP come campi custom. Erogatore e fruitore DEVONO inoltre seguire le
seguenti regole:

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare tutti i metodi esposti con relativi schemi dei messaggi di
   richiesta e di ritorno. Inoltre le interfacce devono specificare
   eventuali header SOAP richiesti;

-  La specifica dell’interfaccia del fruitore DEVE rispettare quanto
   richiesto dall’erogatore; in particolare si richiede che
   l’erogatore fornisca un WSDL descrittivo del servizio di callback
   che il fruitore è tenuto ad implementare;

-  Al passo (1), il fruitore DEVE indicare l’endpoint della callback
   utilizzando l’header SOAP custom X-ReplyTo;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, il correlation ID utilizzando l’header SOAP
   custom X-Correlation-ID;

-  Al passo (3), l’erogatore DEVE riutilizzare lo stesso correlation ID
   fornito al passo (2) sempre utilizzando l’header SOAP custom
   X-Correlation-ID;

-  Al passo (4), il fruitore DEVE riconoscere tramite un messaggio di
   acknowledgement il ricevimento della risposta.

.. _regole-di-processamento-nonbloccante-3:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
In particolare, al ricevimento della richiesta, fruitore ed erogatore:

-  DEVONO verificare la validità sintattica dei dati in ingresso. In caso di
   dati errati DEVONO restituire  :httpstatus:`400`   fornendo
   nel body di risposta dettagli circa l’errore;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVONO restituire  :httpstatus:`404`  , indicando nel body di
   risposta quale degli ID è mancante;

-  In caso di errori non dipendenti dal richiedente (fruitore o erogatore), DEVONO restituire i
   codici HTTP 5XX rispettando la semantica degli stessi ed indicando
   nel body di risposta il motivo dell’errore;

-  Al momento della ricezione della richiesta, DEVONO restituire un codice 2XX, nel dettaglio:

    * :httpstatus:`200` in caso di presenza della payload SOAP, riempiendo il body di risposta
      con il risultato relativo alla richiesta.
    * :httpstatus:`200` o :httpstatus:`202` in caso di assenza della payload SOAP

-  Nel caso di errore al momento di ricezione della risposta da parte del richiedente (fruitore o erogatore), è
   possibile definire meccanismi specifici per la ritrasmissione delle richieste.


.. _esempio-nonbloccante-3:

Esempio
^^^^^^^

 **Specifica Servizio Server**
 https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1?wsdl

 .. literalinclude:: ../media/soap-callback-server.wsdl
    :language: xml


----

 **Specifica Servizio Callback**
 https://api.indirizzoclient.it/soap/nomeinterfacciaservizio/v1?wsdl

 .. literalinclude:: ../media/soap-callback-client.wsdl
    :language: xml


Segue un esempio di chiamata al metodo M in cui l’erogatore conferma di
essersi preso carico della richiesta.

**Endpoint**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1

**Method**
MRequest

1\) Request Body

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Header>
            <m:X-ReplyTo>https://api.indirizzoclient.it/soap/nomeinterfacciaservizio/v1</m:X-ReplyTo>
        </soap:Header>
        <soap:Body>
            <m:MRequest>
                <M>
                    <o_id>1234</o_id>
                    <a>
                        <a1s>1</a1s>
                        <a2>prova</a2>
                    </a>
                    <b>prova</b>
                </M>
            </m:MRequest>
        </soap:Body>
    </soap:Envelope>

2\) Response Body

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">>
        <soap:Header>
            <m:X-Correlation-ID>b8268033-de67-4fa0-bf06-caebbfa5117a</m:X-Correlation-ID>
        </soap:Header>
        <soap:Body>
            <m:MRequestResponse>
                <return>
                    <outcome>ACCEPTED</outcome>
                </return>
            </m:MRequestResponse>
        </soap:Body>
    </soap:Envelope>


**Endpoint**
https://api.indirizzoclient.it/soap/nomeinterfacciaclient/v1

**Method**
MRequestResponse


(3) Request Body

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Header>
            <m:X-Correlation-ID>b8268033-de67-4fa0-bf06-caebbfa5117a</m:X-Correlation-ID>
        </soap:Header>
        <soap:Body>
            <m:MRequestResponse>
                <return>
                    <c>OK</c>
                </return>
            </m:MRequestResponse>
        </soap:Body>
    </soap:Envelope>

(4) Response Body

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Body>
            <m:MRequestResponseResponse>
                <return>
                    <outcome>OK</outcome>
                </return>
            </m:MRequestResponseResponse>
        </soap:Body>
    </soap:Envelope>

.. _paragrafo-nonbloccante-2:

Profilo non bloccante RPC PULL (busy waiting)
---------------------------------------------

.. _scenario-nonbloccante-2:

Scenario
~~~~~~~~

Questo scenario è simile al precedente, di cui eredita le motivazioni,
ma in questo caso si decide che il fruitore
non fornisce un indirizzo di callback, mentre
l’erogatore fornisce un indirizzo interrogabile per verificare lo stato
di processamento di una richiesta e, al fine dell'elaborazione della
stessa, il risultato.

.. _descrizione-nonbloccante-2:

.. TODO referenze per modello POST + Location -> GET
    https://developer.openstack.org/api-ref/compute/?expanded=create-server-detail,delete-server-detail


Descrizione
~~~~~~~~~~~

Questo scenario prevede due possibili workflow, uno per REST ed uno
per SOAP.

Il fruitore invia una richiesta (passo (1)) e riceve immediatamente un acknowledge (passo (2)) insieme ad:

- un indirizzo dove verificare lo stato del processamento o della risorsa (REST);
- oppure un correlation ID (SOAP).

D'ora in poi il fruitore, periodicamente, verifica lo stato della richiesta
utilizzando (passo (3)):

- l'url indicato (REST)
- oppure il correlation ID (SOAP)

fin quando la risposta alla richiesta sarà pronta (passo (4)).

Gli intervalli di polling possono essere
definiti tramite i meccanismi definiti in "Robustezza".


A questo punto il fruitore può accedere al risultato o alla risorsa finale (passi (5) e (6)).

.. _interfaccia-rest-nonbloccante-2:

Interfaccia REST
~~~~~~~~~~~~~~~~

.. mermaid::
   :caption: Interazione non bloccante tramite busy waiting
   :alt: Interazione non bloccante tramite busy waiting

   sequenceDiagram
        participant F as Fruitore
        participant E as Erogatore
        activate F
        F ->> E: 1. Request()
        activate E
        E -->>F: 2. Location
        deactivate F
        deactivate E
        loop check status
        activate F
        F ->>E: 3. RetrieveResource()
        activate E
        E-->> F : 4. Not Ready
        deactivate F
        deactivate E
        end
        activate F
        F ->>E: 5. RetrieveResource()
        activate E
        E-->> F : 6. Resource
        deactivate F
        deactivate E


Nel caso in cui il profilo venga implementato con tecnologia REST,
DEVONO essere rispettate le seguenti regole:

-  La specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   codici di stato HTTP restituiti con relativo schema della risposta,
   oltre che ad eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare gli schemi delle
   richieste insieme ad eventuali header HTTP richiesti;

-  Al passo (1), il fruitore DEVE utilizzare il verbo HTTP POST;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, un percorso di risorsa per interrogare lo
   stato di processamento della richiesta utilizzando :httpheader:`Location`;
   Il codice HTTP di stato DEVE essere :httpstatus:`202` a meno che non si verifichino errori;

-  Al passo (3), il fruitore DEVE utilizzare il percorso di cui al passo
   (2) per richiedere lo stato della risorsa; Il verbo HTTP
   utilizzato deve essere GET;

-  Al passo (4) l’erogatore indica che la risorsa non è ancora pronta,
   fornendo informazioni circa lo stato della lavorazione
   della richiesta; il codice HTTP restituito è :httpstatus:`200`;

-  Se la risorsa è pronta (passo (5)), l’erogatore
   risponde con la rappresentazione della risorsa;


.. _regole-di-processamento-nonbloccante-4:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al termine del processamento delle richieste, l’erogatore deve fare uso
dei codici di stato HTTP rispettandone la semantica [3]_. In
particolare, al ricevimento della richiesta da parte del fruitore,
l’erogatore DEVE almeno:

-  Verificare la validità sintattica dei dati in ingresso. In caso di
   dati errati deve restituire  :httpstatus:`400`   fornendo
   nel body di risposta dettagli circa l’errore;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVE restituire  :httpstatus:`404`  , indicando nel body di
   risposta quale degli ID è mancante;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi ed indicando
   nel body di risposta il motivo dell’errore;

-  Al momento della ricezione della richiesta, l’erogatore DEVE restituire
   :httpstatus:`202`. In caso di ricezione corretta della risposta,
   il fruitore DEVE restituire :httpstatus:`200`  , riempiendo il body di
   risposta con il risultato dell’operazione. Nel caso di errore al
   momento di ricezione della risposta da parte del fruitore, è
   possibile definire meccanismi specifici per la ritrasmissione della
   risposta o della richiesta.


.. _esempio-nonbloccante-4:

Esempio
^^^^^^^

Specifica Servizio Server: https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/openapi.yaml

.. literalinclude:: ../media/rest-nonblocking.yaml
   :language: yaml

----

Di seguito un esempio di chiamata ad M in cui l’erogatore dichiara di
essersi preso carico della richiesta.

----

**Endpoint**
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M

.. code-block:: http

  POST /rest/v1/nomeinterfacciaservizio/resources/1234/M   HTTP/1.1

  {
     "a": {
       "a1": [1,...,2],
       "a2": "Stringa di esempio"
     },
     "b": "Stringa di esempio"
   }

.. code-block:: http

  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Location:  resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

   {
     "status": "accepted",
     "message": "Preso carico della richiesta",
     "id": "8131edc0-29ed-4d6e-ba43-cce978c7ea8d"
   }

----

Di seguito un esempio di chiamata con cui il fruitore verifica
l’esecuzione di M nei casi di processamento ancora in atto (4) e di
processamento avvenuto (5).

**Endpoint**
http://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

.. code-block:: http

    HTTP/1.1 200 Success

    {
      "status": "processing",
      "message": "Richiesta in fase di processamento"
    }


.. code-block:: http

    HTTP/1.1 303 Permanent

    {
      "status": "done",
      "message": "Processamento completo"
    }

----

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.


Endpoint http://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result


.. code-block:: http

    HTTP/1.1 200 Success

    {
      "c": "OK"
    }



.. _interfaccia-soap-nonbloccante-2:

Interfaccia SOAP
~~~~~~~~~~~~~~~~

.. mermaid::
   :caption: Interazione non bloccante tramite busy waiting
   :alt: interazione non bloccante tramite busy waiting

    sequenceDiagram
        participant F as Fruitore
        participant E as Erogatore
        activate F
        F ->> E: 1. Request()
        activate E
        E -->>F: 2. CorrelationID
        deactivate F
        deactivate E
        loop 0..n
            activate F
            F ->>E: 3. CheckStatus(CorrelationID)
            activate E
            E-->> F : 4. CurrentStatus
            deactivate F
            deactivate E
        end
        activate F
        F ->>E: 5. RetriveResult(CorrelationID)
        activate E
        E-->> F : 6. Result
        deactivate F
        deactivate E


Nel caso in cui il profilo venga implementato con tecnologia SOAP,
DEVONO essere rispettate le seguenti regole:

-  L’interfaccia di servizio dell’erogatore fornisce tre metodi
   differenti al fine di inoltrare una richiesta, controllarne lo stato
   ed ottenerne il risultato;

-  La specifica dell’interfaccia dell’erogatore DEVE indicare l’header
   SOAP X-Correlation-ID;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, un correlation ID riportato nel header
   custom SOAP X-Correlation-ID;

-  Al passo (3), il fruitore DEVE utilizzare i l correlation ID ottenuto
   al passo (2) per richiedere lo stato di processamento di una
   specifica richiesta;

-  Al passo (4) l’erogatore, quando il processamento non si è ancora
   concluso fornisce informazioni circa lo stato della lavorazione
   della richiesta, quando invece il processamento si è concluso risponde
   indicando in maniera esplicita il completamento;

-  Al passo (5), il fruitore utilizza il correlation ID di cui al passo
   (2) al fine di richiedere il risultato della richiesta;

-  Al passo (6), l’erogatore fornisce il risultato del processamento.


.. _regole-di-processamento-nonbloccante-5:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire :httpstatus:`500` fornendo dettagli
   circa l’errore utilizzando il meccanismo della SOAP fault;

-  Nel caso in cui qualcuno degli ID nel messaggio non esista,
   DEVE restituire :httpstatus:`500` indicando tramite la SOAP fault
   quale degli ID è mancante;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire il
   codice :httpstatus:`500`, indicando il motivo dell’errore nella SOAP fault;

-  In caso di successo restituire :httpstatus:`200`, riempiendo il
   body di risposta con il risultato dell’operazione.



.. _esempio-nonbloccante-5:

Esempio
^^^^^^^

Specifica Servizio Server: https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1?wsdl

.. literalinclude:: ../media/soap-nonblocking.wsdl
   :language: XML

----

Di seguito un esempio di chiamata ad M in cui l’erogatore risponde di
avere preso in carico la richiesta.

**Endpoint**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1

**Method**
MRequest

- 1\) Richiesta

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Body>
            <m:MRequest
                    <M>
                        <o_id>1234</o_id>
                        <a>
                            <a1s>1</a1s>
                            <a2>prova</a2>
                        </a>
                        <b>prova</b>
                    </M>
                </m:MRequest>
            </soap:Body>
    </soap:Envelope>

- 2\) Risposta

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
            <soap:Header>
                <m:X-Correlation-ID>c8e191a8-f34f-41ed-82ea-68e096466707</m:X-Correlation-ID>
            </soap:Header>
            <soap:Body>
                <m:MRequestResponse>
                    <return>
                        <status>accepted</status>
                        <message>Preso carico della richiesta</message>
                    </return>
                </m:MRequestResponse>
            </soap:Body>
    </soap:Envelope>


Di seguito un esempio di chiamata con cui il fruitore verifica
l’esecuzione di M nei casi di processamento ancora in atto e di
processamento avvenuto (4).


**Endpoint**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1

**Method**
MProcessingStatus


- 3\) richiesta verifica status

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
            <soap:Header>
                <m:X-Correlation-ID>c8e191a8-f34f-41ed-82ea-68e096466707</m:X-Correlation-ID>
            </soap:Header>
            <soap:Body>
                <m:MProcessingStatus/>
            </soap:Body>
    </soap:Envelope>

- 4\) risposta verifica status in attesa

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
            <soap:Body>
                <m:MProcessingStatusResponse>
                    <return>
                        <status>processing</status>
                        <message>Richiesta in fase di processamento</message>
                    </return>
                </m:MProcessingStatusResponse>
            </soap:Body>
    </soap:Envelope>

- 4\) risposta verifica status completato

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Body>
            <m:MProcessingStatusResponse>
                <return>
                    <status>done</status>
                    <message>Richiesta completata</message>
                </return>
            </m:MProcessingStatusResponse>
        </soap:Body>
    </soap:Envelope>




Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

**Endpoint**
https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1

**Method**
MProcessingStatus

- 5\) richiesta recupero entry


.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Header>
            <m:X-Correlation-ID>c8e191a8-f34f-41ed-82ea-68e096466707</m:X-Correlation-ID>
        </soap:Header>
        <soap:Body>
            <m:MResponse/>
        </soap:Body>
    </soap:Envelope>

- 6\) risposta recupero entry

.. code-block:: XML

    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:m="http://amministrazioneesempio.it/nomeinterfacciaservizio">
        <soap:Body>
            <m:MResponseResponse">
                <return>
                    <c>OK</c>
                </return>
            </m:MResponseResponse>
        </soap:Body>
    </soap:Envelope>




.. [1]
   Cf. https://swagger.io/docs/specification/callbacks/

.. [2]
   http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

.. [3]
   http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
