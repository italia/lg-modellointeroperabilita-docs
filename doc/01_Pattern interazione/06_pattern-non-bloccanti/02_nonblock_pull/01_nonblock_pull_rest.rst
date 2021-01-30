[NONBLOCK_PULL_REST] Not Blocking Pull REST
-------------------------------------------

Nel caso in cui il profilo venga implementato con tecnologia REST,
DEVONO essere rispettate le seguenti regole:

-  La specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   codici di stato HTTP restituiti con relativo schema della risposta,
   oltre che ad eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare gli schemi delle
   richieste insieme ad eventuali header HTTP richiesti;

-  Al passo (1), il fruitore DEVE utilizzare il verbo HTTP POST;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta, un percorso per interrogare lo stato di
   processamento utilizzando HTTP header Location, il codice HTTP di
   stato DEVE essere HTTP status 202 Accepted a meno che non si
   verifichino errori;

-  Al passo (3), il fruitore DEVE utilizzare il percorso di cui al passo
   (2) per richiedere lo stato della risorsa; il verbo HTTP utilizzato
   deve essere GET;

-  Al passo (4) l’erogatore indica, sulla base dello stato del
   processamento, che la risorsa non è ancora pronta (il codice HTTP
   restituito è HTTP status 200 OK) o indica che la risorsa è pronta,
   utilizzando HTTP header Location, per indicare il percorso dove
   recuperare la risorsa (il codice HTTP restituito è HTTP status 303
   See Other);

-  Al passo (5), il fruitore DEVE utilizzare il percorso di cui al passo
   (4) in caso di risorsa pronta per richiedere la risorsa, il verbo
   HTTP utilizzato deve essere GET;

-  Al passo (6) l’erogatore risponde con la rappresentazione della
   risorsa, il codice HTTP restituito è HTTP status 200 OK.

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Al termine del processamento delle richieste, l’erogatore deve fare uso
dei codici di stato HTTP rispettando la semantica. In particolare, al
ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica e semantica dei dati in
   ingresso

-  DEVE, in caso di dati errati, restituire HTTP status 400 Bad Request
   fornendo nel body di risposta dettagli circa l’errore;

-  DOVREBBE, in caso di representation semanticamente non corretta,
   ritornare HTTP status 422 Unprocessable Entity;

-  DEVE, se qualcuno degli ID nel path o nel body non esiste, restituire
   HTTP status 404 Not Found, indicando nel body di risposta quale degli
   ID è mancante;

-  PUÒ, se ipotizza che la richiesta sia malevola, ritornare HTTP status
   400 Bad Request o HTTP status 404 Not Found;

-  DEVE, in caso di errori non dipendenti dalla richiesta, restituire
   HTTP status 5XX rispettando la semantica degli stessi;

-  DEVE, ricevuta la richiesta, restituire HTTP status 202 Accepted.

-  In caso di ricezione corretta della risposta, il fruitore DEVE
   restituire HTTP status 200 OK , riempiendo il body di risposta con il
   risultato dell’operazione.

-  In caso di errore al momento di ricezione della risposta da parte del
   fruitore, è possibile definire meccanismi specifici per la
   ritrasmissione della risposta o della richiesta.

NB: I messaggi di errore devono essere utili al client ma NON DEVONO
rivelare dettagli tecnici e/o informazioni riservate.

.. _esempio-4:

Esempio
^^^^^^^

Specifica Servizio Server

https://api.ente.example/rest/nome-api/v1/openapi.yaml

.. literalinclude:: file-d0f6ac6f34fbe9304da62adbeaeb90f398f5ce55818391790b6141dea87bd75a.yaml
   :language: yaml

Di seguito un esempio di chiamata ad **M** in cui l’erogatore dichiara
di essersi preso carico della richiesta.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request Header & Body

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Content-Type: application/json

   {
   "a": { "a1": [1,…,2], "a2": "Stringa di esempio" },
   "b": "Stringa di esempio"
   }


2. Response Header & Body (HTTP status 202 Accepted)

.. code-block:: http

   HTTP/1.1 202 Accepted
   Content-Type: application/json
   Location: resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d
   
   {
   "status": "accepted",
   "message": "Preso carico della richiesta",
   "id": "8131edc0-29ed-4d6e-ba43-cce978c7ea8d"
   }

Di seguito un esempio di chiamata con cui il fruitore verifica
l’esecuzione di M nei casi di processamento ancora in atto e di
processamento avvenuto (4).

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

4. Response Header & Body (HTTP status 200 Success)

.. code-block:: http

   HTTP/1.1 200 Success
   Content-Type: application/json

   {
   "status": "processing",
   "message": "Richiesta in fase di processamento"
   }

4. Response Header & Body (HTTP status 303 See Other)

.. code-block:: http

   HTTP/1.1 303 See Other
   
   {
   "status": "done",
   "message": "Processamento completo"
   }

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result

6. Response Header & Body (HTTP status 200 Success)

.. code-block:: http

   HTTP/1.1 200 Success
   Content-Type: application/json

   { "c": "OK" }
