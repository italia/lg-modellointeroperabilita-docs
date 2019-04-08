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

Si raccomanda di evitare l'uso di media-type personalizzati come da ​:RFC:`6838#section-3.4` (eg.
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

Le date devono essere conformi ad :RFC:`3339`,
ad esempio `2015-05-28` per la data e `2015-05-28T14:07:17Z` per l'ora.

Le date negli header HTTP devono essere conformi allo standard
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
di durata​ <https://en.wikipedia.org/wiki/ISO_8601#Durations>`__.

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

-  I booleani non devono essere ``null``.
-  Gli array vuoti non devono essere ``null``, ma liste vuote, ad es. ``[]``.
-  Le enumeration devono essere rappresentate da stringhe non nulle.

Usare standard per Lingue, Nazioni e Monete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilizzare per le codifiche web gli standard indicati in Linee Guida per
la Valorizzazione del Patrimonio Informativo Nazionale, inclusi:

-  `ISO 3166-1-alpha2 country (due lettere) <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
-  `ISO 639-1 language code <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__
-  :BCP:`47` (basato su ISO 639-1) per le varianti dei linguaggi.
   Dove non strettamente necessario il subta​g​​, basta la prima parte (ad es. it vs it- IT)
-  `ISO 4217 currency codes​ <http://en.wikipedia.org/wiki/ISO_4217>`__
   alpha-3

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

I numeri e gli interi devono indicare la dimensione utilizzando
il parametro ``format``. La seguente tabella - non esaustiva - elenca
un set minimo di formati. Le implementazioni devono utilizzare il tipo più adatto.

Le parti possono concordare la definizione di nuovi tipi, che dev'essere
documentata nell'interfaccia.

.. csv-table::

    :header:  type,   format,   valori ammessi
    integer,  int32,    interi tra -2^31 e 2^31-1
    integer,  int64,    interi tra -2^63 e 2^63-1
    number,   decimal32 o float,    IEEE 754-2008/ISO 60559:2011 decimale a 32 bit
    number,   decimal64 o double,    IEEE 754-2008/ISO 60559:2011 decimale a 64 bit
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

Preferire l'uso di ASCII snake_case al camelCase:  [1]_``[a-z_0-9]*$``.
Sebbene sia possibile scegliere coerentemente, ove possibile si deve preferire
l'utilizzo dello snake_case.

Progettazione e Naming delle Interfacce di Servizio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In assenza di specifiche regole (es. HL7, INSPIRE, ..) per l'API Naming,
valgono le seguenti.

Uso corretto dei metodi HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metodi HTTP devono essere utilizzati rispettando la semantica indicata
in

`rfc7231#section-4.3 <https://tools.ietf.org/html/rfc7231#section-4.3>`__

Uso corretto degli header HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In generale gli header:

-  devono essere utilizzati solo per passare informazioni di contesto
-  la semantica e gli intenti delle operazioni deve essere definita
   tramite URI, Status e Method e non dagli Header, che dovrebbero supportare
   funzionalità di protocollo come flow control, content negotiation, ed authentication,
   come indicato ​in :RFC:`7231`.

Prima di usare un header:

-  si deve verificare se è già adottato da IANA

`https://www.iana.org/assignments/message-headers/message-headers.xhtml <https://www.iana.org/assignments/message-headers/message-%20headers.xhtml>`__

Usare l'appropriato REST Maturity Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le API devono seguire le indicazioni in ​\ `REST Maturity Level
2​ <http://martinfowler.com/articles/richardsonMaturityModel.html#level2>`__
in modo da essere resource-oriented e fare affidamento su HTTP verbs e
status. Questo include:

-  Evitare le azioni e ragionare intorno alle risorse
-  Evitare i verbi negli URL
-  Usare correttamente gli HTTP method
-  Usare gli status HTTP appropriati

Per API destinate ad interfacciarsi con un front-end o con le persone,
può aver senso adottare un approccio di tipo HATEOAS o ​\ `REST Maturity
Level
3​ <http://martinfowler.com/articles/richardsonMaturityModel.html#level3>`__.

In un contesto machine-to-machine dove le interazioni sono spesso
predefinite, la complessità di HATEOAS non porta necessariamente dei
benefici.

Quando le risorse contengono link e riferimenti a risorse esterne, si
dovrebbero usare le specifiche indicate in ​\ `IANA registered link
relations​ <http://www.iana.org/assignments/link-relations/link-relations.xml>`__.
Se le specifiche IANA contengono dei dash ``-``, questi vanno convertiti
in underscore ``_``, e​g. ``terms-of-service -> terms_of_service``.

Esempio: una ricerca paginata con link relations.

