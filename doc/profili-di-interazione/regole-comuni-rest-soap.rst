Raccomandazioni tecniche per REST
=================================

In questa sezione si raccolgono per la tecnologia REST
delle indicazioni al fine di favorire l'interoperabilità.

Formato dei dati
~~~~~~~~~~~~~~~~

Nella tecnologia REST, la comunicazione DOVREBBE avvenire tramite oggetti JSON :RFC:`7159` con il relativo
​\  `media-type​ <https://www.iana.org/assignments/media-types/media-types.xhtml>`__
``application/json``.

E' possibile eccepire in presenza di specifiche in cui gli oggetti di
comunicazione sono formalizzati in forma diversa da JSON (es. INSPIRE, HL7).

.. TODO: non è chiaro il fine del paragrafo, sembra in sovrapposizione con quanto scritto nel paragrafo precedente.

Codificare dati strutturati con oggetti JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I dati in formato JSON :RFC:`7159` strutturati DEVONO essere trasferiti tramite ​oggetti
​, in modo da permettere l'estensione retrocompatibile della
response con ulteriori attributi (Eg. paginazione).

Cioè:

-  il payload di una response contenente una entry ritorna un oggetto

.. code-block:: JSON

    { "given_name": "Paolo", "last_name": "Rossi", "id": 313 }

-  il payload di una response contenente più entry ​ritorna un oggetto
   contenente una lista​ e non direttamente una lista.

.. code-block:: JSON

    {
       "items":[
          {
             "given_name":"Carlo",
             "family_name":"Bianchi",
             "id":314
          },
          {
             "given_name":"Giuseppe",
             "family_name":"Verdi",
             "id":315
          }
       ]
    }

Evitare Content-Type personalizzati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si raccomanda di evitare l'uso di media-type personalizzati come da :RFC:`6838` section-3.4 (eg.
``application/x.custom.name+json``) ed utilizzare nomi standard come:

- `application/json​ <https://www.iana.org/assignments/media-types/application/json>`__,
- `application/problem+json​ <https://www.iana.org/assignments/media-types/application/problem+json>`__,
- `application/jose+json​ <https://www.iana.org/assignments/media-types/application/jose+json>`__,

Si raccomanda di utilizzare Content-Type semanticamente coerenti
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando si ritornano dati binari, immagini o documenti (eg. pdf, png, ...)
utilizzare

.. code-block::

   Content-Type: application/pdf


Utilizzare le properties secondo nomenclature standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le properties DEVONO utilizzare ove possibile la nomenclatura indicata
nelle `Linee Guida per la valorizzazione del Patrimonio informativo
pubblico <https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/>`__
e le `relative ontologie <https://github.com/italia/daf-ontologie-vocabolari-controllati>`__.


Si raccomanda di utilizzare formati standard per Data ed Ora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le date DEVONO essere conformi ad :RFC:`3339`,
ad esempio `2015-05-28` per la data e `2015-05-28T14:07:17Z` per l'ora.

Le date negli header HTTP DEVONO essere conformi allo standard
`HTTP date format`_ definito in :RFC:`7231`.

:RFC:`3339` permette di indicare una timezone prefissando la data con la
distanza da UTC:

-  `2015-05-28T14:07:17+01:00`
-  `2015-05-28T14:07:17-05:00`

Quando la data è specificata in UTC occorre utilizzare sempre il
suffisso Z (Zulu time zone)

-  `2015-05-28T14:07:17Z`

Tempi di durata e intervalli devono utilizzare ISO 8601.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito alcuni esempi di durata in formato ​\ `ISO 8601 per i tempi
di durata​ <https://www.iso.org/iso-8601-date-and-time-format.html>`__.

Le durate sono prefissate da "P", giorni e Ore sono separati da "T".

Esempi:

- ``P1Y2M3D`` - 1 anno, 2 mesi e 3 giorni
- ``PT1H4M5S`` - 1 ora, 4 minuti e 5 secondi
- ``P1M`` - 1 mese
- ``PT1M`` - 1 minuto
- ``P1Y2M10DT2H30M`` - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

Un'analoga sintassi ISO8601 per lo stesso intervallo è la seguente:

``P0001-02-10T2:30:00``


