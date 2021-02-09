Raccomandazioni su progettazione e naming
--------------------------------------------

In assenza di specifiche regole per l’API Naming (es. HL7, INSPIRE, ..)
DOVREBBERO essere adottate le seguenti regole.

[RAC_REST_NAME_001] Uso corretto dei metodi HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metodi HTTP DEVONO essere utilizzati rispettando la semantica indicata
in :rfc:`7231#section-4.3`.

[RAC_REST_NAME_002] Usare parole separate da trattino «-» per i path (kebab-case)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nella definizione dei path si DEVE utilizzare il separatore «-»
(kebab-case).

Esempio: :code:`/​tax-code​/{tax_code_id}`

Il path DOVREBBE essere semplice, intuitivo e coerente.

[RAC_REST_NAME_003] Preferire Hyphenated-Pascal-Case per gli header HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DOVREBBE preferirsi Hyphenated-Pascal-Case per gli header HTTP.

Esempio:

.. code-block:: python

   Accept-Encoding
   Apply-To-Redirect-Ref
   Disposition-Notification-Options
   Message-ID

[RAC_REST_NAME_004] Le collezioni di risorse possono usare nomi al plurale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si consiglia di differenziare il nome delle collezioni e delle risorse.
Questo permette di separare a livello di URI, endpoint che sono in larga
parte funzionalmente differenti.

Esempio 1: ricerca di documenti per data in una collezione

Request:

.. code-block:: http

   GET /​documenti​?data=2018-05-01 HTTP/1.1
   Host: api.example
   Accept: application/json


Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
     "items": [ ".." ],
     "limit": 10,
     "next_cursor": 21314123
   }

Esempio 2: recupera un singolo documento

Request:

.. code-block:: http

   GET /​documento​/21314123 HTTP/1.1
   Host: api.example
   Accept: application/json

Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
     "id": 21314123,
     "title": "Atto di nascita ..."
   }

[RAC_REST_NAME_005] Utilizzare Query String standardizzate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esempio 1: La paginazione DEVE essere implementata tramite i parametri:

.. code-block:: python

   cursor, limit, offset, sort

Esempio 2: La ricerca, il filtering e l’embedding dei parametri DEVE
essere implementata tramite i parametri:

.. code-block:: python

   q, fields, embed

[RAC_REST_NAME_006] Non usare l’header Link se la response è in JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eventuali link a risorse utili al flusso applicativo DEVONO essere
restituiti nel payload e non nell’ :httpheader:`Link` definito in :rfc:`8288`.
Questo semplifica l'implementazione dei client. È comunque possibile
usare l':httpheader:`Link` per passare informazioni di tipo diverso.

[RAC_REST_NAME_007] Usare URI assoluti nei risultati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le response DOVREBBERO restituire URI assoluti, al fine di indicare
chiaramente al client l’indirizzo delle risorse di destinazione e non
obbligare i client a fare «inferenza» dal contesto.

[RAC_REST_NAME_008] Usare lo schema Problem JSON per le risposte di errore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In caso di errori si DEVONO ritornare:

-  un payload di tipo Problem definito in :rfc:`7807`

-  il media type application/problem+json

-  uno status code esplicativo

-  l’oggetto, possibilmente esteso

Quando si restituisce un errore è importante non esporre dati interni
delle applicazioni. Per prevenire il rischio di user-enumeration, i
messaggi di errore di autenticazione non devono fornire informazioni
sull’esistenza o meno dell’utenza.

Dopo aver validato il contenuto delle richieste si DEVE ritornare:

-  :httpstatus:`415` se il valore in :httpheader:`Content-Type` non è
   supportato;

-  :httpstatus:`400` o :httpstatus:`404` se si
   ipotizza che la richiesta sia malevola;

-  :httpstatus:`422` se la representation contenuta
   nella richiesta è sintatticamente corretta ma semanticamente non
   processabile.

[RAC_REST_NAME_009] Ottimizzare l’uso della banda e migliorare la responsività
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si DOVREBBERO utilizzare:

-  tecniche di compressione;

-  paginazione;

-  un filtro sugli attributi necessari;

-  le specifiche di optimistic locking (:httpheader:`ETag`,
   if-(none-)match) :rfc:`7232`.

È possibile ridurre l’uso della banda e velocizzare le richieste
filtrando i campi delle risorse restituite.

Esempio 1: Non filtrato

Request:

.. code-block:: http

   GET /resources/123 HTTP/1.1
   Host: api.example

Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {
   
   "id": "cddd5e44-dae0-11e5-8c01-63ed66ab2da5",
   "name": "Mario Rossi",
   "address": "via del Corso, Roma, Lazio, Italia",
   "birthday": "1984-09-13",
   "partner": {
	   "id": "1fb43648-dae1-11e5-aa01-1fbc3abb1cd0",
	   "name": "Maria Rossi",
	   "address": "via del Corso, Roma, Lazio, Italia",
	   "birthday": "1988-04-07"
	   }
   }

Esempio 2: Filtrato

Request:

.. code-block:: http

   GET /resources/123?fields=(name,partner(name)) HTTP/1.1
   Host: api.example


Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {
   "name": "Mario Rossi",
   "partner": {
	   "name": "Maria Rossi"
	   }
   }


Si DOVREBBE effettuare la Resource Expansion per ritornare risorse
correlate tra loro, in modo da ridurre il numero di richieste.

In tal caso va usato:

-  il​ parametro embed utilizzando lo stesso formato dei campi per il
   filtering;

-  l’attributo \_embedded contenente le entry espanse.

Esempio 3: Resource Expansion, utile a ritornare i dati di una persona
associati ad un codice fiscale.

Request:

.. code-block:: http

   GET /tax_code/MRORSS12T05E472W?embed=(person) HTTP/1.1
   Accept: application/json

Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {
     "tax_code":"MRORSS12T05E472W",
     "_embedded": {
	    "person":{
		  "given_name":"Mario",
		  "family_name":"Rossi",
		  "id":"1234-ABCD-7890"
        }
     }
   }

[RAC_REST_NAME_010] Il caching http deve essere disabilitato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il caching DOVREBBE essere disabilitato tramite
:httpheader:`Cache-Control` per evitare che delle richieste vengano inopportunamente
messe in cache. Il mancato rispetto di questa raccomandazione può
portare all'esposizione accidentale di dati personali.

Le API che supportano il caching DEVONO documentare le varie limitazioni
e modalità di utilizzo tramite gli header definiti in :rfc:`7234`:

-  :httpheader:`Cache-Control`
-  :httpheader:`Vary`.

Eventuali conflitti nella creazione di risorse DEVONO essere gestiti
tramite gli header:

-  :httpheader:`ETag`;
-  :httpheader:`If-Match`;
-  :httpheader:`If-None-Match`;

che contengono un identificatore opaco che il server è in grado di associare
univocamente alla versione della risorsa erogata.
Si veda :rfc:`7232#section-2.3` per ulteriori informazioni su come
implementare questi header.

[RAC_REST_NAME_011] Esporre lo stato del servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'API DEVE esporre lo stato del servizio al path \`/status\` e ritornare
un oggetto con media-type application/problem+json (:rfc:`7807`).
Se il servizio funziona correttamente, l'API ritorna :httpstatus:`200`.

Segue un esempio di specifica del path in formato OpenAPI 3.

ESEMPIO: Esposizione stato del servizio

.. literalinclude:: file-470c9c7d9f2d0c6947f8fe7dd6e4410f6fd1c951043908bf504dd15c7d8a2868.yaml
   :language: yaml

.. forum_italia::
   :topic_id: 21494
   :scope: document