.. code-block::

    GET /dipendenti?nome=Mario%20Rossi&amp;limit=2

    {
      "limit": 2,
      "items":[
        {
          "id":"RSSMRA75L01H501A",
          "nome":"Mario Rossi",
          "coniuge":{
            "href":"https://...",
            "id":"BNCFNC75A41H501G",
            "nome":"Francesca Bianchi"
          }
        },
        {
          "id":"RSSMRA77L01H501A",
          "nome":"Mario Rossi",
          "coniuge":{
            "href":"https://...",
            "id":"VRDBNC81A41H501S",
            "nome":"Bianca Verdi"
          }
        }
      ],
      "first":"https://...",
      "next":"https://...",
      "prev":"https://...",
      "last":"https://..."
    }


Usare parole separate da trattino "-" per i Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo si applica solo al Path, e non ai parametri del path (eg.
{tax_code_id}).

Esempio:

::

    /​tax-code​/{tax_code_id}

Inoltre, il Path dovrebbe essere semplice, intuitivo e coerente.

Usare un case consistente snake_case o camelCase per i Query Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una volta scelto un case, siate consistenti: non mescolare snake_case e
camelCase nella stessa API.

I nomi utilizzati devono usare abbreviazioni e acronimi universalmente
riconosciuti

Preferire Hyphenated-Pascal-Case per gli header HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esempi:

::

    Accept-Encoding

    Apply-To-Redirect-Ref

    Disposition-Notification-Options

    Original-Message-ID

Le collezioni di risorse devono usare nomi al plurale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Differenziare il nome delle collezioni e delle risorse permette di
separare a livello di URI endpoint che sono in larga parte funzionalmente differenti.

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

    q, fields. embed

E' possibile trovare un elenco di parametri standardizzati nel
repository:

- https://github.com/teamdigitale/openapi/tree/master/docs

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

-  un payload di tipo Problem definito in ​:RFC:`7807`
-  il media type dev'essere ``application/problem+json``
-  lo status code dev'essere esplicativo
-  l'oggetto può essere esteso

Quando si restituisce un errore è importante *non esporre dati interni*
delle applicazioni e seguire le indicazioni nel §6.4 delle `Linee Guida per lo sviluppo di sicuro di codice`_


Ottimizzare l'uso della banda e migliorare la responsività
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Utilizzare quando possibile:

-  gzip compression;
-  paginazione;
-  un filtro sugli attributi necessari;
-  le specifiche di optimistic locking (etag, if-(none-)match)

E' possibile ridurre l'uso della banda e velocizzare le richieste
filtrando i campi delle risorse restituite. Si vedano qui ulteriori
informazioni su come supportare il filtraggio dei campi delle risorse
ritornate:

https://cloud.google.com/compute/docs/api/how-tos/performance#partial

Esempio 1: Non filtrato

::

    >> Request:
    GET http://api.example.org/resources/123 HTTP/1.1
    HTTP/1.1 200 OK

    << Response:
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

Esempio 2: Filtrato `<http://zalando.github.io/restful-api-guidelines/index.html#filtered>`__

::

    >> Request:
    GET http://api.example.org/resources/123?fields=(name,partner(name)) HTTP/1.1

    << Response:
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

::

    >> Request:
    GET /tax_code/MRORSS12T05E472W?embed=(person) HTTP/1.1

    << Response:
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


Di default il caching deve essere disabilitato tramite:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Cache-Control​: no-cache header.

in modo da evitare che delle richieste vengano inopportunamente messe in
cache.

Le API che supportano il caching devono documentare le varie limitazioni
e modalità di

utilizzo tramite gli header definiti in :RFC:`7234`

-  Cache-Control
-  Vary

Eventuali conflitti nella creazione di risorse vanno gestiti tramite gli
header:

-  `ETag <https://tools.ietf.org/html/rfc7232#section-2.3>`__
-  `If-Match <https://tools.ietf.org/html/rfc7232#section-3.1>`__
-  `If-None-Match​ <https://tools.ietf.org/html/rfc7232#section-3.2>`__.

contenenti un hash del response body, un hash dell'ultimo campo
modificato della entry o un numero di versione.

Se l'etag della entry su cui si opera non corrisponde al valore della
richiesta, la response ritorna lo status code ``412 - precondition failed``.

Le API devono supportare la paginazione delle collezioni tramite:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  paginazione classica tramite i query parameter offset e limit

-  paginazione con cursore; la paginazione a cursore permette
   l'implementazione di pagine con infinite scrolling.

La paginazione dovrebbe essere implementata in modo da limitare l'uso
improprio delle API (eg. download in parallelo di interi dataset, ...)

Per il ripristino del download di un documento si faccia riferimento a
Range Requests :RFC:`7233`.