Utilizzare le seguenti convenzioni di rappresentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  I booleani non DEVONO essere ``null``.
-  Gli array vuoti non DEVONO essere ``null``, ma liste vuote, ad es. ``[]``.
-  Le enumeration DEVONO essere rappresentate da stringhe non nulle.

Usare standard per Lingue, Nazioni e Monete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilizzare per le codifiche web gli standard indicati in Linee Guida per
la Valorizzazione del Patrimonio Informativo Nazionale, inclusi:

-  `ISO 3166-1-alpha2 country (due lettere) <https://www.iso.org/iso-3166-country-codes.html>`__
-  `ISO 639-1 language code <https://www.iso.org/standard/22109.html>`__
-  :BCP:`47` (basato su ISO 639-1) per le varianti dei linguaggi.
-  `ISO 4217 alpha-3 currency codes​ <https://www.iso.org/iso-4217-currency-codes.html>`__


Per le valute, è possibile basarsi sullo schema Money - ripreso dal
lavoro di standardizzazione del ​\ `Berlin Group sotto l'egida dell'European Standards​ <https://www.berlin-group.org/>`__
e contenente i campi:

-  amount​ (string)
-  currency (iso-4217)

Esempio 1:

.. code-block:: JSON

    {
       "tax_id": "imu-e472",
       "value": {
          "amount": "100.23",
          "currency": "EUR"
       }
    }


Definire ``format`` quando si usano i tipi Number ed Integer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I numeri e gli interi DEVONO indicare la dimensione utilizzando
il parametro ``format``. La seguente tabella - non esaustiva - elenca
un set minimo di formati. Le implementazioni DEVONO utilizzare il tipo più adatto.

Le parti possono concordare la definizione di nuovi tipi, che dev'essere
documentata nell'interfaccia.

.. csv-table::
    :header:  type,   format,   valori ammessi

    integer,  int32,    interi tra -2^31 e 2^31-1
    integer,  int64,    interi tra -2^63 e 2^63-1
    number,   decimal32 / float,    IEEE 754-2008/ISO 60559:2011 decimale a 32 bit
    number,   decimal64 / double,    IEEE 754-2008/ISO 60559:2011 decimale a 64 bit
    number,   decimal128,   IEEE 754-2008/ISO 60559:2011 decimale a 128 bit


Le proprietà degli oggetti JSON devono avere un naming consistente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Segliere uno dei due stili di seguito e codificarlo in ASCII:

-  snake_case
-  camelCase

Non usare contemporaneamente snake_case e camelCase nella stessa API.

Analogamente non usare contemporaneamente i due stili nella naming
convention, ad esempio

-  sì​: ``{ "givenName": "Mario", "familyName": "Rossi"}``
-  sì: ``{ "given_name": "Mario", "family_name": "Rossi"}``
-  no: ``{ "givenName": "Mario", "family_name": "Rossi"}``


Progettazione e Naming delle Interfacce di Servizio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In assenza di specifiche regole (es. HL7, INSPIRE, ..) per l'API Naming,
valgono le seguenti.

Uso corretto dei metodi HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


I metodi HTTP devono essere utilizzati rispettando la semantica indicata
in :RFC:`7231` section-4.3.

.. TODO rimuovere la parte ridondante dal resto.

Uso corretto degli header HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In generale gli header:

-  DEVONO essere utilizzati solo per passare informazioni di contesto

-  la semantica e gli intenti delle operazioni deve essere definita
   tramite URI, Status e Method e non dagli Header, che dovrebbero supportare
   funzionalità di protocollo come indicato ​in :RFC:`7231`.

Prima di usare un header:

-  si deve verificare se è già adottato da IANA _IANA_message_headers



Usare parole separate da trattino "-" per i Path (kebab-case)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo si applica solo al Path.


Esempio:

::

    /​tax-code​/{tax_code_id}

Inoltre, il Path dovrebbe essere semplice, intuitivo e coerente.


Preferire Hyphenated-Pascal-Case per gli header HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esempi:

::

    Accept-Encoding

    Apply-To-Redirect-Ref

    Disposition-Notification-Options

    Original-Message-ID


Le collezioni di risorse possono usare nomi al plurale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si consiglia di differenziare il nome delle collezioni e delle risorse. Questo permette di
separare a livello di URI, endpoint che sono in larga parte funzionalmente differenti.

