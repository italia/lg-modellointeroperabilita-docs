Accesso CRUD a Risorse
===========================

.. _scenario-3:

Scenario
---------------

In molti casi, le interfacce di servizio vengono utilizzate più che per
eseguire compiti complessi, al fine di eseguire operazioni di tipo CRUD
- Create, Read, Update, Delete su risorse del dominio di interesse. Ad
esempio, una prenotazione è una risorsa che può essere creata (quando
viene fissata), letta, modificata ed eliminata. Questo genere di
operazione ha durata molto breve, e quindi deve essere implementata
mediante una modalità bloccante come quella vista in Sezione 3.2.2.

.. _descrizione-3:

Descrizione
------------------

.. mermaid::
   :caption: Interazione bloccante CRUD
   :alt: interazione bloccante CRUD

    sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

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
una interfaccia di servizio SOAP, il ModI consiglia nei casi in cui
occorra un approccio a risorse, su cui è naturale utilizzare operazioni
CRUD, di sviluppare una interfaccia RESTful.

.. _interfaccia-rest-3:

Interfaccia REST
-----------------------

.. _regole-di-processamento-6:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L'approccio RESTful trova la sua applicazione naturale in operazioni
CRUD - Create, Read, Update, Delete su risorse ed a tal fine sfrutta i
verbi standard dell'HTTP per indicare tali operazioni. In particolare la
seguente mappatura viene utilizzata:

