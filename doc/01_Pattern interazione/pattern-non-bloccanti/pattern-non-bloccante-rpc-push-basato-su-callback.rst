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

   1. .. rubric:: Regole di processamento
         :name: regole-di-processamento-2

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

+-------------------------------------------------------------------------+
| **openapi**: 3.0.1                                                      |
|                                                                         |
| **info**:                                                               |
|                                                                         |
| **title**: RESTCallbackServer                                           |
|                                                                         |
| **version**: "1.0"                                                      |
|                                                                         |
| **description**: \|-                                                    |
|                                                                         |
| Questo file descrive semplicemente i metodi di un'API                   |
|                                                                         |
| e non indica tutte le informazioni di metadatazione che                 |
|                                                                         |
| normalmente vanno inserite.                                             |
|                                                                         |
| **license**:                                                            |
|                                                                         |
| **name**: Apache 2.0 License                                            |
|                                                                         |
| **url**: http://www.apache.org/licenses/LICENSE-2.0.html                |
|                                                                         |
| **paths**:                                                              |
|                                                                         |
| /resources/{id_resource}/M:                                             |
|                                                                         |
| **post**:                                                               |
|                                                                         |
| **description**: M                                                      |
|                                                                         |
| **operationId**: PushMessage                                            |
|                                                                         |
| **parameters**:                                                         |
|                                                                         |
| - **name**: X-ReplyTo                                                   |
|                                                                         |
| **in**: header                                                          |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| - **name**: id_resource                                                 |
|                                                                         |
| **in**: path                                                            |
|                                                                         |
| **required**: true                                                      |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **type**: integer                                                       |
|                                                                         |
| **format**: int32                                                       |
|                                                                         |
| **requestBody**:                                                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/MType'                                  |
|                                                                         |
| **responses**:                                                          |
|                                                                         |
| **202**:                                                                |
|                                                                         |
| **description**: Preso carico correttamente di M                        |
|                                                                         |
| **headers**:                                                            |
|                                                                         |
| **X-Correlation-ID**:                                                   |
|                                                                         |
| **required**: true                                                      |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ACKMessage'                             |
|                                                                         |
| **400**:                                                                |
|                                                                         |
| **description**: Richiesta non valida                                   |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **404**:                                                                |
|                                                                         |
| **description**: Identificativo non trovato                             |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **default**:                                                            |
|                                                                         |
| **$ref**: '#/components/responses/default'                              |
|                                                                         |
| **callbacks**:                                                          |
|                                                                         |
| **completionCallback**:                                                 |
|                                                                         |
| '{$request.header#/X-ReplyTo}':                                         |
|                                                                         |
| **post**:                                                               |
|                                                                         |
| **requestBody**:                                                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/MResponseType'                          |
|                                                                         |
| **responses**:                                                          |
|                                                                         |
| **200**:                                                                |
|                                                                         |
| **description**: Risposta correttamente ricevuta                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ACKMessage'                             |
|                                                                         |
| **default**:                                                            |
|                                                                         |
| **$ref**: '#/components/responses/default'                              |
|                                                                         |
| **components**:                                                         |
|                                                                         |
| **responses**:                                                          |
|                                                                         |
| **default**:                                                            |
|                                                                         |
| **description**: \|-                                                    |
|                                                                         |
| Errore inatteso. Non ritornare informazioni                             |
|                                                                         |
| sulla logica interna e/o non pertinenti all'interfaccia.                |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **schemas**:                                                            |
|                                                                         |
| **MType**:                                                              |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **a**:                                                                  |
|                                                                         |
| **$ref**: '#/components/schemas/AComplexType'                           |
|                                                                         |
| **b**:                                                                  |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **ACKMessage**:                                                         |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **outcome**:                                                            |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **MResponseType**:                                                      |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **c**:                                                                  |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **AComplexType**:                                                       |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **a1s**:                                                                |
|                                                                         |
| **type**: array                                                         |
|                                                                         |
| **items**:                                                              |
|                                                                         |
| **type**: integer                                                       |
|                                                                         |
| **format**: int32                                                       |
|                                                                         |
| **a2**:                                                                 |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **ErrorMessage**:                                                       |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **detail**:                                                             |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| A human readable explanation specific to this occurrence of the         |
|                                                                         |
| problem.                                                                |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **instance**:                                                           |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| An absolute URI that identifies the specific occurrence of the problem. |
|                                                                         |
| It may or may not yield further information if dereferenced.            |
|                                                                         |
| **format**: uri                                                         |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **status**:                                                             |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| The HTTP status code generated by the origin server for this occurrence |
|                                                                         |
| of the problem.                                                         |
|                                                                         |
| **exclusiveMaximum**: true                                              |
|                                                                         |
| **format**: int32                                                       |
|                                                                         |
| **maximum**: 600                                                        |
|                                                                         |
| **minimum**: 100                                                        |
|                                                                         |
| **type**: integer                                                       |
|                                                                         |
| **title**:                                                              |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| A short, summary of the problem type. Written in english and readable   |
|                                                                         |
| for engineers (usually not suited for non technical stakeholders and    |
|                                                                         |
| not localized); example: Service Unavailable                            |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **type**:                                                               |
|                                                                         |
| **default**: about:blank                                                |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| An absolute URI that identifies the problem type. When dereferenced,    |
|                                                                         |
| it SHOULD provide human-readable documentation for the problem type     |
|                                                                         |
| (e.g., using HTML).                                                     |
|                                                                         |
| **format**: uri                                                         |
|                                                                         |
| **type**: string                                                        |
+-------------------------------------------------------------------------+

