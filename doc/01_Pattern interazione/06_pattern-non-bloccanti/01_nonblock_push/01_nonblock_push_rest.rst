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
   stato DEVE essere :httpstatus:`200` a meno che non si verifichino
   errori.

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

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
   restituire :httpstatus:`404`, indicando nel body di risposta
   quale degli ID è mancante;

-  Se si ipotizza che la richiesta sia malevola, PUÒ ritornare HTTP
   status 400 Bad Request o :httpstatus:`404`

-  In caso di errori non dipendenti dalla richiesta, DEVONO restituire
   HTTP status 5XX rispettando la semantica degli stessi;

-  Al momento della ricezione della richiesta, l’erogatore DEVE
   restituire HTTP status 202 Accepted. In caso di ricezione corretta
   della risposta, il fruitore DEVE restituire :httpstatus:`200`,
   ritornando nel body di risposta un acknowledgement dell’avvenuta
   ricezione. In caso di errore di ricezione della risposta da parte del
   fruitore, è possibile utilizzare meccanismi specifici per la
   ritrasmissione della risposta o della richiesta.

NB: I messaggi di errore devono essere utili al client ma NON DEVONO
rivelare dettagli tecnici e/o informazioni riservate.

.. _esempio-2:

Esempio
^^^^^^^

Specifica Servizio Server

https://api.ente.example/rest/nome-api/v1/RESTCallbackServer.yaml

.. literalinclude:: RESTCallbackServer.yaml
   :language: yaml

Specifica Servizio Client

https://api.indirizzoclient.it/rest/nome-api/v1/RESTCallbackClient.yaml

.. literalinclude:: RESTCallbackClient.yaml
   :language: yaml


Di seguito il fruitore effettua una richiesta al metodo **M**;
l'erogatore conferma la presa in carico della richiesta ritornando
:httpstatus:`202`.


Endpoint: https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Host: api.ente.example
   Content-Type: application/json
   X-ReplyTo: https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

   {
     "a": {
       "a1": [ 1, "..", 2 ],
       "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
     },
     "b": "Stringa di esempio"
   }


2. Response

.. code-block:: http

   HTTP/1.1 202 Accepted
   Content-Type: application/json
   X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d

   {"result": "ACK"}


Quindi l'erogatore notifica al fruitore l'avvenuto processamento
delle informazioni tramite una :httpmethod:`POST` all'URL concordato.
Il fruitore conferma con :httpstatus:`200` l'avvenuta ricezione
della notifica.

Endpoint

https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

3. Request

.. code-block:: http

   POST /rest/v1/nomeinterfacciaclient/Mresponse HTTP/1.1
   Host: api.indirizzoclient.it
   Content-Type: application/json
   X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d

   {"c": "OK"}

4. Response

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {"result": "ACK"}

.. forum_italia::
   :topic_id: 21456
   :scope: document