Supportare le informazioni di inoltro tramite l'header Forwarded
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le informazioni di inoltro HTTP (eg. indirizzo ip di provenienza,
destinazione ...) erogatori devono essere:

-  preservate​ dall'infrastruttura

-  scambiate tramite l'header Forwarded definito in :RFC:`7239` e pronto per
   IPv6 :RFC:`8200`.

eg.

.. ::

   Forwarded: for=192.0.2.60; for="[2001:db8:cafe::17]"; proto=https; by=203.0.113.43

Gli header ``X-Forwarded-For`` ``X-Forwarded-Host`` e ``X-Forwarded-Proto`` - che
non hanno un comportamento codificato e dipendono dalle varie implementazioni,
devono comunque essere supportati e preservati.


Riferimenti
~~~~~~~~~~~~~~

Specifiche

-  `OpenAPI
   Specification <https://github.com/OAI/OpenAPI-Specification/>`__
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

l'utilizzo del protocollo SOAP ai fini di interoperabilità è l'oggetto
del WS-I Basic Profile (BP) la cui versione 2.01 (ultima versione
rilasciata) è quella a cui fa riferimento il ModI. In particolare il
BP2.0 impiega SOAP 1.22 e WS-Addressing3. I framework implementativi più
diffusi sono conformi a questa specifica sulla quale quindi il presente
documento non si soffermerà. Indichiamo di seguito invece le best
practice relative alla specifica dei servizi e del formato dei dati.

Formato dei dati
~~~~~~~~~~~~~~~~~~~~~~~~~~

Codificare dati strutturati con oggetti XML

I dati strutturati devono essere trasferiti tramite ​oggetti XML​ che
utilizzano elementi contenitivi per le liste:

-  il payload di una response contenente una entry ritorna un oggetto

.. code-block:: XML

    <persona givenName="Paolo" familyName="Rossi" id="313" />

-  il payload di una response contenente più entry ​ritorna un oggetto
   contenente

una lista​ e non direttamente una lista.

.. code-block:: XML

    <persone>
        <persona givenName="Carlo" familyName="Bianchi" id="314" />
        <persona givenName="Giuseppe" familyName="Verdi" id="315" />
    </persone>

Vanno utilizzati namespace e definiti specifici XSD.

Evitare Content-Type personalizzati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 Cf. ​\ http://ws-i.org/profiles/BasicProfile-2.0-2010-11-09.html

2 Cf. ​\ https://www.w3.org/TR/soap12/

3 Cf. ​\ `https://www.w3.org/Submission/ws-
addressing/ <https://www.w3.org/Submission/ws-addressing/>`__

Evitare l'uso di media-type personalizzati come da ​\ `RFC 6838 <https://tools.ietf.org/html/rfc6838#section-3.4>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(eg.application/x.custom.name+xml) ed utilizzare nomi standard come
​ `application/xml`_

Utilizzare embedding o referencing per trasferire i dati binari.
l'inserimento di dati binari all'interno del payload può avvenire o tramite embedding (ed in questo
caso la codifica base64 è da preferirsi a quella esadecimale) oppure tramite referencing.

Attributi ed elementi devono utilizzare ove possibile la nomenclatura indicata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

nelle Linee Guida per la valorizzazione del Patrimonio informativo
nazionale e le relative ontologie

Utilizzare formati standard per Data ed Ora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le date devono essere conformi ad :RFC:`3339`,
ad esempio `2015-05-28` per la data e `2015-05-28T14:07:17Z` per l'ora.

Le date negli header HTTP devono essere conformi allo standard
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
di durata​ <https://en.wikipedia.org/wiki/ISO_8601#Durations>`__.

Le durate sono prefissate da "P", giorni e Ore sono separati da "T".

Esempi:

- ``P1Y2M3D`` - 1 anno, 2 mesi e 3 giorni
- ``PT1H4M5S`` - 1 ora, 4 minuti e 5 secondi
- ``P1M`` - 1 mese
- ``PT1M`` - 1 minuto
- ``P1Y2M10DT2H30M`` - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

Un'analoga sintassi ISO8601 per lo stesso intervallo è la seguente:

``P0001-02-10T2:30:00``

Utilizzare le convenzioni di rappresentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si consiglia l'utilizzo di elementi come figli di un elemento quando:

-  Può esistere come elemento a se stante

-  Occorre definire una lista (gli attributi non possono essere
   multivalore)

I nomi delle liste devono essere al plurale.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I ``Boolean`` non devono essere mai null.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le properties devono avere un naming consistente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

l'utilizzo più frequente è quello di camelCase sia per gli elementi che
per gli attributi. In alcuni casi è possibile utilizzare PascalCase per
gli elementi e camelCase per gli attributi (come nel
​\ `NIME <https://en.wikipedia.org/wiki/National_Information_Exchange_Model>`__\ 4)