Specifica Servizio Client

https://api.indirizzoclient.it/rest/nome-api/v1/RESTCallbackClient.yaml

+-------------------------------------------------------------------------+
| **openapi**: 3.0.1                                                      |
|                                                                         |
| **info**:                                                               |
|                                                                         |
| **title**: RESTCallbackClient                                           |
|                                                                         |
| **version**: "1.0"                                                      |
|                                                                         |
| **description**: \|-                                                    |
|                                                                         |
| Questo file descrive semplicemente i metodi di un'API                   |
|                                                                         |
| e non indica tutte le informazioni di metadatazione che                 |
|                                                                         |
| normalmente vanno inserite.                                             |
|                                                                         |
| **license**:                                                            |
|                                                                         |
| **name**: Apache 2.0 License                                            |
|                                                                         |
| **url**: http://www.apache.org/licenses/LICENSE-2.0.html                |
|                                                                         |
| **paths**:                                                              |
|                                                                         |
| **/MResponse**:                                                         |
|                                                                         |
| **post**:                                                               |
|                                                                         |
| **description**: M                                                      |
|                                                                         |
| **operationId**: PushResponseMessage                                    |
|                                                                         |
| **parameters**:                                                         |
|                                                                         |
| - **name**: X-Correlation-ID                                            |
|                                                                         |
| **in**: header                                                          |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **requestBody**:                                                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/MResponseType'                          |
|                                                                         |
| **responses**:                                                          |
|                                                                         |
| **200**:                                                                |
|                                                                         |
| **description**: Risposta correttamente ricevuta                        |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ACKMessage'                             |
|                                                                         |
| **400**:                                                                |
|                                                                         |
| **description**: Richiesta non valida                                   |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **404**:                                                                |
|                                                                         |
| **description**: Identificativo non trovato                             |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **default**:                                                            |
|                                                                         |
| **description**: \|-                                                    |
|                                                                         |
| Errore inatteso. Non ritornare informazioni                             |
|                                                                         |
| sulla logica interna e/o non pertinenti all'interfaccia.                |
|                                                                         |
| **content**:                                                            |
|                                                                         |
| **application/json**:                                                   |
|                                                                         |
| **schema**:                                                             |
|                                                                         |
| **$ref**: '#/components/schemas/ErrorMessage'                           |
|                                                                         |
| **components**:                                                         |
|                                                                         |
| **schemas**:                                                            |
|                                                                         |
| **ACKMessage**:                                                         |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **outcome**:                                                            |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **MResponseType**:                                                      |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **c**:                                                                  |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **ErrorMessage**:                                                       |
|                                                                         |
| **type**: object                                                        |
|                                                                         |
| **properties**:                                                         |
|                                                                         |
| **detail**:                                                             |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| A human readable explanation specific to this occurrence of the         |
|                                                                         |
| problem.                                                                |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **instance**:                                                           |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| An absolute URI that identifies the specific occurrence of the problem. |
|                                                                         |
| It may or may not yield further information if dereferenced.            |
|                                                                         |
| **format**: uri                                                         |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **status**:                                                             |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| The HTTP status code generated by the origin server for this occurrence |
|                                                                         |
| of the problem.                                                         |
|                                                                         |
| **exclusiveMaximum**: true                                              |
|                                                                         |
| **format**: int32                                                       |
|                                                                         |
| **maximum**: 600                                                        |
|                                                                         |
| **minimum**: 100                                                        |
|                                                                         |
| **type**: integer                                                       |
|                                                                         |
| **title**:                                                              |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| A short, summary of the problem type. Written in english and readable   |
|                                                                         |
| for engineers (usually not suited for non technical stakeholders and    |
|                                                                         |
| not localized); example: Service Unavailable                            |
|                                                                         |
| **type**: string                                                        |
|                                                                         |
| **type**:                                                               |
|                                                                         |
| **default**: about:blank                                                |
|                                                                         |
| **description**: \|                                                     |
|                                                                         |
| An absolute URI that identifies the problem type. When dereferenced,    |
|                                                                         |
| it SHOULD provide human-readable documentation for the problem type     |
|                                                                         |
| (e.g., using HTML).                                                     |
|                                                                         |
| **format**: uri                                                         |
|                                                                         |
| **type**: string                                                        |
+-------------------------------------------------------------------------+

