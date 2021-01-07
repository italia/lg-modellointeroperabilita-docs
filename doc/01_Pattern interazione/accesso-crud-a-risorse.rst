Accesso CRUD a risorse
======================

In un’architettura orientata alle risorse le API vengono utilizzate, più
che per eseguire compiti complessi, per eseguire operazioni di tipo CRUD
- Create, Read, Update, Delete su risorse del dominio di interesse. Ad
esempio, una prenotazione è una risorsa che può essere creata (quando
viene fissata), letta, modificata ed eliminata.

In questo scenario si assume che le API sono utilizzare per la gestione
da parte del fruitore delle risorse messe a disposizione dell’erogatore.
L’insieme di operazione CRUD garantire dall’erogatore dipende dalla
natura della risorse e dalla relazione costruita con i fruitori, sono
possibili relazione in cui l’erogatore rende disponibile ai fruitori la
solo operazione di lettura (Read).

|{"theme":"default","source":"sequenceDiagram\n\n activate Fruitore\n
\\n activate Erogatore\n Fruitore->>Erogatore: 1. Request()\n
Erogatore-->>Fruitore: 2. Reply\n deactivate Erogatore\n \\n deactivate
Fruitore"}|

*Figura 5 - Interazione CRUD*

Il sequence diagram è, come si nota in figura, equivalente a quello di
una RPC bloccante. In questo caso la richiesta DEVE contenere:

-  Una operazione da effettuare sulla risorsa da scegliere tra Create,
   Read, Update e Delete;

-  Un percorso che indica un identificativo di risorsa (es. una
   specifica prenotazione) oppure di una collezione di risorse (es. un
   insieme di prenotazioni);

-  Nel caso di una operazione di Create o Update, un pacchetto dati
   indicante come inizializzare o modificare (anche parzialmente) la
   risorsa in questione.

Per quanto sia possibile sviluppare funzionalità CRUD anche sviluppando
una interfaccia di servizio SOAP, il ModI prevede lo sviluppo di una
interfaccia REST.

13. .. rubric:: [CRUD_REST] CRUD REST
       :name: crud_rest-crud-rest

    9. .. rubric:: Regole di processamento
          :name: regole-di-processamento-6

L’approccio RESTful trova la sua applicazione naturale in operazioni
CRUD - Create, Read, Update, Delete su risorse ed a tal fine sfrutta i
verbi standard dell’HTTP per indicare tali operazioni. In particolare la
seguente mappatura viene utilizzata:

+-----------------+-----------------+-----------------+-----------------+
| **CRUD**        | **Verbo HTTP**  | **Esito (stato  | **Esito (stato  |
|                 |                 | HTTP) Se        | HTTP) Se        |
|                 |                 | applicato a     | applicato a     |
|                 |                 | intera          | risorsa         |
|                 |                 | collezione (es. | specifica (es.  |
|                 |                 | /clienti)**     | /clienti/{id}   |
|                 |                 |                 | )**             |
+-----------------+-----------------+-----------------+-----------------+
| Create          | POST            | 201 (Created),  | 404 (Not        |
|                 |                 | l’header        | Found), 409     |
|                 |                 | "Location"      | (Conflict) se   |
|                 |                 | nella risposta  | la risorsa è    |
|                 |                 | può contenere   | già esistente.  |
|                 |                 | un link a       |                 |
|                 |                 | /clienti/{id}   |                 |
|                 |                 | che indica l’ID |                 |
|                 |                 | creato.         |                 |
+-----------------+-----------------+-----------------+-----------------+
| Read            | GET             | 200 (OK), lista | 200 (OK), 404   |
|                 |                 | dei clienti.    | (Not Found), se |
|                 |                 | Implementare    | l’ID non è      |
|                 |                 | meccanismi di   | stato trovato o |
|                 |                 | paginazione,    | è non valido.   |
|                 |                 | ordinamento e   |                 |
|                 |                 | filtraggio per  |                 |
|                 |                 | navigare grandi |                 |
|                 |                 | liste.          |                 |
+-----------------+-----------------+-----------------+-----------------+
| Update:         | PUT             | 405 (Method Not | 200 (OK) o 204  |
| Replace/ Create |                 | Allowed), a     | (No Content).   |
|                 |                 | meno che non si | 404 (Not        |
|                 |                 | voglia          | Found), se l’ID |
|                 |                 | sostituire ogni | non è stato     |
|                 |                 | risorsa nella   | trovato o è non |
|                 |                 | collezione.     | valido. 201     |
|                 |                 |                 | (Created), nel  |
|                 |                 |                 | caso di UPSERT. |
+-----------------+-----------------+-----------------+-----------------+
| Update: Modify  | PATCH           | 405 (Method Not | 200 (OK) o 204  |
|                 |                 | Allowed), a     | (No Content).   |
|                 |                 | meno che non si | 404 (Not        |
|                 |                 | voglia          | Found), se l’ID |
|                 |                 | applicare una   | non è stato     |
|                 |                 | modifica ad     | trovato o è non |
|                 |                 | ogni risorsa    | valido.         |
|                 |                 | nella           |                 |
|                 |                 | collezione.     |                 |
+-----------------+-----------------+-----------------+-----------------+
| Delete          | DELETE          | 405 (Method Not | 200 (OK). 404   |
|                 |                 | Allowed), a     | (Not Found), se |
|                 |                 | meno che non si | l’ID non è      |
|                 |                 | voglia          | stato trovato o |
|                 |                 | permettere di   | è non valido.   |
|                 |                 | eliminare       |                 |
|                 |                 | l’intera        |                 |
|                 |                 | collezione.     |                 |
+-----------------+-----------------+-----------------+-----------------+

Si noti l’uso distinto di HTTP method PUT e HTTP method PATCH per la
sostituzione e l’applicazione di modifiche ad una risorsa
rispettivamente. E’ possibile utilizzare anche altri HTTP method a patto
che si rispettino i dettami dell’approccio RESTful.

In alcuni casi l' HTTP method PUT può essere utilizzato con funzionalità
di UPSERT (Update o Insert). In particolare, questo è necessario nei
casi in cui sia il fruitore a definire gli identificativi del sistema
erogatore.

Per usare il HTTP method PATCH bisogna usare alcuni accorgimenti, perché
questo metodo non è definito nelle nuove specifiche di HTTP/1.1 del 2014
ma nel precedente RFC 5789.

NON SI DOVREBBE associare un significato di patch a dei media-type che
non lo prevedono (eg. application/json o application/xml) ma utilizzare
dei media-type adeguati [1]_.

E’ possibile ad esempio usare application/merge-patch+json definito in
RFC 7396 facendo attenzione:

-  che HTTP method PATCH rifiuti richieste con media-type non adeguato
   con HTTP status 415 Unsupported Media Type;

-  che il media-type di patching sia compatibile con gli schemi
   utilizzati;

-  di verificare le considerazioni di sicurezza presenti in RFC
   7396#section-5 e RFC 5789#section-5.

   10. .. rubric:: Esempio
          :name: esempio-6

Per illustrare l’approccio RESTful al CRUD, semplificheremo un API per
gestire le prenotazioni di un appuntamento presso un ufficio municipale.
L’erogatore, verifica la compatibilità con la disponibilità nello
specifico orario ed accetta o nega la creazione o l’eventuale
variazione. Come da specifica seguente i metodi implementati sono HTTP
method POST (creazione), HTTP method DELETE (eliminazione), HTTP method
PATCH (modifica) e HTTP method GET (lettura).

Specifica Servizio Server

https://api.ente.example/rest/appuntamenti/v1/openapi.yaml

.. code-block:: python

   openapi: 3.0.1
   
   info:
   
   title: RESTCRUD
   
   version: "1.0"
   
   description: \|-
   
   Questo file descrive semplicemente i metodi di un'API
   
   e non indica tutte le informazioni di metadatazione che
   
   normalmente vanno inserite.
   
   license:
   
   name: Apache 2.0 License
   
   url: http://www.apache.org/licenses/LICENSE-2.0.html
   
   paths:
   
   /municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni:
   
   get:
   
   description: Mostra prenotazioni
   
   operationId: listReservations
   
   parameters:
   
   - $ref: '#/components/parameters/limit'
   
   - $ref: '#/components/parameters/cursor'
   
   - $ref: '#/components/parameters/path_id_municipio'
   
   - $ref: '#/components/parameters/path_id_ufficio'
   
   responses:
   
   '200':
   
   description: Una lista di prenotazioni.
   
   content:
   
   application/json:
   
   schema:
   
   properties:
   
   prenotazioni:
   
   type: array
   
   items:
   
   $ref: '#/components/schemas/Prenotazione'
   
   count:
   
   type: integer
   
   format: int32
   
   next:
   
   type: string
   
   '400':
   
   $ref: '#/components/responses/400BadRequest'
   
   '404':
   
   $ref: '#/components/responses/404NotFound'
   
   default:
   
   $ref: '#/components/responses/default'
   
   post:
   
   description: Aggiungi una prenotazione
   
   operationId: AddReservation_1
   
   parameters:
   
   - $ref: '#/components/parameters/path_id_municipio'
   
   - $ref: '#/components/parameters/path_id_ufficio'
   
   requestBody:
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/Prenotazione'
   
   responses:
   
   '201':
   
   description: Prenotazione Creata.
   
   headers:
   
   Location:
   
   description: ID della prenotazione creata
   
   schema:
   
   type: string
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/Prenotazione'
   
   '400':
   
   $ref: '#/components/responses/400BadRequest'
   
   '404':
   
   $ref: '#/components/responses/404NotFound'
   
   default:
   
   $ref: '#/components/responses/default'
   
   /municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/{id_preno
   tazione}:
   
   get:
   
   description: LeggiPrenotazione
   
   operationId: GetReservation_1
   
   parameters:
   
   - $ref: '#/components/parameters/path_id_municipio'
   
   - $ref: '#/components/parameters/path_id_ufficio'
   
   - name: id_prenotazione
   
   in: path
   
   required: true
   
   schema:
   
   type: integer
   
   format: int32
   
   responses:
   
   '200':
   
   description: Prenotazione estratta correttamente
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/Prenotazione'
   
   '400':
   
   $ref: '#/components/responses/400BadRequest'
   
   '404':
   
   $ref: '#/components/responses/404NotFound'
   
   default:
   
   $ref: '#/components/responses/default'
   
   delete:
   
   description: EliminaPrenotazione
   
   operationId: DeleteReservation
   
   parameters:
   
   - $ref: '#/components/parameters/path_id_municipio'
   
   - $ref: '#/components/parameters/path_id_ufficio'
   
   - name: id_prenotazione
   
   in: path
   
   required: true
   
   schema:
   
   type: integer
   
   format: int32
   
   responses:
   
   '200':
   
   description: Prenotazione eliminata correttamente
   
   '404':
   
   $ref: '#/components/responses/404NotFound'
   
   default:
   
   $ref: '#/components/responses/default'
   
   patch:
   
   description: Modifica Prenotazione
   
   operationId: PatchReservation
   
   parameters:
   
   - $ref: '#/components/parameters/path_id_municipio'
   
   - $ref: '#/components/parameters/path_id_ufficio'
   
   - name: id_prenotazione
   
   in: path
   
   required: true
   
   schema:
   
   type: integer
   
   format: int32
   
   requestBody:
   
   content:
   
   application/merge-patch+json:
   
   schema:
   
   $ref: '#/components/schemas/PatchPrenotazione'
   
   responses:
   
   '200':
   
   description: Prenotazione modificata correttamente
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/Prenotazione'
   
   '400':
   
   $ref: '#/components/responses/400BadRequest'
   
   '404':
   
   $ref: '#/components/responses/404NotFound'
   
   default:
   
   $ref: '#/components/responses/default'
   
   components:
   
   parameters:
   
   path_id_municipio:
   
   name: id_municipio
   
   in: path
   
   required: true
   
   schema:
   
   type: integer
   
   format: int32
   
   path_id_ufficio:
   
   name: id_ufficio
   
   in: path
   
   required: true
   
   schema:
   
   type: integer
   
   format: int32
   
   limit:
   
   description: How many items to return at one time (max 100)
   
   in: query
   
   name: limit
   
   schema:
   
   format: int32
   
   type: integer
   
   cursor:
   
   description: An opaque identifier that points to the next item in
   the collection.
   
   example: 01BX9NSMKVXXS5PSP2FATZM123
   
   in: query
   
   name: cursor
   
   schema:
   
   type: string
   
   responses:
   
   400BadRequest:
   
   description: Richiesta non accoglibile
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/ErrorMessage'
   
   404NotFound:
   
   description: Identificativo non trovato
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/ErrorMessage'
   
   default:
   
   description: \|-
   
   Errore inatteso. Questo viene ritornato nel caso ci sia
   
   un errore inatteso. Non vanno mai esposti i dati interni
   
   del server.
   
   content:
   
   application/json:
   
   schema:
   
   $ref: '#/components/schemas/ErrorMessage'
   
   schemas:
   
   TaxCode:
   
   description: Il codice fiscale.
   
   example: RSSMRA75L01H501A
   
   externalDocs:
   
   url: https://w3id.org/italia/onto/CPV/taxCode
   
   pattern:
   /^(?:(?:[B-DF-HJ-NP-TV-Z]|[AEIOU])[AEIOU][AEIOUX]|[B-DF-HJ-NP-TV-Z]{2
   }[A-Z]){2}[\dLMNP-V]{2}(?:[A-EHLMPR-T](?:[04LQ][1-9MNP-V]|[1256LMRS][
   \dLMNP-V])|[DHPS][37PT][0L]|[ACELMRT][37PT][01LM])(?:[A-MZ][1-9MNP-V]
   [\dLMNP-V]{2}|[A-M][0L](?:[1-9MNP-V][\dLMNP-V]|[0L][1-9MNP-V]))[A-Z]$
   /i
   
   type: string
   
   Prenotazione:
   
   type: object
   
   properties:
   
   nome:
   
   type: string
   
   cognome:
   
   type: string
   
   codice_fiscale:
   
   $ref: '#/components/schemas/TaxCode'
   
   dettagli:
   
   $ref: '#/components/schemas/PatchPrenotazione'
   
   PatchPrenotazione:
   
   type: object
   
   properties:
   
   data:
   
   type: string
   
   format: date-time
   
   motivazione:
   
   type: string
   
   ErrorMessage:
   
   type: object
   
   properties:
   
   detail:
   
   description: \|
   
   A human readable explanation specific to this occurrence of the
   
   problem.
   
   type: string
   
   instance:
   
   description: \|
   
   An absolute URI that identifies the specific occurrence of the
   problem.
   
   It may or may not yield further information if dereferenced.
   
   format: uri
   
   type: string
   
   status:
   
   description: \|
   
   The HTTP status code generated by the origin server for this
   occurrence
   
   of the problem.
   
   exclusiveMaximum: true
   
   format: int32
   
   maximum: 600
   
   minimum: 100
   
   type: integer
   
   title:
   
   description: \|
   
   A short, summary of the problem type. Written in english and readable
   
   for engineers (usually not suited for non technical stakeholders and
   
   not localized); example: Service Unavailable
   
   type: string
   
   type:
   
   default: about:blank
   
   description: \|
   
   An absolute URI that identifies the problem type. When dereferenced,
   
   it SHOULD provide human-readable documentation for the problem type
   
   (e.g., using HTML).
   
   format: uri
   
   type: string

Di seguito un esempio di chiamata per creare una prenotazione.

1. Request

.. code-block:: http

   POST
   /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}
   /prenotazioni
   HTTP/1.1
   
   {
   
   "nome_proprio": "Mario",
   
   "cognome": "Rossi",
   
   "codice_fiscale": "\ MRORSS77T05E472I",
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "string"
   
   }
   
   }

