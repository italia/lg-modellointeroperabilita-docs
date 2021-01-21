Pattern non bloccante RPC PUSH (basato su callback)
===================================================

Questo caso particolare, denominato RPC PUSH, è utilizzabile nel caso in
cui il fruitore abbia a sua volta la possibilità di esporre una
interfaccia di servizio per la ricezione delle risposte.

.. mermaid::

   sequenceDiagram
     activate Fruitore
     activate Erogatore
     Fruitore->>+Erogatore: 1. Request(callback endpoint)
     Erogatore-->>Fruitore: 2. CorrelationID
     Erogatore->>Fruitore: 3. Reply(CorrelationID)
     Fruitore-->>Erogatore: 4. Ack
     deactivate Erogatore
     deactivate Fruitore

*Figura 2 - Interazione non bloccante tramite callback*

In questo pattern (vedi figura), la richiesta del fruitore contiene un
riferimento al servizio da chiamare al momento della risposta. Si
suppone infatti che i fruitori espongano a loro volta delle interfacce
con segnatura standard. Al momento del ricevimento della richiesta
(passo 1), l’erogatore risponde (passo 2) riconoscendo l’avvenuta
ricezione (acknowledgement o in breve ack) ed indica un CorrelationID
(ID di correlazione), generato lato erogatore, che permetta al fruitore,
una volta ricevuta la risposta, di accoppiarla alla richiesta originale.
Quando il processamento è terminato infatti, l’erogatore (passo 3)
chiama il fruitore (invertendo quindi i ruoli chiamato/chiamante)
riportando l’esito ed indicando il CorrelationID. Il fruitore riconosce
(sempre mediante un messaggio di ack) la ricezione della risposta (passo
4).

[NONBLOCK_PUSH_REST] Not Blocking Push REST
-------------------------------------------

Nel caso in cui il pattern venga implementato con tecnologia REST,
DEVONO essere rispettate le seguenti indicazioni:

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare tutti i codici di stato HTTP previsti dall'interfaccia,
   con il relativo schema della risposta, oltre che ad eventuali header
   HTTP restituiti;

-  Le specifiche delle interfacce del fruitore e dell’erogatore DEVONO
   dichiarare gli schemi delle richieste insieme ad eventuali header
   HTTP richiesti;

-  La specifica dell’interfaccia dell’erogatore deve dichiarare tramite
   il formalismo specifico il formato delle callback; questa specifica
   deve essere rispettata dall’interfaccia esposta dal fruitore, e
   quindi nella rispettiva specifica;

-  Al passo (1), il fruitore DEVE indicare l’endpoint della callback
   utilizzando l’header HTTP custom *X-ReplyTo* ed usando HTTP method
   POST ;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, il CorrelationID utilizzando l’header HTTP
   custom *X-Correlation-ID*; Il codice HTTP di stato DEVE essere HTTP
   status 202 Accepted a meno che non si verifichino errori;

-  Al passo (3), l’erogatore DEVE utilizzare lo stesso CorrelationID
   fornito al passo (2) sempre utilizzando l’header HTTP custom
   *X-Correlation-ID*; Il verbo HTTP utilizzato deve essere POST;

-  Al passo (4), il fruitore DEVE riconoscere tramite un messaggio di
   acknowledgement il ricevimento della risposta; Il codice HTTP di
   stato DEVE essere HTTP status 200 OK a meno che non si verifichino
   errori.

Regole di processamento
------------------------------------------------------------

Al termine del processamento delle richieste, l’erogatore ed il fruitore
DEVONO fare uso dei codici di stato HTTP rispettando la semantica.
Fruitore ed erogatore:

-  DEVONO verificare la validità sintattica dei dati in ingresso. In
   caso di dati errati DEVONO restituire HTTP status 500 Internal Server
   Error fornendo dettagli circa l’errore;

-  In caso di dati errati DEVONO restituire HTTP status 400 Bad Request
   fornendo nel body di risposta dettagli circa l’errore;

-  In caso di representation semanticamente non corretta DEVONO
   ritornare HTTP status 422 Unprocessable Entity;

-  Se qualcuno degli ID nel path o nel body non esiste, DEVONO
   restituire HTTP status 404 Not Found, indicando nel body di risposta
   quale degli ID è mancante;

-  Se si ipotizza che la richiesta sia malevola, PUÒ ritornare HTTP
   status 400 Bad Request o HTTP status 404 Not Found

-  In caso di errori non dipendenti dalla richiesta, DEVONO restituire
   HTTP status 5XX rispettando la semantica degli stessi;

-  Al momento della ricezione della richiesta, l’erogatore DEVE
   restituire HTTP status 202 Accepted. In caso di ricezione corretta
   della risposta, il fruitore DEVE restituire HTTP status 200 OK,
   ritornando nel body di risposta un acknowledgement dell’avvenuta
   ricezione. In caso di errore di ricezione della risposta da parte del
   fruitore, è possibile utilizzare meccanismi specifici per la
   ritrasmissione della risposta o della richiesta.