Di seguito un esempio di chiamata al metodo **M** con la presa in carico
da parte dell’erogatore.

HTTP Operation POST

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request Header & Body

+-----------------------------------------------------------------------+
| POST **/rest/nome-api/v1/resources/1234/M** **HTTP**/1.1              |
|                                                                       |
| Content-Type: application/json                                        |
|                                                                       |
| X-ReplyTo:                                                            |
| https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mrespons |
| e                                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| **"a"**: {                                                            |
|                                                                       |
| **"a1"**: [1,...,2],                                                  |
|                                                                       |
| **"a2"**: "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"                              |
|                                                                       |
| },                                                                    |
|                                                                       |
| **"b"**: "Stringa di esempio"                                         |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+

2. Response Header & Body (HTTP status 202 Accepted)

+--------------------------------------------------------+
| **HTTP**/1.1 202 Accepted                              |
|                                                        |
| Content-Type: application/json                         |
|                                                        |
| X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d |
|                                                        |
| {                                                      |
|                                                        |
| **"result"** : "ACK"                                   |
|                                                        |
| }                                                      |
+--------------------------------------------------------+

Di seguito un esempio di risposta da parte dell’erogatore verso il
fruitore.

Endpoint

https://api.indirizzoclient.it/rest/v1/nomeinterfacciaclient/Mresponse

3. Request Header & Body

+----------------------------------------------------------------+
| POST **/rest/v1/nomeinterfacciaclient/Mresponse** **HTTP**/1.1 |
|                                                                |
| X-Correlation-ID: 69a445fb-6a9f-44fe-b1c3-59c0f7fb568d         |
|                                                                |
| {                                                              |
|                                                                |
| **"c":** "OK"                                                  |
|                                                                |
| }                                                              |
+----------------------------------------------------------------+

4. Response Header & Body (HTTP status 200 OK)

+------------------------------------+
| **HTTP/1.1 200 Success**           |
|                                    |
| **Content-Type: application/json** |
|                                    |
| {                                  |
|                                    |
| **"result" : "**\ ACK\ **"**       |
|                                    |
| }                                  |
+------------------------------------+

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

   3. .. rubric:: Regole di processamento
         :name: regole-di-processamento-3

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

   4. .. rubric:: Esempio
         :name: esempio-3

