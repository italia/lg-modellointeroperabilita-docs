Robustezza
==========

Ai fini di garantire la responsività di una interfaccia di servizio, è
necessario impedire a singoli fruitori di esaurire la capacità di
calcolo dell’erogatore. La tecnica comunemente utilizzata in questi casi
è il rate limiting (anche noto come throttling). Il rate limit fornisce
ad uno specifico fruitore un numero massimo di richieste soddisfacibili
all’interno di uno specifico arco temporale (es. 1000 richieste al
minuto). Un numero di richieste che superi il limite imposto provoca il
rifiuto di ulteriori richieste da parte di uno specifico fruitore per un
intervallo di tempo. Sulle politiche riguardanti il numero massimo di
richieste e la relativa finestra temporale, e quelle riguardanti il
tempo di attesa per nuove richieste (che può essere incrementato in caso
di richieste reiterate, es. con una politica di aumento esponenziale) si
lascia libertà agli implementatori previa un’analisi di carico massimo
sopportabile dall’erogatore.

Gli erogatori di interfacce di servizio REST DEVONO segnalare eventuali
limiti raggiunti con **HTTP 429 (too many requests)**.

Le API restituiscono in ogni response i valori globali di throttling
tramite i seguenti header:

-  X-RateLimit-Limit: limite massimo di richieste per un endpoint

-  X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo
   reset

-  X-RateLimit-Reset: il numero di secondi che mancano al prossimo reset

In caso di superamento delle quote, le API restituiscono anche l'header:

-  Retry-After: il numero minimo di secondi dopo cui il client è
   invitato a riprovare [1]_

Nel caso di interfacce di servizio SOAP non esistono regole guida
standard per la gestione del rate limit e del throttling. Si suggerisce
l’utilizzo degli stessi header e status code HTTP visti nel caso REST.

Si propone di seguito una specifica di servizio REST relativa ad un
profilo RPC bloccante arricchito con gli header relativi al rate
limiting. L’utilizzo degli header HTTP in SOAP è fuori dagli obiettivi
di WSDL come Interface Definition Language.

