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
------------------------------------------------------------

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire HTTP status 500 Internal Server Error
   fornendo dettagli circa l’errore utilizzando il meccanismo della SOAP
   fault;

-  Se l’erogatore ipotizza che la richiesta sia malevola PUÒ ritornare
   HTTP status 400 Bad Request o HTTP status 404 Not Found

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice HTTP status 500 Internal Server Error indicando il motivo
   dell’errore nella SOAP fault;

-  In caso di successo restituire HTTP status 200 OK, riempiendo il body
   di risposta con il risultato dell’operazione.

Esempio
------------------------------------------------------------

Specifica Servizio

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: file-474638784088431f8ebe114acc2c79def211df3757d1a83547f73e7716455a3c.xml
   :language: xml

A seguire un esempio di chiamata al metodo **M**.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

.. code-block:: python

   <soap:Envelope
   
   xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
   
   xmlns:m="http://ente.example/nome-api" >
   
   <soap:Header>
   
   *<!--Autenticazione-->*
   
   </soap:Header>
   
   <soap:Body>
   
   <m:MRequest>
   
   <M>
   
   <oId>\ 1234\ </oId>
   
   <a>
   
   <a1s><a1>\ 1\ </a1>...\ <a1>\ 2\ </a1></a1s>
   
   <a2>\ RGFuJ3MgVG9vbHMgYXJlIGNvb2wh\ </a2>
   
   </a>
   
   <b>\ Stringa di esempio\ </b>
   
   </M>
   
   </m:MRequest>
   
   </soap:Body>
   
   </soap:Envelope>

2. Response Body (HTTP status code 200 OK)

.. code-block:: python

   <soap:Envelope
   
   xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
   
   xmlns:m="http://ente.example/nome-api" >
   
   <soap:Body>
   
   <m:MRequestResponse>
   
   <return>
   
   <m:c>\ OK\ </m:c>
   
   </return>
   
   </m:MRequestResponse>
   
   </soap:Body>
   
   </soap:Envelope>

2. Response Body (HTTP status code 500 Internal Server Error)

.. code-block:: python

   <soap:Envelope
   
   xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
   
   xmlns:m="http://ente.example/nome-api" >
   
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