Specifica Servizio Server

https://api.ente.example/soap/nome-api/v1?wsdl

+-----------------------------------------------------------------------+
| <?xml version="1.0"?>                                                 |
|                                                                       |
| **<wsdl:definitions**                                                 |
|                                                                       |
| xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"                         |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap12/"                  |
|                                                                       |
| name="SOAPCallbackServerService"                                      |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<wsdl:types>**                                                      |
|                                                                       |
| **<xs:schema**                                                        |
|                                                                       |
| xmlns:xs="http://www.w3.org/2001/XMLSchema"                           |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| attributeFormDefault="unqualified" elementFormDefault="unqualified"   |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<xs:element** name="MRequest" type="tns:MRequest"\ **/>**           |
|                                                                       |
| **<xs:element** name="MRequestResponse"                               |
| type="tns:MRequestResponse"\ **/>**                                   |
|                                                                       |
| **<xs:element** name="ErrorMessageFault" nillable="true"              |
| type="tns:errorMessageFault"\ **/>**                                  |
|                                                                       |
| **<xs:element** name="X-ReplyTo" nillable="true"                      |
| type="xs:string"\ **/>**                                              |
|                                                                       |
| **<xs:element** name="X-Correlation-ID" nillable="true"               |
| type="xs:string"\ **/>**                                              |
|                                                                       |
| **<xs:complexType** name="MRequest"\ **>**                            |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="M" type="tns:mType"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="mType"\ **>**                               |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="o_id" type="xs:int"\ **/>**       |
|                                                                       |
| **<xs:element** minOccurs="0" name="a"                                |
| type="tns:aComplexType"\ **/>**                                       |
|                                                                       |
| **<xs:element** minOccurs="0" name="b" type="xs:string"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="aComplexType"\ **>**                        |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** maxOccurs="unbounded" minOccurs="0" name="a1s"        |
| nillable="true" type="xs:string"\ **/>**                              |
|                                                                       |
| **<xs:element** minOccurs="0" name="a2" type="xs:string"\ **/>**      |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="MRequestResponse"\ **>**                    |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="return"                           |
| type="tns:ackMessage"\ **/>**                                         |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="ackMessage"\ **>**                          |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="outcome" type="xs:string"\ **/>** |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="errorMessageFault"\ **>**                   |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="customFaultCode"                  |
| type="xs:string"\ **/>**                                              |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **</xs:schema>**                                                      |
|                                                                       |
| **</wsdl:types>**                                                     |
|                                                                       |
| **<wsdl:message** name="MRequest"\ **>**                              |
|                                                                       |
| **<wsdl:part** element="tns:MRequest" name="parameters"\ **/>**       |
|                                                                       |
| **<wsdl:part** element="tns:X-ReplyTo" name="X-ReplyTo"\ **/>**       |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:message** name="MRequestResponse"\ **>**                      |
|                                                                       |
| **<wsdl:part** element="tns:MRequestResponse" name="result"\ **/>**   |
|                                                                       |
| **<wsdl:part** element="tns:X-Correlation-ID"                         |
| name="X-Correlation-ID"\ **/>**                                       |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:message** name="ErrorMessageException"\ **>**                 |
|                                                                       |
| **<wsdl:part** element="tns:ErrorMessageFault"                        |
| name="ErrorMessageException"\ **/>**                                  |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:portType** name="SOAPCallback"\ **>**                         |
|                                                                       |
| **<wsdl:operation** name="MRequest"\ **>**                            |
|                                                                       |
| **<wsdl:input** message="tns:MRequest" name="MRequest"\ **/>**        |
|                                                                       |
| **<wsdl:output** message="tns:MRequestResponse"                       |
| name="MRequestResponse"\ **/>**                                       |
|                                                                       |
| **<wsdl:fault** message="tns:ErrorMessageException"                   |
| name="ErrorMessageException"\ **/>**                                  |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:portType>**                                                  |
|                                                                       |
| **<wsdl:binding** name="SOAPCallbackServiceSoapBinding"               |
| type="tns:SOAPCallback"\ **>**                                        |
|                                                                       |
| **<soap:binding** style="document"                                    |
| transport="http://schemas.xmlsoap.org/soap/http"\ **/>**              |
|                                                                       |
| **<wsdl:operation** name="MRequest"\ **>**                            |
|                                                                       |
| **<soap:operation** soapAction="" style="document"\ **/>**            |
|                                                                       |
| **<wsdl:input** name="MRequest"\ **>**                                |
|                                                                       |
| **<soap:header** message="tns:MRequest" part="X-ReplyTo"              |
| use="literal"\ **/>**                                                 |
|                                                                       |
| **<soap:body** parts="parameters" use="literal"\ **/>**               |
|                                                                       |
| **</wsdl:input>**                                                     |
|                                                                       |
| **<wsdl:output** name="MRequestResponse"\ **>**                       |
|                                                                       |
| **<soap:header** message="tns:MRequestResponse"                       |
| part="X-Correlation-ID" use="literal"\ **/>**                         |
|                                                                       |
| **<soap:body** parts="result" use="literal"\ **/>**                   |
|                                                                       |
| **</wsdl:output>**                                                    |
|                                                                       |
| **<wsdl:fault** name="ErrorMessageException"\ **>**                   |
|                                                                       |
| **<soap:fault** name="ErrorMessageException" use="literal"\ **/>**    |
|                                                                       |
| **</wsdl:fault>**                                                     |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:binding>**                                                   |
|                                                                       |
| **<wsdl:service** name="SOAPCallbackService"\ **>**                   |
|                                                                       |
| **<wsdl:port** name="SOAPCallbackPort"                                |
| binding="tns:SOAPCallbackServiceSoapBinding" **>**                    |
|                                                                       |
| **<soap:address**                                                     |
| location="https://api.ente.example/soap/nome-api/v1"\ **/>**          |
|                                                                       |
| **</wsdl:port>**                                                      |
|                                                                       |
| **</wsdl:service>**                                                   |
|                                                                       |
| **</wsdl:definitions>**                                               |
+-----------------------------------------------------------------------+

