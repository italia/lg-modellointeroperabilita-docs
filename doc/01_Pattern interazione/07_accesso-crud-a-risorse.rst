Accesso CRUD a risorse
======================

In un’architettura orientata alle risorse le API vengono utilizzate, più
che per eseguire compiti complessi, per eseguire operazioni di tipo CRUD
- Create, Read, Update, Delete - su risorse del dominio di interesse. Ad
esempio, una prenotazione è una risorsa che può essere creata (quando
viene fissata), letta, modificata ed eliminata.

In questo scenario si assume che le API siano utilizzate per la gestione
da parte del fruitore delle risorse messe a disposizione dall’erogatore.
L’insieme di operazioni CRUD offerte dall’erogatore dipende dalla
natura della risorse e dalla relazione costruita con i fruitori: sono
possibili relazioni in cui l’erogatore rende disponibile ai fruitori la
sola operazione di lettura (Read).

.. mermaid::

    sequenceDiagram
	activate Fruitore
	activate Erogatore
	Fruitore->>Erogatore: 1. Request()
	Erogatore-->>Fruitore: 2. Reply
	deactivate Erogatore
	deactivate Fruitore


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

[CRUD_REST] CRUD REST
---------------------

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

L’approccio RESTful trova la sua applicazione naturale in operazioni
CRUD - Create, Read, Update, Delete su risorse ed a tal fine sfrutta i
metodi standard dell’HTTP per indicare tali operazioni.
In particolare la seguente mappatura viene utilizzata:

.. list-table::
    :header-rows: 1

    * -    CRUD
      -    Metodo HTTP
      -    Esito (stato HTTP) Se applicato a intera collezione (es. :code:`/clienti`)
      -    Esito (stato HTTP) Se applicato a risorsa specifica (es. :code:`/clienti/{id}` )
    * -    Create
      -    POST
      -    :httpstatus:`201`, l’header "Location" nella risposta può contenere un link a /clienti/{id} che indica l’ID creato.
      -    404 (Not Found), 409 (Conflict) se la risorsa è già esistente.
    * -    Read
      -    GET
      -    200 (OK), lista dei clienti. Implementare meccanismi di paginazione, ordinamento e filtraggio per navigare grandi liste.
      -    200 (OK), 404 (Not Found), se l’ID non è stato trovato o è non valido.
    * -    Update: Replace/ Create
      -    PUT
      -    405 (Method Not Allowed), a meno che non si voglia sostituire ogni risorsa nella collezione.
      -    200 (OK) o 204 (No Content). 404 (Not Found), se l’ID non è stato trovato o è non valido. 201 (Created), nel caso di UPSERT.
    * -    Update: Modify
      -    PATCH
      -    405 (Method Not Allowed), a meno che non si voglia applicare una modifica ad ogni risorsa nella collezione.
      -    200 (OK) o 204 (No Content). 404 (Not Found), se l’ID non è stato trovato o è non valido.
    * -    Delete
      -    DELETE
      -    405 (Method Not Allowed), a meno che non si voglia permettere di eliminare l’intera collezione.
      -    200 (OK). 404 (Not Found), se l’ID non è stato trovato o è non valido.

Si noti l’uso distinto di :httpmethod:`PUT` e :httpmethod:`PATCH` per la
sostituzione e l’applicazione di modifiche ad una risorsa
rispettivamente. È possibile utilizzare anche altri :httpmethod:`a` patto
che si rispettino i dettami dell’approccio RESTful.

In alcuni casi l' :httpmethod:`PUT` può essere utilizzato con funzionalità
di UPSERT (Update o Insert). In particolare, questo è necessario nei
casi in cui sia il fruitore a definire gli identificativi del sistema
erogatore.

Per usare il :httpmethod:`PATCH` bisogna usare alcuni accorgimenti, perché
questo metodo non è definito nelle nuove specifiche di HTTP/1.1 del 2014
ma nel precedente :rfc:`5789`.

NON SI DOVREBBE associare un significato di patch a dei media-type che
non lo prevedano (eg. :code:`application/json` o :code:`application/xml`) ma utilizzare
dei media-type adeguati [1]_.

È possibile ad esempio usare :code:`application/merge-patch+json` definito in
:rfc:`7396` facendo attenzione:

-  che :httpmethod:`PATCH` rifiuti richieste con media-type non adeguato
   con :httpstatus:`415`;

-  che il media-type di patching sia compatibile con gli schemi
   utilizzati;

-  di verificare le considerazioni di sicurezza presenti in
   :rfc:`7396#section-5` e :rfc:`5789#section-5`.

Esempio
^^^^^^^

Per illustrare l’approccio RESTful al CRUD, faremo l'esempio di un API per
gestire le prenotazioni di un appuntamento presso un ufficio municipale.
L’erogatore verifica la compatibilità con la disponibilità nello
specifico orario ed accetta o nega la creazione o l’eventuale
variazione. Come da specifica seguente i metodi implementati sono
:httpmethod:`POST` (creazione), :httpmethod:`DELETE` (eliminazione), 
:httpmethod:`PATCH` (modifica) e :httpmethod:`GET` (lettura).

Specifica Servizio Server

https://api.ente.example/rest/appuntamenti/v1/openapi.yaml

.. literalinclude:: ../media/rest-crud.yaml
   :language: yaml


Di seguito un esempio di chiamata per creare una prenotazione.

1. Request

.. code-block:: http

   POST /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni HTTP/1.1
   Host: api.ente.example
   Content-Type: application/json

   {
       "nome_proprio": "Mario",
       "cognome": "Rossi",
       "codice_fiscale": "MRORSS77T05E472I",
       "dettagli": {
           "data": "2018-12-03T14:29:12.137Z",
           "motivazione": "string"
       }
   }

2. Response

.. code-block:: http

   HTTP/1.1 201 Created
   Content-Type: application/json
   Location: https://api.ente.example/rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254

   {
       "id": 12323254,
       "nome_proprio": "Mario",
       "cognome": "Rossi",
       "codice_fiscale": "MRORSS77T05E472I",
       "dettagli": {
           "data": "2018-12-03T14:29:12.137Z",
           "motivazione": "string"
       }
   }

Di seguito, un esempio in cui il fruitore richiede l’estrazione di una
specifica prenotazione. Si noti l’utilizzo dell’URL restituito nell’
:httpheader:`Location` al passo precedente.

1. Request

.. code-block:: http

   GET /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254 HTTP/1.1
   Host: api.ente.example


2. Response

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 12323254,
       "nome_proprio": "Mario",
       "cognome": "Rossi",
       "codice_fiscale": "MRORSS77T05E472I",
       "dettagli": {
           "data": "2018-12-03T14:29:12.137Z",
           "motivazione": "string"
       }
   }

Di seguito una richiesta di modifica dei dettagli di una prenotazione.

1. Request

.. code-block:: http

   PATCH /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254 HTTP/1.1
   Host: api.ente.example
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
   Content-Type: application/json

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
in :rfc:`5789#section-2.2`. La response ritorna il media-type suggerito
dalla specifica tramite :httpheader:`Accept-Patch`

1. Request

.. code-block:: http

    PATCH /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254 HTTP/1.1
    Host: api.ente.example
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

   DELETE /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254 HTTP/1.1
   Host: api.ente.example


2. Response

.. code-block:: http

   HTTP/1.1 200 OK


.. [1]
   Cf. https://www.rfc-editor.org/errata/eid3169

.. forum_italia::
   :topic_id: 21461
   :scope: document