2. Response

.. code-block:: http

   HTTP/1.1 201 Created
   
   Location:
   https://api.ente.example/rest/appuntamenti/v1/municipio/{id_municipio
   }/ufficio/{id_ufficio}/prenotazioni/12323254
   
   {
   
   "id": 12323254,
   
   "nome_proprio": "Mario",
   
   "cognome": "Rossi",
   
   "codice_fiscale": "\ MRORSS77T05E472I",
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "string"
   
   }
   
   }

Di seguito un esempio in cui il fruitore richiede l’estrazione di una
specifica prenotazione. Si noti l’utilizzo dell’URL restituito nell"
HTTP header Location al passo precedente.

1. Request

.. code-block:: http

   GET
   /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}
   /prenotazioni/12323254
   HTTP/1.1

2. Response

.. code-block:: http

   HTTP/1.1 200 OK
   
   {
   
   "id": 12323254,
   
   "nome_proprio": "Mario",
   
   "cognome": "Rossi",
   
   "codice_fiscale": "\ MRORSS77T05E472I",
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "string"
   
   }
   
   }

Di seguito una richiesta di modifica dei dettagli di una prenotazione.

1. Request

.. code-block:: http

   PATCH
   /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}
   /prenotazioni/12323254
   HTTP/1.1
   
   Content-Type: application/merge-patch+json
   
   {
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "nuova motivazione"
   
   }
   
   }