+-----------------+-----------------+-----------------+-----------------+
| **CRUD**        | **Verbo HTTP**  | **Esito (stato  | **Esito (stato  |
|                 |                 | HTTP) Se        | HTTP) Se        |
|                 |                 | applicato a     | applicato a     |
|                 |                 | intera          | risorsa         |
|                 |                 | collezione (es. | specifica (es.  |
|                 |                 | /clienti)**     | /clienti/{id})**|
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Create          | POST            | 201 (Created),  | 404 (Not        |
|                 |                 | l'header        | Found), 409     |
|                 |                 | 'Location'      | (Conflict) se   |
|                 |                 | nella risposta  | la risorsa è    |
|                 |                 | può contenere   | già esistente.  |
|                 |                 | un link a       |                 |
|                 |                 | /clienti/{id}   |                 |
|                 |                 | che indica l'ID |                 |
|                 |                 | creato.         |                 |
+-----------------+-----------------+-----------------+-----------------+
| Read            | GET             | 200 (OK), lista | 200 (OK), 404   |
|                 |                 | dei clienti.    | (Not Found), se |
|                 |                 | Implementare    | l'ID non è      |
|                 |                 | meccanismi di   | stato trovato o |
|                 |                 | paginazione,    | è non valido.   |
|                 |                 | ordinamento e   |                 |
|                 |                 | filtraggio per  |                 |
|                 |                 | navigare grandi |                 |
|                 |                 | liste.          |                 |
+-----------------+-----------------+-----------------+-----------------+
| Update/Replace/ | PUT             | 405 (Method Not | 200 (OK) o 204  |
| Create          |                 | Allowed), a     | (No Content).   |
|                 |                 | meno che non si | 404 (Not        |
|                 |                 | voglia          | Found), se l'ID |
|                 |                 | sostituire ogni | non è stato     |
|                 |                 | risorsa nella   | trovato o è non |
|                 |                 | collezione.     | valido. 201     |
|                 |                 |                 | (Created), nel  |
|                 |                 |                 | caso di UPSERT. |
+-----------------+-----------------+-----------------+-----------------+
| Update/Modify   | PATCH           | 405 (Method Not | 200 (OK) o 204  |
|                 |                 | Allowed), a     | (No Content).   |
|                 |                 | meno che non si | 404 (Not        |
|                 |                 | voglia          | Found), se l'ID |
|                 |                 | applicare una   | non è stato     |
|                 |                 | modifica ad     | trovato o è non |
|                 |                 | ogni risorsa    | valido.         |
|                 |                 | nella           |                 |
|                 |                 | collezione.     |                 |
+-----------------+-----------------+-----------------+-----------------+
| Delete          | DELETE          | 405 (Method Not | 200 (OK). 404   |
|                 |                 | Allowed), a     | (Not Found), se |
|                 |                 | meno che non si | l'ID non è      |
|                 |                 | voglia          | stato trovato o |
|                 |                 | permettere di   | è non valido.   |
|                 |                 | eliminare       |                 |
|                 |                 | l'intera        |                 |
|                 |                 | collezione.     |                 |
+-----------------+-----------------+-----------------+-----------------+

Si noti l'uso distinto di :httpmethod:`PUT` e :httpmethod:`PATCH` per la sostituzione
e l'applicazione di modifiche ad una risorsa rispettivamente. E'
possibile utilizzare anche altri verbi HTTP a patto che si rispettino i
dettami dell'approccio RESTful.

In alcuni casi il verbo :httpmethod:`PUT` può essere utilizzato con funzionalità di
UPSERT (Update o Insert). In particolare, questo è necessario nei casi
in cui sia il fruitore a definire gli identificativi del sistema
erogatore.

Per usare il :httpmethod:`PATCH` bisogna usare alcuni accorgimenti, perché
questo metodo non è definito nelle nuove specifiche di HTTP/1.1 del 2014
ma nel precedente :rfc:`5789`.

Come indicato in questa considerazione https://www.rfc-editor.org/errata/eid3169
**NON SI DOVREBBE** associare un significato di patch a dei media-type che
non lo prevedono (eg. ``application/json`` o ``application/xml``) ma utilizzare
dei media-type adeguati.

E' possibile ad esempio usare ``application/merge-patch+json`` definito
in :rfc:`7386` facendo attenzione:

  - che :httpmethod:`PATCH` rifiuti richieste con media-type non adeguato con :httpstatus:`415`;
  - che il media-type di patching sia compatibile con gli schemi utilizzati;
  - di verificare le considerazioni di sicurezza presenti in :rfc:`7396#section-5`
    e :rfc:`5789#section-5`.

.. _esempio-6:

Esempio
~~~~~~~~~~~~~~~~

Per illustrare l'approccio RESTful al CRUD, esemplificheremo
un API per gestire le prenotazioni di un
appuntamento presso un ufficio municipale. L'erogatore, verifica la
compatibilità con la disponibilità nello specifico orario ed accetta o
nega la creazione o l'eventuale variazione. Come da
specifica seguente i metodi implementati sono :httpmethod:`POST` (creazione), :httpmethod:`DELETE`
(eliminazione), :httpmethod:`PATCH` (modifica) e :httpmethod:`GET` (lettura).


 Specifica Servizio Server  https://api.amministrazioneesempio.it/rest/appuntamenti/v1/openapi.yaml

 .. literalinclude:: ../media/rest-crud.yaml
    :language: yaml


Di seguito un esempio di chiamata per creare una prenotazione.

.. code-block:: http
   :caption: Request

   POST /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni HTTP/1.1

   {
     "nome_proprio": "Mario",
     "cognome": "Rossi",
     "codice_fiscale": "MRORSS77T05E472I",
     "dettagli": {
       "data": "2018-12-03T14:29:12.137Z",
       "motivazione": "string"
     }
   }


.. code-block:: http
   :caption: Response

   HTTP/1.1 201 Created
   Location: https://api.amministrazioneesempio.it/rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254

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


Di seguito un esempio in cui il fruitore richiede l'estrazione di una
specifica prenotazione. Si noti l'utilizzo dell'URL restituito
nell\' :httpheader:`Location` al passo precedente.

.. code-block:: http
   :caption: Request

   GET /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254  HTTP/1.1


.. code-block:: http
   :caption: Response

   HTTP/1.1 200 OK

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


.. code-block:: http
   :caption: Request


   PATCH /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254  HTTP/1.1
   Content-Type: application/merge-patch+json

   {
      "dettagli": {
        "data": "2018-12-03T14:29:12.137Z",
        "motivazione": "nuova motivazione"
      }
   }


.. code-block:: http
   :caption: Response

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
con media-type ``application/json``, che non avendo una semantica
di patching definita, dev'essere rifiutato seguendo le indicazioni
presenti in :rfc:`5789#section-2.2`. La response ritorna
il media-type suggerito dalla specifica tramite :httpheader:`Accept-Patch`


.. code-block:: http
   :caption: Request


   PATCH /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254  HTTP/1.1
   Content-Type: application/json

   {
      "dettagli": {
        "data": "2018-12-03T14:29:12.137Z",
        "motivazione": "nuova motivazione"
      }
   }

.. code-block:: http
   :caption: Response

   HTTP/1.1 415 Unsupported Media Type
   Accept-Patch: application/merge-patch+json


Di seguito un esempio di cancellazione di una specifica prenotazione.


.. code-block:: http
   :caption: Request

   DELETE /rest/appuntamenti/v1/municipio/{id_municipio}/ufficio/{id_ufficio}/prenotazioni/12323254  HTTP/1.1


.. code-block:: http
   :caption: Response

   HTTP/1.1 200 OK
