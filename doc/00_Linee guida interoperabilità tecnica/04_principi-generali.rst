Principi generali
=================

Interazioni
-----------

L’ambito di applicazione delle Linee Guida, in coerenza con il ModI, 
comprende i tre tipi di interazioni previste nell’EIF che vedono 
coinvolte Pubbliche Amministrazioni, cittadini e imprese.

Le interazioni prevedono che i soggetti coinvolti possano svolgere 
la funzione di **erogatore di servizi, quando il soggetto mette a 
disposizione servizi digitali utilizzati da altri soggetti**, e la 
funzione di **fruitore di servizi, quando il soggetto utilizza i servizi 
digitali messi a disposizione da un altro soggetto**.

|image0|

*Figura 1 - Ambito di applicazione del modello di interoperabilità*

I soggetti fruitori possono utilizzare i servizi digitali in maniera 
trasparente all’erogatore, attraverso:

-  una soluzione software attivata da un attore umano (user agent/human);

-  un sistema applicativo automatico (server/machine), anche allo scopo 
   di definire nuovi servizi a valore aggiunto.

Application Programming Interface (API)
---------------------------------------

Con Application Programming Interface (API) si indica ogni insieme di 
procedure/funzionalità/operazioni disponibili al programmatore, di solito 
raggruppate a formare un insieme di strumenti specifici per l’espletamento 
di un determinato compito. Spesso, con tale termine si intendono le 
librerie software disponibili in un certo linguaggio di programmazione. 
Una buona API fornisce una "scatola nera", cioè un livello di astrazione 
che evita al programmatore di conoscere i dettagli implementativi 
dell’API stessa. Questo permette di ri-progettare o migliorare le funzioni 
all’interno dell’API, senza cambiare il codice che si affida ad essa. 
La finalità di un’API è di ottenere un’astrazione a più alto livello, 
di solito tra lo strato sottostante l’API e i suoi consumatori (client).

Con Web API si indicano le API rese disponibili al client attraverso 
Internet (prevalentemente sul Web, che si basa sul protocollo HTTP).

Per il World Wide Web Consortium (W3C), un web service è qualsiasi 
software disponibile su Internet che standardizza la sua interfaccia 
tramite la codifica eXtensible Markup Language (XML). Un client interroga 
un servizio web inviando una richiesta in formato XML; il servizio web 
ritorna una risposta utilizzando l’analogo formato. Client e web service 
comunicano attraverso una rete che li connette e sfruttano generalmente 
il protocollo applicativo HTTP. I web service si basano principalmente 
su standard come XML-Remote Procedure Call (XML-RPC) e Simple Object 
Access Protocol (SOAP). Quindi, un web service è un possibile modo di 
realizzare una Web API. A partire dalla seconda metà degli anni 2000, 
creando possibili confusioni, il termine Web API è stato utilizzato 
come alternativa a web service per indicare altri 
approcci/protocolli/tecnologie, come le API REpresentational State 
Transfer (REST) per realizzare API senza utilizzare XML-RPC e SOAP.

**Nell’ambito delle Linee Guida, accettando la nomenclatura in uso a 
livello europeo e più in generale nel contesto internazionale, si utilizza 
il termine generico API per indicare indifferentemente le Web API, i web 
service e le API REST, lasciando al contesto in cui lo stesso è utilizzato 
la declinazione del significato esplicito.**

Le Linee Guida individuano le modalità con cui le Pubbliche Amministrazioni 
implementano le proprie API, quale elemento tecnologico di base del ModI, 
attraverso cui le Pubbliche Amministrazioni rendono disponibile gli 
e-service utilizzati dai sistemi informatici di altre Pubbliche 
Amministrazioni, cittadini e imprese.

.. |image0| image:: ./media/image1.png
   :width: 4.125in
   :height: 2.90278in


Qualità dei servizi
-------------------

Il concetto di qualità di servizio, anche comunemente chiamata Quality 
of Service (QoS), fa riferimento alla descrizione non funzionale di una 
API, cioè alla capacità di quest’ultima di soddisfare le aspettative 
dei fruitori. 

Assicurare la QoS nell’ambito Internet ai fini dell’interoperabilità è 
una sfida critica a causa della natura dinamica e impredicibile del 
contesto applicativo. Cambiamenti negli schemi di traffico, la presenza 
di transazioni critiche, gli effetti dei problemi di rete, le performance 
dei protocolli e degli standard di rete richiedono una definizione 
precisa della QoS offerta da una API.

