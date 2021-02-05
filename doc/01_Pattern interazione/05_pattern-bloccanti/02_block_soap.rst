[BLOCK_SOAP] Blocking SOAP
==========================

Se il pattern viene implementato con tecnologia SOAP, a differenza del
caso REST, il metodo invocato non è specificato nell’endpoint chiamato,
poiché viene identificato all’interno del body. Inoltre tutti gli ID
coinvolti DEVONO essere riportati all’interno del body. DEVE essere
rispettata le seguente regola:

-  la specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   metodi esposti con relativi schemi dei messaggi di richiesta e di
   ritorno. Inoltre le interfacce devono specificare eventuali header
   SOAP richiesti.

Regole di processamento
-----------------------

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire :httpstatus:`500`
   fornendo dettagli circa l’errore utilizzando il meccanismo della SOAP
   fault;

-  Se l’erogatore ipotizza che la richiesta sia malevola PUÒ ritornare
   :httpstatus:`400` o :httpstatus:`404`

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice :httpstatus:`500` indicando il motivo
   dell’errore nella SOAP fault;

-  In caso di successo restituire :httpstatus:`200`, riempiendo il body
   di risposta con il risultato dell’operazione.

Esempio
-------

Specifica Servizio

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: BLOCK_SOAP_example_wsdl.xml
   :language: xml

A seguire un esempio di chiamata al metodo **M**.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

.. literalinclude:: BLOCK_SOAP_example_request.xml
   :language: xml

2. Response Body (HTTP status code 200 OK)

.. literalinclude:: BLOCK_SOAP_example_response200.xml
   :language: xml

2. Response Body (HTTP status code 500 Internal Server Error)

.. literalinclude:: BLOCK_SOAP_example_response500.xml
   :language: xml

.. forum_italia::
   :topic_id: 21453
   :scope: document
