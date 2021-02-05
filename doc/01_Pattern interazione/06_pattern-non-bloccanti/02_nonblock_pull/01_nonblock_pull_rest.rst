[NONBLOCK_PULL_REST] Not Blocking Pull REST
-------------------------------------------

Quando il profilo viene implementato con tecnologia REST,
DEVONO essere rispettate le seguenti regole:

-  La specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   codici di stato HTTP restituiti con relativo schema della risposta,
   oltre che ad eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare gli schemi delle
   richieste insieme ad eventuali header HTTP richiesti;

-  Al passo (1), il fruitore DEVE utilizzare il verbo HTTP POST;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta, un URL per interrogare lo stato di
   processamento utilizzando :httpheader:`Location`, il codice HTTP di
   stato DEVE essere :httpstatus:`202` a meno che non si
   verifichino errori;

-  Al passo (3), il fruitore DEVE utilizzare il percorso di cui al passo
   (2) per richiedere lo stato della risorsa; il verbo HTTP utilizzato
   deve essere GET;

-  Al passo (4) l’erogatore indica, sulla base dello stato del
   processamento, che l'operazione:
   * 4a. non è completata (:httpstatus:`200`)
   * 4b. che la risorsa finale è pronta (:httpstatus:`303`) all’URL indicato nell’ :httpheader:`Location`;

-  Al passo (5), il fruitore DEVE recuperare la risorsa con una richiesta :httpmethod:`GET`
   all'URL indicato in (4b.);

-  Al passo (6) l’erogatore risponde con la rappresentazione della
   risorsa, il codice HTTP restituito è :httpstatus:`200`.

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Al termine del processamento delle richieste, l’erogatore deve fare uso
dei codici di stato HTTP rispettando la semantica. In particolare, al
ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica e semantica dei dati in
   ingresso

-  DEVE, in caso di dati errati, restituire :httpstatus:`400`
   fornendo nel body di risposta dettagli circa l’errore;

-  DOVREBBE, in caso di representation semanticamente non corretta,
   ritornare :httpstatus:`422`;

-  DEVE, se qualcuno degli ID nel path o nel body non esiste, restituire
   :httpstatus:`404`, indicando nel body di risposta quale degli
   ID è mancante;

-  PUÒ, se ipotizza che la richiesta sia malevola, ritornare HTTP status
   400 Bad Request o :httpstatus:`404`;

-  DEVE, in caso di errori non dipendenti dalla richiesta, restituire
   HTTP status 5xx rispettando la semantica degli stessi;

-  DEVE, ricevuta la richiesta, restituire :httpstatus:`202`.

-  In caso di ricezione corretta della risposta, il fruitore DEVE
   restituire :httpstatus:`200`, riempiendo il body di risposta con il
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

Il fruitore richiede la risorsa **M**,
e l’erogatore risponde dichiarando di aver preso in carico la richiesta.

Endpoint https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request:

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Host: api.ente.example
   Content-Type: application/json

   {
     "a": {
        "a1": [1, "…", 2],
        "a2": "Stringa di esempio"
     },
     "b": "Stringa di esempio"
   }


2. Response

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 202 Accepted
   Content-Type: application/json
   Location: /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

   {
     "status": "accepted",
     "message": "Preso carico della richiesta",
     "id": "8131edc0-29ed-4d6e-ba43-cce978c7ea8d"
   }

Quindi il fruitore verifica lo stato dell’esecuzione di **M** (3).
L’erogatore ritorna un payload diverso a seconda dei casi:
- processamento ancora in atto (4a)
- e di processamento avvenuto (4b).

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

3. Request

.. code-block:: http

   GET /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d HTTP/1.1
   Host: api.ente.example


4a. Response (:httpstatus:`200`)

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 200 OK
   Host: api.ente.example
   Content-Type: application/json

   {
     "status": "processing",
     "message": "Richiesta in fase di processamento"
   }

4b. Response (:httpstatus:`303`)

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 303 See Other
   Content-Type: application/json
   Location: /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result

   {
     "status": "done",
     "message": "Processamento completo"
   }

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result

5. Request:

.. code-block:: http

   GET /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result HTTP/1.1
   Host: api.ente.example


6. Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Host: api.ente.example
   Content-Type: application/json

   {"c": "OK"}

.. forum_italia::
   :topic_id: 21459
   :scope: document
