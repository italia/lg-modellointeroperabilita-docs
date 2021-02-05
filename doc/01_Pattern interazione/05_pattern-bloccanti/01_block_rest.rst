[BLOCK_REST] Blocking REST
==========================

Nel caso di implementazione tramite tecnologia REST, DEVONO essere
seguite almeno le seguenti indicazioni:

-  La specifica dell’interfaccia DEVE dichiarare tutti i codici di stato
   HTTP previsti dall'interfaccia, con il relativo schema della
   risposta, oltre che ad eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare lo schema della
   richiesta insieme ad eventuali header HTTP richiesti;

-  Al passo (1) il fruitore DEVE utilizzare come verbo HTTP per
   l’esecuzione della chiamata a procedura il verbo :httpmethod:`POST` su
   un URL contenente gli ID interessati ed il nome del metodo;

-  Al passo (2) l'erogatore DEVE utilizzare HTTP status 2xx a meno che
   non si verifichino errori.

Regole di processamento
-----------------------

Al termine del processamento della richiesta, l’erogatore DEVE fare uso
dei codici di stato HTTP rispettando la semantica. In particolare, al
ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica e semantica dei dati in
   ingresso;

-  DEVE, in caso di dati errati, restituire :httpstatus:`400`
   fornendo nel body di risposta dettagli circa l’errore;

-  DOVREBBE, in caso di rappresentazione semanticamente non corretta,
   ritornare :httpstatus:`422`;

-  DOVREBBE, se qualcuno degli ID nel path o nel body non esiste,
   restituire :httpstatus:`404`, indicando nel body di risposta
   quale degli ID è mancante;

-  PUÒ, se ipotizza che la richiesta sia malevola, ritornare HTTP status
   400 Bad Request o :httpstatus:`404`

-  DEVE, in caso di errori non dipendenti dalla richiesta, restituire
   HTTP status 5xx rispettando la semantica degli stessi;

-  DEVE, in caso di successo, restituire HTTP status 2xx inviando il
   risultato dell’operazione nel payload body.

NB: I messaggi di errore devono essere utili al client ma NON DEVONO
rivelare dettagli tecnici e/o informazioni riservate.

Esempio
-------

Specifica Servizio

https://api.ente.example/rest/nome-api/v1/RESTblocking.yaml

.. literalinclude:: RESTblocking.yaml
   :language: yaml



Di seguito un esempio di chiamata al metodo **M**.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request

.. code-block:: http

    POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
    Host: api.ente.example
    Content-Type: application/json

    {
      "a": {
        "a1s": [ 1, 2 ],
        "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
      },
      "b": "Stringa di esempio"
    }


2. Response :httpstatus:`200`

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {"c": "risultato"}

2. Response :httpstatus:`500`

.. code-block:: http

   HTTP/1.1 500 Internal Server Error
   Content-Type: application/problem+json

   {
       "type": "https://apidoc.ente.example/probs/operation-too-long",
       "status": 500,
       "title": "L'operazione è durata troppo.",
       "detail": "Il sistema non e' riuscito a completare in tempo l'operazione prevista."
   }

2. Response :httpstatus:`400`

.. code-block:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/problem+json

   {
       "type": "https://apidoc.ente.example/probs/invalid-a",
       "status": 400,
       "title": "L'attributo \`b\` ha un valore non valido.",
       "detail": "L'attributo \`b\` dev'essere una stringa di lunghezza   inferiore a 32 caratteri."
   }

2. Response  :httpstatus:`404`

.. code-block:: http

   HTTP/1.1 400 Not Found
   Content-Type: application/problem+json

   {
       "status": 404,
       "title": "Risorsa non trovata."
   }

.. forum_italia::
   :topic_id: 21452
   :scope: document
