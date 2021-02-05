[NONBLOCK_PUSH_SOAP] Not Blocking Push SOAP
-------------------------------------------

Nel caso di implementazione mediante tecnologia SOAP, l’endpoint di
callback ed il CorrelationID, vengono inseriti all’interno dell’header
SOAP come campi custom. Erogatore e fruitore DEVONO inoltre seguire le
seguenti regole:

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare tutti i metodi esposti con relativi schemi dei messaggi di
   richiesta e di ritorno. Inoltre le interfacce devono specificare
   eventuali header SOAP richiesti;

-  La specifica dell’interfaccia del fruitore DEVE rispettare quanto
   richiesto dall’erogatore; in particolare si richiede che l’erogatore
   fornisca un WSDL descrittivo del servizio di callback che il fruitore
   è tenuto ad implementare;

-  Al passo (1), il fruitore DEVE indicare l’endpoint della callback
   utilizzando l’header SOAP custom X-ReplyTo;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, il CorrelationID utilizzando l’header SOAP
   custom X-Correlation-ID;

-  Al passo (3), l’erogatore DEVE utilizzare lo stesso CorrelationID
   fornito al passo (2) sempre utilizzando l’header SOAP custom
   X-Correlation-ID;

-  Al passo (4), il fruitore DEVE riconoscere tramite un messaggio di
   acknowledgement il ricevimento della risposta.

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
In particolare, al ricevimento della richiesta, fruitore ed erogatore:

-  DEVONO verificare la validità sintattica dei dati in ingresso. In
   caso di dati errati DEVONO restituire HTTP status 500 Internal Server
   Error fornendo dettagli circa l’errore, utilizzando il meccanismo
   della SOAP fault;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVONO restituire :httpstatus:`500`, indicando
   nel body di risposta quale degli ID è mancante;

-  Se ipotizzano che la richiesta sia malevola POSSONO ritornare HTTP
   status 400 Bad Request o :httpstatus:`404`

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice HTTP status 500 indicando il motivo dell’errore nella SOAP
   fault;

-  Al momento della ricezione della richiesta, DEVONO restituire un
   codice 2XX, nel dettaglio:

   -  :httpstatus:`200` in caso di presenza della payload SOAP,
      riempiendo il body di risposta con il risultato relativo alla
      richiesta.

   -  :httpstatus:`200` o HTTP status 202 Accepted in caso di assenza
      della payload SOAP

-  Nel caso di errore al momento di ricezione della risposta da parte
   del richiedente (fruitore o erogatore), è possibile definire
   meccanismi specifici per la ri-trasmettere le richieste.

Esempio
^^^^^^^

Specifica Servizio Erogatore

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_wsdl_erogatore.xml
   :language: xml

Specifica Servizio Fruitore (callback)

https://api.indirizzoclient.it/soap/nome-api/v1?wsdl

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_wsdl_fruitore.xml
   :language: xml

Segue un esempio di chiamata al metodo **M** in cui l’erogatore conferma
di essersi preso carico della richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_request_to_erogatore.xml
   :language: xml

2. Response Body

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_response_from_erogatore.xml
   :language: xml

Di seguito un esempio di richiesta da parte dell’erogatore verso la callback del
fruitore.

Endpoint

https://api.indirizzoclient.it/soap/nomeinterfacciaclient/v1Method

MRequestResponse

3. Request Body

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_request_to_fruitore.xml
   :language: xml

4. Response Body

.. literalinclude:: NONBLOCK_PUSH_SOAP_example_response_from_fruitore.xml
   :language: xml

.. forum_italia::
   :topic_id: 21457
   :scope: document