Esempio 1: ricerca documenti per data in una collezione

::

    GET /​documenti​?data=2018-05-01

    {
      "items": [ .. ]
      "limit": 10
      "next_cursor": 21314123
    }

Esempio 2: recupera un singolo documento

::

    GET /​documento​/21314123

    {

      "id": 21314123
      "title: "Atto di nascita ...",
      ..
    }

Utilizzare Query Strings standardizzate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esempio 1: La paginazione dev'essere implementata tramite i parametri:

::

    cursor, limit, offset, sort

Esempio 2: La ricerca, il filtering e l'embedding dei parametri
dev'essere implementata tramite i parametri:

::

    q, fields, embed

.. TODO completare l'elenco.

Non passare credenziali o dati riservati nell'URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eventuali dati riservati o credenziali e token di autenticazione 
NON DEVONO essere passati nei query parameters o comunque
nell'URL.


Non usare l'header ``Link`` :RFC:`8288` se la response è in JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eventuali link a risorse vanno restituiti nel payload. Va\' invece
evitato di ritornare l'header ``Link`` definito in :RFC:`8288`
(già :RFC:`5988`).

Usare URI assoluti nei risultati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Restituendo URI assoluti si indica chiaramente al client l'indirizzo
delle risorse di destinazione e non si obbligano i client a fare
"inferenza" dal contesto.

Usare lo schema Problem JSON per le risposte di errore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In caso di errori si deve ritornare:

-  un payload di tipo Problem definito in :RFC:`7807`
-  il media type dev'essere ``application/problem+json``
-  lo status code dev'essere esplicativo
-  l'oggetto può essere esteso

Quando si restituisce un errore è importante *non esporre dati interni*
delle applicazioni.

Per prevenire il rischio di user-enumeration, i messaggi di errore 
di autenticazione non devono fornire informazioni sull'esistenza o meno dell'utenza.


Dopo aver validato il contenuto delle richieste si DEVE ritornare:

-  :httpstatus:`415`  se il Content-Type non è supportato;
-  :httpstatus:`400` o :httpstatus:`404` se si ipotizza che la richiesta sia malevola;
-  :httpstatus:`422`  se la representation della richiesta è sintatticamente corretta
   ma semanticamente non processabile.


Ottimizzare l'uso della banda e migliorare la responsività
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Utilizzare quando possibile:

-  tecniche di compressione;
-  paginazione;
-  un filtro sugli attributi necessari;
-  le specifiche di optimistic locking (:httpheader:`ETag`, if-(none-)match) :RFC:`7232`

E' possibile ridurre l'uso della banda e velocizzare le richieste
filtrando i campi delle risorse restituite.

Esempio 1: Non filtrato

.. code-block:: HTTP
    :caption: Request

    GET http://api.example.org/resources/123 HTTP/1.1

.. code-block:: HTTP
    :caption: Response

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "id":"cddd5e44-dae0-11e5-8c01-63ed66ab2da5",
      "name":"Mario Rossi",
      "address":"via del Corso, Roma, Lazio, Italia",
      "birthday":"1984-09-13",
      "partner":{
        "id":"1fb43648-dae1-11e5-aa01-1fbc3abb1cd0",
        "name":"Maria Rossi",
        "address":"via del Corso, Roma, Lazio, Italia",
        "birthday":"1988-04-07"
      }
    }

Esempio 2: Filtrato

.. code-block:: HTTP
    :caption: Request

    GET /resources/123?fields=(name,partner(name)) HTTP/1.1

.. code-block:: HTTP
    :caption: Response

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "name": "Mario Rossi",
        "partner": {
            "name": "Maria Rossi"
        }
    }

Effettuare la Resource Expansion permette di ridurre il numero di
richieste, quando bisogna ritornare risorse correlate tra loro.

In tal caso va usato:

-  il​ parametro ``embed`` utilizzando lo stesso formato dei campi per il
   filtering
-  l'attributo ``_embedded`` contenente le entry espanse.


.. code-block:: HTTP
    :caption: Request

    GET /tax_code/MRORSS12T05E472W?embed=(person) HTTP/1.1
    Accept: application/json