Gli elementi chiave a supporto della QoS possono essere riassunti come 
segue:

-  Disponibilità. La probabilità che una API sia disponibile e 
   funzionante in un istante casuale. Associato al concetto di 
   disponibilità è quello di Time-To-Repair (TTR), cioè il tempo 
   necessario a ripristinare una API una volta che questa diventa 
   indisponibile. La disponibilità di una API dovrebbe potere essere 
   verificata tramite l’esposizione di una API di monitoraggio, dedicata 
   e a basso impatto (quindi a elevata disponibilità);

-  Accessibilità. Misura la capacità di una API di essere contattabile 
   in un qualunque istante di tempo;

-  Prestazioni. Le prestazioni vengono misurate solitamente rispetto a 
   due valori: il throughput e la latenza. Il throughput rappresenta il 
   numero di richieste soddisfatte in un dato intervallo. La latenza 
   rappresenta la quantità di tempo che passa tra l’invio di una richiesta 
   e la ricezione di una risposta. Una API con buone prestazioni ha un 
   elevato throughput e una bassa latenza;

-  Affidabilità. Rappresenta la capacità di una API di funzionare 
   correttamente e consistentemente, fornendo la stessa QoS a dispetto 
   di malfunzionamenti di diversa natura. Di solito è espressa in termini 
   di fallimenti in un dato lasso di tempo;

-  Scalabilità. L’abilità di servire in modo consistente, efficiente e 
   performante le richieste all'aumentare o al diminuire del loro numero. 
   È strettamente connessa al concetto di accessibilità;

-  Sicurezza. La sicurezza implica aspetti quali confidenzialità, 
   integrità, autorizzazione e autenticazione;

-  Transazionalità. Ci sono alcuni casi (ad es., API stateful) in cui 
   è necessario assicurare l’esecuzione transazionale di una operazione. 
   La capacità di una operazione di rispettare questa proprietà è parte 
   della QoS.

Gli erogatori di API devono prendere tutte le iniziative necessarie a 
mantenere i requisiti di QoS richiesti dal caso d’uso. Questo include 
anche l’utilizzo di buone pratiche, ad esempio, per assicurare prestazioni
e scalabilità, il risparmio della banda è una condizione fondamentale.


Service Level Agreement – SLA
-----------------------------

L’integrazione può coinvolgere numerose organizzazioni e erogatori 
esterni di API. Al fine di accordarsi sulla QoS, gli erogatori e i 
fruitori di API utilizzano quelli che vengono definiti Service Level 
Agreement (SLA), ovvero accordi sul livello di servizio. Un SLA può 
contenere le parti seguenti:

-  Scopo. Le ragioni che hanno portato alla definizione del SLA;

-  Parti. I soggetti interessati dal SLA e i rispettivi ruoli (ad es., 
   l’erogatore e il fruitore della API);

-  Periodo di validità. L’intervallo di tempo, espresso mediante data, 
   ora di inizio, data e ora di fine, per il quale si ritiene valido un 
   particolare termine di accordo all’interno degli SLA;

-  Perimetro. Quali sono operazioni interessate dallo specifico SLA;

-  Service Level Objectives (SLO), ovvero obiettivi sul livello di 
   servizio. I singoli termini di accordo all’interno di un SLA. Di 
   solito, sono definiti utilizzando dei Service Level Indicators (SLI), 
   ovvero indicatori sul livello di servizio, che quantificano i singoli 
   aspetti di QoS (ad es., la disponibilità);

-  Penalità. Le sanzioni che si applicano nel caso che l’erogatore 
   dell’interfaccia di servizio non riesca ad assicurare gli obiettivi 
   specificati nel SLA;

-  Esclusioni. Gli aspetti della QoS non coperti dal SLA;

-  Amministrazione. I processi mediante i quali le parti possono 
   monitorare la QoS.

Gli SLA possono essere statici o dinamici. Negli SLA dinamici, i SLO 
   (con associati SLI) variano nel tempo e i periodi di validità 
   definiscono gli intervalli di validità di questi ultimi (ad es., 
   in orario lavorativo i SLO possono essere differenti da quelli 
   imposti durante la notte). La misurazione dei livelli di QoS 
   all’interno di un SLA richiedono il tracciamento delle operazioni 
   effettuate in un contesto infrastrutturale multi-dominio (geografico, 
   tecnologico e applicativo). 


Dominio di interoperabilità
---------------------------

