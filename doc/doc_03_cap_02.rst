Profili di Interazione
=======================

Il *profilo di interazione* definisce le modalità secondo le quali un
fruitore ed un erogatore possono interagire, l'interazione avviene
definendo le interfacce di servizio.
I *profili di interazione* quali riferimenti
concettuali coniugano, fatto salvo per l'accesso CRUD, message exchange
pattern (MEP) per le tecnologie SOAP e REST proposte dal ModI.
Di seguito l'attenzione è rivolta agli
aspetti funzionali rimandando per gli aspetti di sicurezza all'apposito documento
delle linee guida.

Per i concetti di bloccante e non bloccante si rimanda alla lettura di "Concetti di base".

Descrizione delle API
---------------------

Ogni interfaccia di servizio deve essere rappresentata mediante
un IDL - Interface Description Language standard - che il ModI fissa:

-  per le interfacce di servizio REST, OpenAPI 3.0 e successive

-  per le interfacce di servizio SOAP, WSDL 1.1 e successive

L'endpoint deve indicare in modo esplicito la tecnologia utilizzata
(REST o SOAP) e la versione (versioning su URL).


Logging
-------

I log DEVONO contenere:

- l'istante della comunicazione in formato RFC3339, in UTC e con i separatori Z e T in maiuscolo.
  Questa specifica è fondamentale per l’interoperabilità dei sistemi di logging e auditing,
  evitando problemi di transizione all’ora legale e la complessità nella gestione di fusi orari
  nell’ottica dell’interoperabilità con altre PA europee;
- l'URI che identifica erogatore e l’operazione richiesta;
- tipologia di chiamata (ad es., metodo HTTP per i protocolli basati su HTTP);
- esito della chiamata (ad es., stato della response HTTP se disponibile, SOAP fault nel caso di web service SOAP);
- ove applicabile, l’Indirizzo IP del client;
- ove applicabile, identificativo del consumatore o altro soggetto operante la richiesta comunicato dal fruitore
  - è cura del fruitore procedere alla codifica e l'anonimizzazione, ove necessario;
- ove applicabile, un identificativo univoco della richiesta, utile a eventuali correlazioni.


Versioning
----------

Il versionamento DEVE rispettare le regole del Semantic Versioning 2.0 ed in particolare:

- la versione deve rispettare la sintassi <MAJOR>.<MINOR>.<PATCH>
- incrementare la versione MAJOR quando si apportano modifiche incompatibili alle API;
- incrementare la versione MINOR quando si aggiungono nuove funzionalità in modo retrocompatibile;
- incrementare la versione PATCH quando si apportano correzioni di bug retrocompatibili o modifiche editoriali
  che non influiscono sulle funzionalità o in generale sulla fruizione dell'API.



.. toctree::
  :maxdepth: 2
  :caption: Contenuti

  profili-di-interazione/modalità-di-descrizione-dei-profili.rst
  profili-di-interazione/profilo-bloccante-rpc.rst
  profili-di-interazione/profili-non-bloccanti.rst
  profili-di-interazione/accesso-crud-a-risorse.rst
  profili-di-interazione/regole-comuni-rest-soap.rst
  profili-di-interazione/robustezza.rst
  profili-di-interazione/passaggio-di-allegati.rst

.. discourse::
   :topic_identifier: 8904