Specifica Servizio Callback

https://api.indirizzoclient.it/soap/nome-api/v1?wsdl

+-----------------------------------------------------------------------+
| <?xml version='1.0' encoding='UTF-8'?>                                |
|                                                                       |
| **<wsdl:definitions**                                                 |
|                                                                       |
| xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"                         |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap12/"                  |
|                                                                       |
| name="SOAPCallbackClientInterfaceService"                             |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<wsdl:types>**                                                      |
|                                                                       |
| **<xs:schema**                                                        |
|                                                                       |
| xmlns:xs="http://www.w3.org/2001/XMLSchema"                           |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| attributeFormDefault="unqualified" elementFormDefault="unqualified"   |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<xs:element** name="MRequestResponse"                               |
| type="tns:MRequestResponse"\ **/>**                                   |
|                                                                       |
| **<xs:element** name="MRequestResponseResponse"                       |
| type="tns:MRequestResponseResponse"\ **/>**                           |
|                                                                       |
| **<xs:element** name="X-Correlation-ID" nillable="true"               |
| type="xs:string"\ **/>**                                              |
|                                                                       |
| **<xs:complexType** name="MRequestResponse"\ **>**                    |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="return"                           |
| type="tns:mResponseType"\ **/>**                                      |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="mResponseType"\ **>**                       |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="c" type="xs:string"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="MRequestResponseResponse"\ **>**            |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="return"                           |
| type="tns:ackMessage"\ **/>**                                         |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="ackMessage"\ **>**                          |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="outcome" type="xs:string"\ **/>** |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **</xs:schema>**                                                      |
|                                                                       |
| **</wsdl:types>**                                                     |
|                                                                       |
| **<wsdl:message** name="MRequestResponse"\ **>**                      |
|                                                                       |
| **<wsdl:part** element="tns:MRequestResponse"                         |
| name="parameters"\ **/>**                                             |
|                                                                       |
| **<wsdl:part** element="tns:X-Correlation-ID"                         |
| name="X-Correlation-ID"\ **/>**                                       |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:message** name="MRequestResponseResponse"\ **>**              |
|                                                                       |
| **<wsdl:part** element="tns:MRequestResponseResponse"                 |
| name="result"\ **/>**                                                 |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:portType** name="SOAPCallbackClient"\ **>**                   |
|                                                                       |
| **<wsdl:operation** name="MRequestResponse"\ **>**                    |
|                                                                       |
| **<wsdl:input** message="tns:MRequestResponse"                        |
| name="MRequestResponse"\ **/>**                                       |
|                                                                       |
| **<wsdl:output** message="tns:MRequestResponseResponse"               |
| name="MRequestResponseResponse"\ **/>**                               |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:portType>**                                                  |
|                                                                       |
| **<wsdl:binding** name="SOAPCallbackClientServiceSoapBinding"         |
| type="tns:SOAPCallbackClient"\ **>**                                  |
|                                                                       |
| **<soap:binding** style="document"                                    |
| transport="http://schemas.xmlsoap.org/soap/http"\ **/>**              |
|                                                                       |
| **<wsdl:operation** name="MRequestResponse"\ **>**                    |
|                                                                       |
| **<soap:operation** soapAction="" style="document"\ **/>**            |
|                                                                       |
| **<wsdl:input** name="MRequestResponse"\ **>**                        |
|                                                                       |
| **<soap:header** message="tns:MRequestResponse"                       |
| part="X-Correlation-ID" use="literal"\ **/>**                         |
|                                                                       |
| **<soap:body** parts="parameters" use="literal"\ **/>**               |
|                                                                       |
| **</wsdl:input>**                                                     |
|                                                                       |
| **<wsdl:output** name="MRequestResponseResponse"\ **>**               |
|                                                                       |
| **<soap:body** parts="result" use="literal" **/>**                    |
|                                                                       |
| **</wsdl:output>**                                                    |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:binding>**                                                   |
|                                                                       |
| **<wsdl:service** name="SOAPCallbackClientService"\ **>**             |
|                                                                       |
| **<wsdl:port** binding="tns:SOAPCallbackClientServiceSoapBinding"     |
| name="SOAPCallbackClientPort"\ **>**                                  |
|                                                                       |
| **<soap:address**                                                     |
| location="https://api.indirizzoclient.it/soap/nome-api/v1"\ **/>**    |
|                                                                       |
| **</wsdl:port>**                                                      |
|                                                                       |
| **</wsdl:service>**                                                   |
|                                                                       |
| **</wsdl:definitions>**                                               |
+-----------------------------------------------------------------------+