Nell’ambito delle presenti Linee Guida, per dominio di interoperabilità 
si indica uno specifico contesto in cui più Pubbliche Amministrazioni 
e/o soggetti privati hanno l’esigenza di scambiare dati e/o integrare 
i propri processi per dare seguito al disposto normativo.

Ogni dominio di interoperabilità è caratterizzato da:

-  i soggetti partecipanti, le Pubbliche Amministrazioni e gli eventuali 
   soggetti privati (cittadini e imprese);

-  i sistemi informatici dei soggetti partecipanti che scambiano dati 
   e/o integrano i propri processi;

-  l’insieme di API implementate per garantire le interazioni tra i 
   sistemi informatici dei soggetti partecipanti;

-  i criteri di sicurezza che le singole API forniscono per assicurare 
   transazioni tra i soggetti partecipanti conformi alla norma.

Logging
-------

Il logging riveste un ruolo fondamentale nella progettazione e nello 
sviluppo di API. Le moderne piattaforme middleware, oltre ad integrare 
meccanismi di logging interni, possono connettersi ad API esterne che 
permettono la raccolta (log collection), la ricerca e la produzione di 
analitiche, utili tra l’altro all’identificazione di problemi e al 
monitoraggio del sistema e della QoS. L’utilizzo di log collector 
permette di centralizzare non solo i log relativi all’utilizzo delle 
API, ma anche quelli di eventuali altri servizi digitali e componenti 
di rete (ad es., proxy e application-gateway). Ai fini di non ripudio, 
i messaggi applicativi possono essere memorizzati insieme alla firma 
digitale, ed archiviati nel rispetto della normativa sulla conservazione 
e sulla privacy. L’erogatore deve documentare in dettaglio il formato 
e le modalità di tracciatura, consultazione e reperimento delle 
informazioni. L’erogatore non deve tracciare nei log segreti quali 
password, chiavi private o token di autenticazione. L’erogatore deve 
tracciare un evento per ogni richiesta, contenente almeno i seguenti 
parametri minimi:

-  istante della richiesta;

-  identificativo del fruitore e dell’operazione richiesta;

-  tipologia di chiamata;

-  esito della chiamata;

-  ove applicabile, identificativo del consumatore o altro soggetto 
   operante la richiesta comunicato dal fruitore - è cura del fruitore
   procedere alla codifica e l'anonimizzazione, ove necessario;

-  ove applicabile, un identificativo univoco della richiesta, utile a 
   eventuali correlazioni.

Pattern e profili di interoperabilità
-------------------------------------

Le Linee Guida individuano:

-  pattern di interoperabilità, ovvero la definizione di una soluzione 
   a una esigenza di scambio di messaggi e informazioni, declinata in 
   una specifica tecnologia. Si suddividono in:

   -  pattern di interazione, puntualizzano le modalità tecniche per 
      implementare i modelli di scambio dei messaggi (anche detti
      message exchange patterns) [1]_, necessari all’interazione 
      tra i sistemi informatici di erogatori e fruitori;

   -  pattern di sicurezza, individuano le modalità tecniche per 
      assicurare che i pattern di interazione rispettino specifiche 
      esigenze di sicurezza (autenticazione e autorizzazione delle 
      parti, confidenzialità delle comunicazioni, integrità dei messaggi 
      scambiati, ...) negli scambi realizzati;

-  profili di interoperabilità, la combinazione di più pattern per 
   descrivere le esigenze di specifici domini di interoperabilità, 
   quale ad esempio il non ripudio delle comunicazioni e/o dei messaggi 
   scambiati.

**I pattern e profili di interoperabilità individuati nei Documenti 
operativi delle Linee Guida sono utilizzati dalle Pubbliche 
Amministrazioni nell’implementazione delle proprie API**. 

**Le Pubbliche Amministrazioni selezionano i pattern e/o i profili di 
interoperabilità sulla base delle specifiche esigenze del dominio di 
interoperabilità a cui partecipano**.

Catalogo delle API
------------------

Le Linee Guida individuano il Catalogo delle API (in breve, Catalogo) 
quale componente, unica e centralizzata, che assicura alle parti 
coinvolte nel rapporto di erogazione e fruizione la consapevolezza 
sulle API disponibili, e per esse, i livelli di servizio dichiarati.

La presenza del Catalogo è funzionale a:

-  facilitare l’interoperabilità tra le Pubbliche Amministrazioni e i 
   soggetti privati interessati;

-  contenere la spesa delle Pubbliche Amministrazioni, riducendo la 
   replicazione di API;