+--------------------+------------------------------------------------------------------------------------+
| Specifica Servizio | https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/openapi.yaml |
+--------------------+------------------------------------------------------------------------------------+
| .. code-block:: YAML                                                                                    |
|                                                                                                         |
|    openapi: 3.0.1                                                                                       |
|    info:                                                                                                |
|      title: RESTrobustezza                                                                              |
|      license:                                                                                           |
|        name: Apache 2.0 License                                                                         |
|        url: http://www.apache.org/licenses/LICENSE-2.0.html                                             |
|      version: "1.0"                                                                                     |
|    paths:                                                                                               |
|      /resources/{id_resource}/M:                                                                        |
|        post:                                                                                            |
|          description: M                                                                                 |
|          operationId: PushMessage_1                                                                     |
|          parameters:                                                                                    |
|          - name: id_resource                                                                            |
|            in: path                                                                                     |
|            required: true                                                                               |
|            schema:                                                                                      |
|              type: integer                                                                              |
|              format: int32                                                                              |
|          requestBody:                                                                                   |
|            content:                                                                                     |
|              application/json:                                                                          |
|                schema:                                                                                  |
|                  $ref: '#/components/schemas/MType'                                                     |
|          responses:                                                                                     |
|            500:                                                                                         |
|              description: Errore interno avvenuto                                                       |
|              content:                                                                                   |
|                application/json:                                                                        |
|                  schema:                                                                                |
|                    $ref: '#/components/schemas/ErrorMessage'                                            |
|            404:                                                                                         |
|              description: Identificativo non trovato                                                    |
|              headers:                                                                                   |
|                X-RateLimit-Remaining:                                                                   |
|                  description: Chiamate rimanenti                                                        |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Reset:                                                                       |
|                  description: Secondi dal reset del limite                                              |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Limit:                                                                       |
|                  description: Limite massimo richieste                                                  |
|                  schema:                                                                                |
|                    type: string                                                                         |
|              content:                                                                                   |
|                application/json:                                                                        |
|                  schema:                                                                                |
|                    $ref: '#/components/schemas/ErrorMessage'                                            |
|            200:                                                                                         |
|              description: Esecuzione di M avvenuta con successo                                         |
|              headers:                                                                                   |
|                X-RateLimit-Remaining:                                                                   |
|                  description: Chiamate rimanenti                                                        |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Reset:                                                                       |
|                  description: Secondi dal reset del limite                                              |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Limit:                                                                       |
|                  description: Limite massimo richieste                                                  |
|                  schema:                                                                                |
|                    type: string                                                                         |
|              content:                                                                                   |
|                application/json:                                                                        |
|                  schema:                                                                                |
|                    $ref: '#/components/schemas/MResponseType'                                           |
|            400:                                                                                         |
|              description: Richiesta malformata                                                          |
|              headers:                                                                                   |
|                X-RateLimit-Remaining:                                                                   |
|                  description: Chiamate rimanenti                                                        |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Reset:                                                                       |
|                  description: Secondi dal reset del limite                                              |
|                  schema:                                                                                |
|                    type: string                                                                         |
|                X-RateLimit-Limit:                                                                       |
|                  description: Limite massimo richieste                                                  |
|                  schema:                                                                                |
|                    type: string                                                                         |
|              content:                                                                                   |
|                application/json:                                                                        |
|                  schema:                                                                                |
|                    $ref: '#/components/schemas/ErrorMessage'                                            |
|            429:                                                                                         |
|              description: Limite di richieste raggiunto                                                 |
|              headers:                                                                                   |
|                Retry-After:                                                                             |
|                  description: Limite massimo richieste                                                  |
|                  schema:                                                                                |
|                    type: string                                                                         |
|              content:                                                                                   |
|                application/json:                                                                        |
|                  schema:                                                                                |
|                    $ref: '#/components/schemas/ErrorMessage'                                            |
|    components:                                                                                          |
|      schemas:                                                                                           |
|        MType:                                                                                           |
|          type: object                                                                                   |
|          properties:                                                                                    |
|            a:                                                                                           |
|              $ref: '#/components/schemas/AComplexType'                                                  |
|            b:                                                                                           |
|              type: string                                                                               |
|        MResponseType:                                                                                   |
|          type: object                                                                                   |
|          properties:                                                                                    |
|            c:                                                                                           |
|              type: string                                                                               |
|        AComplexType:                                                                                    |
|          type: object                                                                                   |
|          properties:                                                                                    |
|            a1s:                                                                                         |
|              type: array                                                                                |
|              items:                                                                                     |
|                type: integer                                                                            |
|                format: int32                                                                            |
|            a2:                                                                                          |
|              type: string                                                                               |
|        ErrorMessage:                                                                                    |
|          type: object                                                                                   |
|          properties:                                                                                    |
|            error_message:                                                                               |
|              type: string                                                                               |
+---------------------------------------------------------------------------------------------------------+

Di seguito un esempio di chiamata al servizio bloccante con risposta nel
caso in cui i limiti non siano ancora stati raggiunti e nel caso in cui
invece il fruitore debba attendere per presentare nuove richieste.

+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| HTTP Operation                                             | POST                                                                                   |
+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Endpoint                                                   | https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M |
+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| \(1) Request Body                                          | .. code-block:: JSON                                                                   |
|                                                            |                                                                                        |
|                                                            |    {                                                                                   |
|                                                            |      "a": {                                                                            |
|                                                            |        "a1s": [1,2],                                                                   |
|                                                            |        "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"                                            |
|                                                            |      },                                                                                |
|                                                            |      "b": "Stringa di esempio"                                                         |
|                                                            |    }                                                                                   |
+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| \(2) Response Body (HTTP Status Code 200 OK)               | .. code-block:: JSON                                                                   |
|                                                            |                                                                                        |
|                                                            |    X-Rate-Limit-Limit: 30                                                              |
|                                                            |    X-Rate-Limit-Remaining: 11                                                          |
|                                                            |    X-Rate-Limit-Reset: 44                                                              |
|                                                            |                                                                                        |
|                                                            |    {                                                                                   |
|                                                            |      "c" : "risultato"                                                                 |
|                                                            |    }                                                                                   |
+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| \(2) Response Body (HTTP Status Code 429 Too Many Request) | .. code-block:: JSON                                                                   |
|                                                            |                                                                                        |
|                                                            |    Retry-After: 60                                                                     |
|                                                            |                                                                                        |
|                                                            |    {                                                                                   |
|                                                            |      "error_message" : "messaggio di errore"                                           |
|                                                            |    }                                                                                   |
+------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. [1]
   RFC 7231 prevede che l’header Retry-After possa essere utilizzato sia
   in forma di data che di secondi