.. code-block:: HTTP
    :caption: Response

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "tax_code":"MRORSS12T05E472W",
      "_embedded":{
        "person":{
          "given_name":"Mario",
          "family_name":"Rossi",
          "id":"1234-ABCD-7890"
        }
      }
    }


Di default il caching http deve essere disabilitato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il caching va' disabilitato tramite :httpheader:`Cache-Control`
per evitare che delle richieste vengano inopportunamente messe in
cache. Esempio:

.. code-block::

    Cache-Control​: no-cache


Le API che supportano il caching devono documentare le varie limitazioni
e modalità di utilizzo tramite gli header definiti in :RFC:`7234`

-  :httpheader:`Cache-Control`
-  :httpheader:`Vary`

Eventuali conflitti nella creazione di risorse vanno gestiti tramite gli
header:

-  `ETag <https://tools.ietf.org/html/rfc7232#section-2.3>`__
-  `If-Match <https://tools.ietf.org/html/rfc7232#section-3.1>`__
-  `If-None-Match <https://tools.ietf.org/html/rfc7232#section-3.2>`__.

contenenti un hash del response body, un hash dell'ultimo campo
modificato della entry o un numero di versione.

Riferimenti
~~~~~~~~~~~~~~

Specifiche

-  `OpenAPI Specification <https://github.com/OAI/OpenAPI-Specification/>`__
- :BCP:`bcp47`


Articoli

-  `Roy Thomas Fielding - Architectural Styles and the Design of Network-Based <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`__
-  `Software Architectures​ <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`__ Definizione teorica dell'approccio REST.


Libri​

-  `PIs: From Start to Finish <http://www.infoq.com/minibooks/emag-web-%20api>`__

-  `Blogs <http://www.amazon.de/REST-Practice-Hypermedia-Systems-%20Architecture/dp/0596805829>`__

-  `Service Design Patterns <http://www.servicedesignpatterns.com/>`__

-  `REST in Practice: Hypermedia and Systems Architecture <http://www.amazon.de/REST-Practice-Hypermedia-Systems-%20Architecture/dp/0596805829>`__

-  `Build APIs You Won't Hate <https://leanpub.com/build-apis-you-wont-hate>`__

-  `InfoQ eBook - Web A​PIs: From Start to Finish​ <http://www.infoq.com/minibooks/emag-web-%20api>`__\ `¶ <http://www.infoq.com/minibooks/emag-web-api>`__

​Blogs

-  `Lessons-learned blog: Thoughts on RESTful API
   Design <http://restful-api-%20design.readthedocs.org/en/latest/>`__

.. [1]
   a-z\_



Raccomandazioni tecniche per SOAP
==================================

Nell'ambito del protocollo SOAP ai fini dell'interoperabilità è definito in WS-I Basic Profile.

ModI assume l'adozione della specifica `WS-I Basic Profile versione 2.0 <http://www.ws-i.org/Profiles/BasicProfile-2.0-2010-11-09.html>`__
, in quanto i framework implementativi più diffusi sono conformi a questa specifica.

Di seguito sono riportate suggerimenti al fine di favorire l'interoperabilità.


Evitare l'uso di media-type personalizzati
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Si raccomanda di evitare l'uso di media-type personalizzati come da :RFC:`6838` section-3.4
(eg. ``application/x.custom.name+xml``) ed utilizzare nomi standard come
​ `application/xml`_


Utilizzare le properties secondo nomenclature standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le properties DEVONO utilizzare ove possibile la nomenclatura indicata
nelle `Linee Guida per la valorizzazione del Patrimonio informativo
pubblico <https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/>`__
e le `relative ontologie <https://github.com/italia/daf-ontologie-vocabolari-controllati>`__.


Utilizzare formati standard per Data ed Ora
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le date DEVONO essere conformi ad :RFC:`3339`,
ad esempio `2015-05-28` per la data e `2015-05-28T14:07:17Z` per l'ora.

:RFC:`3339` permette di indicare una timezone prefissando la data con la
distanza da UTC:

-  `2015-05-28T14:07:17+01:00`
-  `2015-05-28T14:07:17-05:00`

Quando la data è specificata in UTC occorre utilizzare sempre il
suffisso Z (Zulu time zone)

-  `2015-05-28T14:07:17Z`