Usare standard per Lingue, Nazioni e Monete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilizzare per le codifiche web gli standard indicati in Linee Guida per
la Valorizzazione del Patrimonio Informativo Nazionale, inclusi:

-  `ISO 3166-1-alpha2 country (due lettere) <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
-  `ISO 639-1 language code <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__
-  :BCP:`47` (basato su ISO 639-1) per le varianti dei linguaggi.
   Dove non strettamente necessario il subta​g​​, basta la prima parte (ad es. it vs it- IT)
-  `ISO 4217 currency codes​ <http://en.wikipedia.org/wiki/ISO_4217>`__
   alpha-3 usato in FatturePA_

Nel caso di importi, l'elemento dovrà contenere sia un elemento o attributo di tipo

standard xs:currency che una indicazione del codice della valuta. Ad esempio:

.. code-block:: XML

    <prezzo valuta="EUR" totale="100.00" />

Progettazione e Naming delle Interfacce di Servizio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ai fini del progetto delle interfacce di servizio, esistono diverse
metodologie. In particolare nel ModI si suggerisce l'utilizzo della metodologia di identificazione
delle interfacce contenuta nel libro ​\ `UML Components`_ che permette di identificare servizi ed operazioni per
i singoli componenti applicativi.

Descrittività dei nomi utilizzati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
I nomi utilizzati per servizi ed operazioni nelle interfacce di servizio
devono essere auto-descrittivi e fornire quanta più informazione possibile riguardo al
comportamento implementato.

Occorre inoltre eliminare il rischio di collisioni tra
nomi in differenti domini nel caso in cui un termine possa avere dei significati multipli
(es. protocollo).

Si deve inoltre evitare l'utilizzo di acronimi quando questi non siano
universalmente riconosciuti anche al di fuori del dominio applicativo.


Utilizzo di camelCase e PascalCase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I nomi dei servizi devono essere specificati in PascalCase mentre per le
operazioni implementate e gli argomenti si utilizza il camelCase.

Utilizzo di nomi agnostici rispetto all'implementazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I nomi utilizzati per i servizi e le operazioni non dovrebbero rivelare
dettagli implementativi.

4 Cf.
​\ https://en.wikipedia.org/wiki/National_Information_Exchange_Model

Non includere il numero di versione all'interno del nome del servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Non includere la parola Service nel nome del servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unicità dei namespace e utilizzo di pattern fissi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni servizio all'interno del WSDL deve avere un suo namespace unico. I
namespace

utilizzati per i servizi devono seguire un pattern specifico. In
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



Ottimizzare l'uso della banda e migliorare la responsività
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Utilizzare quando possibile, in special modo per le operazioni che
ritornano liste e risultati di ricerche:

-  gzip compression;
-  paginazione;
-  un filtro sugli attributi necessari.

Le interfacce devono supportare la paginazione delle collezioni tramite:

-  paginazione classica tramite parametri ``offset`` e ``limit``
-  paginazione a cursore permette l'implementazione di pagine con
   infinite scrolling.

La paginazione deve essere implementata in modo da limitare l'uso
improprio delle interfacce

(eg. download in parallelo di interi dataset, …)


Di default il caching deve essere disabilitato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

E' possibile disabilitare il caching tramite l'header:

-  Cache-Control: no-cache header.

in modo da evitare che delle richieste vengano inopportunamente messe in
cache.

Le API che supportano il caching devono documentare le varie limitazioni
e modalità di

utilizzo tramite gli header definiti in :RFC:`7324`

-  Cache-Control
-  Vary

In generale le richieste SOAP utilizzando il metodo HTTP POST (non
idempotente), ma nei casi in cui l'operazione effettuata è idempotente è
possibile implementare meccanismi di caching simili a quelli visti nel
caso REST.



Utilizzo degli status code HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. TODO verificare alla luce di quanto indicato negli altri capitoli

La versione 1.2 di SOAP definisce in dettaglio (si veda la parte 2 della
specifica) l'utilizzo di codici di stato HTTP come confermato dal basic profile 2.0.
Si richiede quindi l'utilizzo di questi codici.

Riferimenti
~~~~~~~~~~~~~~~~~~


.. _`HTTP date format`: :RFC:`7231#section-7.1.1.1`

.. _`Linee Guida per lo sviluppo di sicuro di codice`:
    https://www.agid.gov.it/sites/default/files/repository_files/documentazione/linee_guida_per_lo_sviluppo_sicuro_di_codice_v1.0.pdf

.. _FatturePA: http://www.fatturapa.gov.it/export/fatturazione/sdi/Specifiche_tecniche_del_formato_FatturaPA_v1.0.pdf


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
