Dominio di interoperabilità
===========================

Nell’ambito della presente Linea di indirizzo, per dominio di
interoperabilità si indica uno specifico contesto in cui più Pubbliche
Amministrazioni e/o soggetti privati hanno l’esigenza di scambiare dati
e/o integrare i propri processi per dare seguito al disposto normativo.

Ogni dominio di interoperabilità è caratterizzato da:

-  i soggetti partecipanti, le Pubbliche Amministrazioni e gli eventuali
   soggetti privati (cittadini e imprese);

-  i sistemi informatici dei soggetti partecipanti che scambiano dati
   e/o integrano i propri processi;

-  l’insieme di API implementate per garantire le interazioni tra i
   sistemi informatici dei soggetti partecipanti;

-  i criteri di sicurezza che le singole API forniscono per assicurare
   transazioni tra i soggetti partecipanti conformi alla norma.

   11. .. rubric:: Logging
          :name: logging

Il logging riveste un ruolo fondamentale nella progettazione e nello
sviluppo di API. Le moderne piattaforme middleware, oltre ad integrare
meccanismi di logging interni, possono connettersi ad API esterne che
permettono la raccolta (log collection), la ricerca e la produzione di
analitiche, utili tra l’altro all’identificazione di problemi e al
monitoraggio del sistema e della QoS. L’utilizzo di log collector
permette di centralizzare non solo i log relativi all’utilizzo delle
API, ma anche quelli di eventuali altri servizi digitali e componenti di
rete (ad es., proxy e application-gateway). Ai fini di non ripudio, i
messaggi applicativi possono essere memorizzati insieme alla firma
digitale, ed archiviati nel rispetto della normativa sulla conservazione
e sulla privacy. L’erogatore deve documentare in dettaglio il formato e
le modalità di tracciatura, consultazione e reperimento delle
informazioni. L’erogatore non deve tracciare nei log segreti quali
password, chiavi private o token di autenticazione. L’erogatore deve
tracciare un evento per ogni richiesta, contenente almeno i seguenti
parametri minimi:

-  istante della richiesta;

-  identificativo dell’erogatore e dell’operazione richiesta;

-  tipologia di chiamata;

-  esito della chiamata;

-  identificativo del fruitore;

-  ove applicabile, identificativo del consumatore o altro soggetto
   operante la richiesta comunicato dal fruitore - è cura del fruitore
   procedere alla codifica e l'anonimizzazione, ove necessario;

-  ove applicabile, un identificativo univoco della richiesta, utile a
   eventuali correlazioni.

   12. .. rubric:: Pattern e profili di interoperabilità
          :name: pattern-e-profili-di-interoperabilità

La Linea di indirizzo individua:

-  pattern di interoperabilità, ovvero la definizione di una soluzione a
   una esigenza di scambio di messaggi e informazioni, declinata in una
   specifica tecnologia. Si suddividono in:

   -  pattern di interazione, puntualizzano le modalità tecniche per
      implementare i modelli di scambio dei messaggi (anche detti
      message exchange patterns) [1]_, necessari all’interazione tra i
      sistemi informatici di erogatori e fruitori;

   -  pattern di sicurezza, individuano le modalità tecniche per
      assicurare che i pattern di interazione rispettino specifiche
      esigenze di sicurezza (autenticazione e autorizzazione delle
      parti, confidenzialità delle comunicazioni, integrità dei messaggi
      scambiati, ...) negli scambi realizzati;

-  profili di interoperabilità, la combinazione di più pattern per
   descrivere le esigenze di specifici domini di interoperabilità, quale
   ad esempio il non ripudio delle comunicazioni e/o dei messaggi
   scambiati.

I pattern e profili di interoperabilità individuati nei Documenti
operativi della Linea di indirizzo sono utilizzati dalle PA
nell’implementazione delle proprie API. Le PA selezionano i pattern e/o
i profili di interoperabilità sulla base delle specifiche esigenze del
dominio di interoperabilità a cui partecipano.

.. [1]
   Cf. https://en.wikipedia.org/wiki/Messaging_pattern