Tempi di durata e intervalli devono utilizzare ISO 8601.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Di seguito alcuni esempi di durata in formato ​\ `ISO 8601 per i tempi
di durata​ <https://www.iso.org/iso-8601-date-and-time-format.html>`__.

Le durate sono prefissate da "P", giorni e Ore sono separati da "T".

Esempi:

- ``P1Y2M3D`` - 1 anno, 2 mesi e 3 giorni
- ``PT1H4M5S`` - 1 ora, 4 minuti e 5 secondi
- ``P1M`` - 1 mese
- ``PT1M`` - 1 minuto
- ``P1Y2M10DT2H30M`` - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

Un'analoga sintassi ISO8601 per lo stesso intervallo è la seguente:

``P0001-02-10T2:30:00``


Usare standard per Lingue, Nazioni e Monete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Utilizzare per le codifiche web gli standard indicati in Linee Guida per
la Valorizzazione del Patrimonio Informativo Nazionale, inclusi:

-  `ISO 3166-1-alpha2 country (due lettere) <https://www.iso.org/iso-3166-country-codes.html>`__
-  `ISO 639-1 language code <https://www.iso.org/standard/22109.html>`__
-  :BCP:`47` (basato su ISO 639-1) per le varianti dei linguaggi.
-  `ISO 4217 alpha-3 currency codes​ <https://www.iso.org/iso-4217-currency-codes.html>`__


Descrittività dei nomi utilizzati
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I nomi utilizzati per servizi ed operazioni nelle interfacce di servizio
devono essere auto-descrittivi e fornire quanta più informazione possibile riguardo al
comportamento implementato.

Si deve inoltre evitare l'utilizzo di acronimi quando questi non siano
universalmente riconosciuti anche al di fuori del dominio applicativo.


Utilizzo di camelCase e PascalCase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Per i nomi dei servizi si suggerisce di utilizzare PascalCase mentre per le
operazioni implementate e gli argomenti si suggerisce l'utilizzo del camelCase.


Non includere il numero di versione all'interno del nome del servizio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Unicità dei namespace e utilizzo di pattern fissi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ove possibile all'interno del WSDL deve essere presente un namespace unico.

I namespace utilizzati per i servizi devono seguire un pattern specifico. In
particolare, per i servizi:

::

    http://<dominioOrganizzativo>/ws/<DominioApplicativo>/<NomeServizio>/V<major>

dove:

- ``<dominioOrganizzativo>`` indica l'organizzazione che espone il servizio,
- ``<DominioApplicativo>`` indica il settore all'interno dell'organizzazione,
- ``<NomeServizio>`` segue le specifiche di cui ai punti precedenti, e <major> indica il
  numero di versione (difatti non inserito nel nome del servizio).

Per quanto riguarda gli XSD all'interno del WSDL si segue il pattern
seguente:

::

    http://<dominioOrganizzativo>/xmlns/<DominioApplicativo>


Riferimenti
~~~~~~~~~~~~~~~~~~


.. _`HTTP date format`: :RFC:`7231#section-7.1.1.1`

.. _`Linee Guida per lo sviluppo di sicuro di codice`:
    https://www.agid.gov.it/sites/default/files/repository_files/documentazione/linee_guida_per_lo_sviluppo_sicuro_di_codice_v1.0.pdf


.. _IANA_message_headers: https://www.iana.org/assignments/message-headers/message-headers.xhtml

Specifiche


.. _application/xml: https://www.iana.org/assignments/media-types/application/xml

SOAP 1.2 ​\ `Parte 1​ <https://www.w3.org/TR/soap12/>`__ e ​\ `Parte
2 <https://www.w3.org/TR/soap12-part2/>`__

`WS-I Basic Profile
2.0 <http://ws-i.org/profiles/BasicProfile-2.0-2010-11-09.html>`__

`WS-Addressing <https://www.w3.org/Submission/ws-addressing/>`__

`Standard eHealth
Ontario <https://www.ehealthontario.on.ca/architecture/education/courses/service-%20oriented-architecture/downloads/SOA-ServiceNamingConventions.pdf>`__

Libri

.. _`UML Components`: https://www.pearson.com/us/higher-education/program/Cheesman-UML-Components-A-Simple-Process-for-Specifying-Component-Based-pro%20Software/PGM319361.html>