Segue un esempio di chiamata al metodo **M** in cui l’erogatore conferma
di essersi preso carico della richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

+-----------------------------------------------------------------------+
| **<soap:Envelope**                                                    |
|                                                                       |
| xmlns:soap="http://www.w3.org/2003/05/soap-envelope"                  |
|                                                                       |
| xmlns:m="http://ente.example/nome-api"\ **>**                         |
|                                                                       |
| **<soap:Header>**                                                     |
|                                                                       |
| **<m:X-ReplyTo>**\ https://api.indirizzoclient.it/soap/nome-api/v1\ * |
| *</m:X-ReplyTo>**                                                     |
|                                                                       |
| **</soap:Header>**                                                    |
|                                                                       |
| **<soap:Body>**                                                       |
|                                                                       |
| **<m:MRequest>**                                                      |
|                                                                       |
| **<M>**                                                               |
|                                                                       |
| **<o_id>**\ 1234\ **</o_id>**                                         |
|                                                                       |
| **<a>**                                                               |
|                                                                       |
| **<a1s>**\ 1\ **</a1s>**                                              |
|                                                                       |
| **<a2>**\ prova\ **</a2>**                                            |
|                                                                       |
| **</a>**                                                              |
|                                                                       |
| **<b>**\ prova\ **</b>**                                              |
|                                                                       |
| **</M>**                                                              |
|                                                                       |
| **</m:MRequest>**                                                     |
|                                                                       |
| **</soap:Body>**                                                      |
|                                                                       |
| **</soap:Envelope>**                                                  |
+-----------------------------------------------------------------------+

