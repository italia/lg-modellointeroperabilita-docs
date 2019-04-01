SOAP
================

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

,  Riferimenti
~~~~~~~~~~~~~~~~~~

.. _FatturePA: http://www.fatturapa.gov.it/export/fatturazione/sdi/Specifiche_tecniche_del_formato_FatturaPA_v1.0.pdf

.. _`HTTP date format`: http://tools.ietf.org/html/rfc7231#section-7.1.1.1


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