NB: I messaggi di errore devono essere utili al client ma NON DEVONO
rivelare dettagli tecnici e/o informazioni riservate.

.. _esempio-2:

Esempio
~~~~~~~

Specifica Servizio Server

https://api.ente.example/rest/nome-api/v1/RESTCallbackServer.yaml

.. literalinclude:: RESTCallbackServer.yaml
   :language: yaml

Specifica Servizio Client

https://api.indirizzoclient.it/rest/nome-api/v1/RESTCallbackClient.yaml

.. literalinclude:: RESTCallbackClient.yaml
   :language: yaml

Di seguito un esempio di chiamata al metodo **M** con la presa in carico
da parte dell’erogatore.

HTTP Operation POST

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request Header & Body

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Content-Type: application/json
   X-ReplyTo: https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse
   
   {
   "a": {
	   "a1": [1,...,2],
	   "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
	   },
   "b": "Stringa di esempio"
   }

2. Response Header & Body (HTTP status 202 Accepted)

.. code-block:: http

   HTTP/1.1 202 Accepted
   Content-Type: application/json
   X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d
   
   { "result" : "ACK" }

Di seguito un esempio di risposta da parte dell’erogatore verso il
fruitore.

Endpoint

https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

3. Request Header & Body

.. code-block:: http

   POST /rest/v1/nomeinterfacciaclient/Mresponse HTTP/1.1
   X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d
   
   { "c": "OK" }

4. Response Header & Body (HTTP status 200 OK)

.. code-block:: http

   HTTP/1.1 200 Ok
   Content-Type: application/json
   
   { "result" : "ACK" }

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
------------------------------------------------------------

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
In particolare, al ricevimento della richiesta, fruitore ed erogatore:

-  DEVONO verificare la validità sintattica dei dati in ingresso. In
   caso di dati errati DEVONO restituire HTTP status 500 Internal Server
   Error fornendo dettagli circa l’errore, utilizzando il meccanismo
   della SOAP fault;

-  Nel caso in cui qualcuno degli ID nel path o nel body non esista,
   DEVONO restituire HTTP status 500 Internal Server Error, indicando
   nel body di risposta quale degli ID è mancante;

-  Se ipotizzano che la richiesta sia malevola POSSONO ritornare HTTP
   status 400 Bad Request o HTTP status 404 Not Found

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice HTTP status 500 indicando il motivo dell’errore nella SOAP
   fault;

-  Al momento della ricezione della richiesta, DEVONO restituire un
   codice 2XX, nel dettaglio:

   -  HTTP status 200 OK in caso di presenza della payload SOAP,
      riempiendo il body di risposta con il risultato relativo alla
      richiesta.

   -  HTTP status 200 OK o HTTP status 202 Accepted in caso di assenza
      della payload SOAP

-  Nel caso di errore al momento di ricezione della risposta da parte
   del richiedente (fruitore o erogatore), è possibile definire
   meccanismi specifici per la ri-trasmettere le richieste.

Esempio
------------------------------------------------------------

Specifica Servizio Server

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: file-d40e5a24d62efffebf0f956ce2b3b7e589e078c95d575e0658cec741f3a6d2da.xml
   :language: xml

Specifica Servizio Callback

https://api.indirizzoclient.it/soap/nome-api/v1?wsdl

.. literalinclude:: file-b039dfb9ab827b230f905ccfe56b8b7f05f6e56febea80c9f586376e64943256.xml
   :language: xml

Segue un esempio di chiamata al metodo **M** in cui l’erogatore conferma
di essersi preso carico della richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

.. literalinclude:: SOAPCallbackRequestResponses.xml
   :language: xml
   :lines: 2-18


2. Response Body

.. literalinclude:: SOAPCallbackRequestResponses.xml
   :language: xml
   :lines: 21-32

Di seguito un esempio di risposta da parte dell’erogatore verso il
fruitore.

Endpoint

https://api.indirizzoclient.it/soap/nomeinterfacciaclient/v1Method

MRequestResponse

3. Response Body

.. literalinclude:: SOAPCallbackRequestResponses.xml
   :language: xml
   :lines: 35-46

4. Response Body

.. literalinclude:: SOAPCallbackRequestResponses.xml
   :language: xml
   :lines: 49-57

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
      activate Erogatore
      Fruitore->>+Erogatore: 1. Request(callback endpoint)
      Erogatore-->>Fruitore: 2. CorrelationID
      Erogatore->>Fruitore: 3. Reply(CorrelationID)
      Fruitore-->>Erogatore: 4. Ack
      deactivate Erogatore
      deactivate Fruitore

