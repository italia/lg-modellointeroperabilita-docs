[NONBLOCK_PULL_SOAP] Not Blocking Pull SOAP
-------------------------------------------

Nel caso in cui il profilo venga implementato con tecnologia SOAP,
DEVONO essere rispettate le seguenti regole:

-  L’interfaccia di servizio dell’erogatore fornisce tre metodi
   differenti al fine di inoltrare una richiesta, controllare lo stato
   ed ottenerne il risultato;

-  La specifica dell’interfaccia dell’erogatore DEVE indicare l’header
   SOAP :code:`X-Correlation-ID`;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, un CorrelationID riportato nel header
   custom SOAP :code:`X-Correlation-ID`;

-  Al passo (3), il fruitore DEVE utilizzare il CorrelationID ottenuto
   al passo (2) per richiedere lo stato di processamento di una
   specifica richiesta;

-  Al passo (4) l’erogatore, quando il processamento non si è ancora
   concluso fornisce informazioni circa lo stato della lavorazione della
   richiesta, quando invece il processamento si è concluso risponde
   indicando in maniera esplicita il completamento;

-  Al passo (5), il fruitore utilizza il CorrelationID di cui al passo
   (2) al fine di richiedere il risultato della richiesta;

-  Al passo (6), l’erogatore fornisce il risultato del processamento.

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire :httpstatus:`500`
   fornendo dettagli circa l’errore utilizzando il meccanismo della SOAP
   fault;

-  Se l’erogatore ipotizza che la richiesta sia malevola PUÒ ritornare
   :httpstatus:`400` o :httpstatus:`404`;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice :httpstatus:`500` indicando il motivo dell’errore nella SOAP
   fault;

-  In caso di successo restituire :httpstatus:`200`, riempiendo il body
   di risposta con il risultato dell’operazione.

Esempio
^^^^^^^

Specifica Servizio Erogatore

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: NONBLOCK_PUSH_PULL_example_wsdl.xml
   :language: xml

Di seguito un esempio di chiamata ad **M** in cui l’erogatore risponde
di avere preso in carico la richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method MRequest

1. Request Body

.. literalinclude:: NONBLOCK_PUSH_PULL_example_request.xml
   :language: xml


2. Response Body (HTTP status code 200 OK)

.. literalinclude:: NONBLOCK_PUSH_PULL_example_response_accepted.xml
   :language: xml

Di seguito un esempio di chiamata con cui il fruitore verifica
l’esecuzione di M nei casi di processamento ancora in atto e di
processamento avvenuto.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method MProcessingStatus

3. Request Body status


.. literalinclude:: NONBLOCK_PUSH_PULL_example_request_status.xml
   :language: xml

4. Response Body (HTTP status code 200 OK) status in attesa


.. literalinclude:: NONBLOCK_PUSH_PULL_example_response_status_processing.xml
   :language: xml


4. Response Body (HTTP status code 200 OK) status completata


.. literalinclude:: NONBLOCK_PUSH_PULL_example_response_status_done.xml
   :language: xml

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1


Method MResponse

5. Request Body result

.. literalinclude:: NONBLOCK_PUSH_PULL_example_request_result.xml
   :language: xml

6. Response Body (HTTP status code 200 OK) result

.. literalinclude:: NONBLOCK_PUSH_PULL_example_response_result.xml
   :language: xml

.. forum_italia::
   :topic_id: 21460
   :scope: document