2. Response

.. code-block:: http

   HTTP/1.1 200 OK
   
   {
   
   "nome_proprio": "Mario",
   
   "cognome": "Rossi",
   
   "codice_fiscale": "MRORSS77T05E472I",
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "nuova motivazione"
   
   }
   
   }

Di seguito una richiesta di modifica dei dettagli di una prenotazione
con media-type application/json, che non avendo una semantica di
patching definita, dev’essere rifiutato seguendo le indicazioni presenti
in RFC 5789#section-2.2. La response ritorna il media-type suggerito
dalla specifica tramite HTTP header Accept-Patch

1. Request

.. code-block:: http

   PATCH
   /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}
   /prenotazioni/12323254
   HTTP/1.1
   
   Content-Type: application/json
   
   {
   
   "dettagli": {
   
   "data": "2018-12-03T14:29:12.137Z",
   
   "motivazione": "nuova motivazione"
   
   }
   
   }

2. Response

.. code-block:: http

   HTTP/1.1 415 Unsupported Media Type
   
   Accept-Patch: application/merge-patch+json

Di seguito un esempio di cancellazione di una specifica prenotazione.

1. Request

.. code-block:: http

   DELETE
   /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}
   /prenotazioni/12323254
   HTTP/1.1

2. Response

.. code-block:: http

   HTTP/1.1 200 OK

.. [1]
   Cf. https://www.rfc-editor.org/errata/eid3169

.. mermaid::
     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Reply
      deactivate Erogatore
       deactivate Fruitore image:: ./media/image5.png
   :width: 4.68056in
   :height: 2.40278in