2. Response Body

+-----------------------------------------------------------------------+
| **<soap:Envelope**                                                    |
|                                                                       |
| **xmlns:soap="http://www.w3.org/2003/05/soap-envelope"**              |
|                                                                       |
| **xmlns:m="http://ente.example/nome-api">>**                          |
|                                                                       |
| **<soap:Header>**                                                     |
|                                                                       |
| **<m:X-Correlation-ID>b8268033-de67-4fa0-bf06-caebbfa5117a</m:X-Corre |
| lation-ID>**                                                          |
|                                                                       |
| **</soap:Header>**                                                    |
|                                                                       |
| **<soap:Body>**                                                       |
|                                                                       |
| **<m:MRequestResponse>**                                              |
|                                                                       |
| **<return>**                                                          |
|                                                                       |
| **<outcome>ACCEPTED</outcome>**                                       |
|                                                                       |
| **</return>**                                                         |
|                                                                       |
| **</m:MRequestResponse>**                                             |
|                                                                       |
| **</soap:Body>**                                                      |
|                                                                       |
| **</soap:Envelope>**                                                  |
+-----------------------------------------------------------------------+

Di seguito un esempio di risposta da parte dell’erogatore verso il
fruitore.

Endpoint

https://api.indirizzoclient.it/soap/nomeinterfacciaclient/v1Method

MRequestResponse

3. Response Body

+-----------------------------------------------------------------------+
| **<soap:Envelope**                                                    |
|                                                                       |
| **xmlns:soap="http://www.w3.org/2003/05/soap-envelope"**              |
|                                                                       |
| **xmlns:m="http://ente.example/nome-api">**                           |
|                                                                       |
| **<soap:Header>**                                                     |
|                                                                       |
| **<m:X-Correlation-ID>b8268033-de67-4fa0-bf06-caebbfa5117a</m:X-Corre |
| lation-ID>**                                                          |
|                                                                       |
| **</soap:Header>**                                                    |
|                                                                       |
| **<soap:Body>**                                                       |
|                                                                       |
| **<m:MRequestResponse>**                                              |
|                                                                       |
| **<return>**                                                          |
|                                                                       |
| **<c>OK</c>**                                                         |
|                                                                       |
| **</return>**                                                         |
|                                                                       |
| **</m:MRequestResponse>**                                             |
|                                                                       |
| **</soap:Body>**                                                      |
|                                                                       |
| **</soap:Envelope>**                                                  |
+-----------------------------------------------------------------------+

4. Response Body

+----------------------------------------------------------+
| **<soap:Envelope**                                       |
|                                                          |
| **xmlns:soap="http://www.w3.org/2003/05/soap-envelope"** |
|                                                          |
| **xmlns:m="http://ente.example/nome-api">**              |
|                                                          |
| **<soap:Body>**                                          |
|                                                          |
| **<m:MRequestResponseResponse>**                         |
|                                                          |
| **<return>**                                             |
|                                                          |
| **<outcome>OK</outcome>**                                |
|                                                          |
| **</return>**                                            |
|                                                          |
| **</m:MRequestResponseResponse>**                        |
|                                                          |
| **</soap:Body>**                                         |
|                                                          |
| **</soap:Envelope>**                                     |
+----------------------------------------------------------+

... mermaid::
     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request(callback endpoint)
      Erogatore-->>Fruitore: 2. CorrelationID
      Erogatore->>Fruitore: 3. Reply(CorrelationID)
      Fruitore-->>Erogatore: 4. Ack
      deactivate Erogatore
       deactivate Fruitore
.. image:: ./media/image2.png

...   :width: 4.68056in
...   :height: 3.125in