-  assicurare la dichiarazione degli SLO da parte dell'erogatore sulle 
   singole API pubblicate;

-  manifestare, ove presenti, gli impegni tra erogatori e fruitori 
   relativi all'utilizzo delle API (SLA).

Il Catalogo, fatti salvi i principi comuni che saranno emanati 
dall’Agenzia per l’Italia Digitale, al fine di normalizzare le tecnologie 
utilizzate a livello nazionale, tiene conto della:

-  Specificità dei territori e dei diversi ambiti entro cui le Pubbliche 
   Amministrazioni operano attraverso la determinazione di specializzazioni 
   dei contenuti del Catalogo, prevedendo aggregazioni di API a livello 
   territoriale (ad es. su base regionale) e/o relativamente agli ambiti 
   tematici entro cui le Pubbliche Amministrazioni operano (ad es. 
   giustizia). Tale scelta è ulteriormente giustificata dalla opportunità 
   di favorire momenti di aggregazione di soggetti omogenei che determini 
   la creazione di API comuni, nonché la condivisione di metodologie per 
   la loro progettazione e il loro sviluppo.

-  Esigenza di assicurare la governance del Catalogo, quale presupposto 
   per garantire una semantica univoca e condivisa, per evitare ridondanze 
   e/o sovrapposizioni in termini di competenze e contenuti (de-duplicazione).

-  Esigenza di assicurare una descrizione formale delle API che, 
   attraverso l’utilizzo degli Interface Description Language (IDL) 
   indicati, permetta di descrivere le API indipendente dal linguaggio 
   di programmazione adottato dall’erogatore e dai fruitori.

Governance del modello
----------------------

L’Agenzia per l’Italia Digitale è responsabile delle attività di 
governance del ModI con l’obiettivo di definire, condividere e assicurare 
l’aggiornamento continuo dei seguenti aspetti:

-  l’insieme delle tecnologie che abilitano l’interoperabilità tra le 
   Pubbliche Amministrazioni, cittadini e imprese;

-  i pattern di interoperabilità (interazione e sicurezza);

-  i profili di interoperabilità.

Il rapporto tra fruitori ed erogatori è reso esplicito tramite il 
Catalogo. In ottemperanza al principio once-only definito nell’EU 
eGovernment Action Plan 2016-2020, l’erogatore si impegna a fornire 
l’accesso alle proprie API a qualunque soggetto che ne abbia diritto e 
ne faccia richiesta. Gli erogatori DEVONO descrivere i propri e-service 
classificando le informazioni scambiate (ove possibile collegandole ai 
vocabolari controllati e a concetti semantici definiti a livello nazionale 
e/o internazionale), e applicando etichette che ne identifichino la 
categoria.

Un erogatore può delegare la registrazione degli e-service all’interno 
del Catalogo ad un’altra Amministrazione, denominata ente capofila, 
relativamente a specifici contesti territoriali e/o ambiti tematici.

In prima istanza si prevede che gli enti capofila possano essere:

-  a livello territoriale, le Regioni per le Pubbliche Amministrazioni 
   Locali del territorio di riferimento;

-  a livello di ambito, le Pubbliche Amministrazioni Centrali per domini 
   di interoperabilità costituiti per specifici ambiti tematici.

Il ModI opera in assenza di elementi centralizzati che mediano 
l’interazione tra erogatori e fruitori. Il Catalogo delle API permette 
ai soggetti pubblici e privati di conoscere gli e-service disponibili 
e le loro modalità di erogazione e fruizione.

L’Agenzia per l’Italia Digitale ha il ruolo di:

-  recepire le esigenze di interoperabilità delle Pubbliche 
   Amministrazioni, astrarle ed eventualmente formalizzare nuovi 
   pattern e/o profili di interoperabilità;

-  coordinare il processo di definizione dei profili e pattern di 
   interoperabilità;

-  rendere disponibile il Catalogo, attraverso un’interfaccia di 
   accesso unica per permettere a tutti i soggetti interessati, 
   pubblici e privati, di assumere consapevolezza degli e-service 
   disponibili;

-  richiedere l'adozione dei pattern e profili di interoperabilità per 
   l’implementazione delle API quale condizione per l’iscrizione al 
   Catalogo, nonché controllare con continuità il rispetto dei requisiti 
   per l’iscrizione al catalogo.

.. [1]
   Cf. https://en.wikipedia.org/wiki/Messaging_pattern

.. forum_italia::
   :topic_id: 21436
   :scope: document
