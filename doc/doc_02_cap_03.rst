SOAP
====

Il protocollo SOAP (Simple Object Access Protocol) è stato sviluppato per superare le limitazioni imposte dai protocolli precedenti per l'interazione distribuita basata su oggetti (CORBA, Java/RMI, DCOM) relative alla distribuzione a livello Internet delle macchine interessate ed ai vincoli imposti dal punto di vista delle tecnologie di implementazione.

La versione corrente della specifica `SOAP è la 1.2 del 27 aprile 2007 <https://www.w3.org/TR/soap12-part1/>`_  [45]_. La specifica definisce due stili di comunicazione (communication modes):

  - quello basato su chiamata a procedura (RPC-like), 

  - e quello basato su scambio di documenti (document style). 
 
In combinazione ad essi, il protocollo definisce delle modalità di scambio dell'informazione: 

  - interazioni one-way (dal client al server), 
  
  - interazioni request/response, 
  
  - invio di notifiche (interazione one-way dal server al client) 
  
  - e solicit/response (interazione request/response in cui la request è inviata dal server). 

  Le ultime due modalità sono poco utilizzate in pratica e fuori dai profili di interoperabilità standard, quindi il loro utilizzo è vietato.

Il protocollo SOAP definisce tre componenti fondamentali:

-   una envelope (letteralmente "busta da lettere") che definisce la struttura del messaggio e come processarlo;

-   un insieme di regole di codifica per esprimere istanze di tipi di dato definiti a livello applicativo;

-   una convenzione per rappresentare lo stile di interazione RPC.

La definizione del protocollo è pensata per essere indipendente dal protocollo sottostante. In particolare, SOAP può operare (tramite i cosiddetti binding) su diversi protocolli di trasporto inclusi HTTP, SMTP, TCP, UDP o JMS. Sebbene implementazioni sono state proposte per ognuno di questi casi (in special modo JMS per interazioni asincrone), il mercato ha premiato principalmente soluzioni sincrone basate su HTTP.

Una delle caratteristiche che contraddistinguono il protocollo SOAP è la sua estensibilità. In particolare si indica con WS-\* lo stack di estensioni costruite su SOAP, molte delle quali hanno avuto grande successo in termini di implementazioni disponibili. Queste estensioni permettono di avere su SOAP una serie di funzionalità che su altri protocolli devono essere costruite ad hoc. Lo svantaggio di questa soluzione è che il protocollo introduce un overhead di processamento che fa preferire altre soluzioni in determinati contesti.

Tra le estensioni supportate dai framework più diffusi abbiamo:

-   WS-Addressing è un modo standard per includere informazioni circa l'instradamento dei messaggi (ad es., l'interfaccia di servizio a cui inviare la risposta o da contattare in caso di errore).

-   WS-Security è la specifica che descrive le politiche di sicurezza implementate a livello applicativo dalle interfacce di servizio. In particolare, WS-Security include meccanismi per autenticazione e autorizzazione, confidenzialità, integrità e firma digitale.

-   WS-Trust è una estensione a WS-Security che permette di richiedere, rinnovare e validare token di sicurezza. Permette inoltre di verificare la relazione di mutua fiducia su un canale sicuro.

-   WS-Federation è una estensione che permette a differenti domini di sicurezza di scambiare informazioni circa identità, attributi di autorizzazione ed autenticazione.

-   WS-ReliableMessaging permette di consegnare in maniera affidabile (ad es., nell'ordine corretto) messaggi SOAP in presenza di problemi di rete e di inattività di componenti software e di sistema.

-   WS-AtomicTransaction è una estensione che permette di ottenere la proprietà tutto o niente per un gruppo di operazioni. Essa definisce tre protocolli (completamento, two-phase commit volatile e two-phase commit durevole) che sono implementati dal framework

-   WS-Coordination.

-   WS-Choreography è la specifica per la definizione di coreografie. Una coreografia specifica i passi relativi allo scambio di messaggi tra diversi soggetti che si integrano.

-   WS-BPEL è la specifica per la definizione di orchestrazioni.

-   WS-Coordination è un framework estensibile per il coordinamento di web service (corrispondenti alle interfacce di servizio). In particolare esso spiega come implementare (e quindi è preso a riferimento dalle varie implementazioni dello stack WS-\*) i protocolli di coordinamento inclusi quelli descritti da WS-AtomicTransaction.

La specifica delle interfacce di servizio SOAP è effettuata tramite `Web Services Description Language - WSDL <https://www.w3.org/TR/wsdl20-primer/>`_ [46]_. Oltre ad indicare le funzionalità offerte dall'interfaccia di servizio dal punto di vista funzionale, esso permette anche di definire le caratteristiche non funzionali tramite le estensioni `WS-Policy <https://www.w3.org/TR/ws-policy/>`_ [47]_ che permettono di specificare le varie componenti della QoS.

Indicazioni di utilizzo
-----------------------

La specifica SOAP permette la definizione di specifici profili di interoperabilità, imponendo alcune restrizioni circa i tipi ed i formati scambiati. Il profilo di interoperabilità secondo il quale interfacce di servizio di tipo SOAP andranno implementate è la `versione 2.0 del Basic Profile <http://docs.oasis-open.org/ws-brsp/BasicProfile/v2.0/cs01/BasicProfile-v2.0-cs01.html>`_ [48]_ (nel seguito BP2) definito dal WS-I (Web Services Interoperability Organization) ed ora confluito in OASIS. BP2 è basato su SOAP 1.2 e WS-Addressing (per il dispatching dei messaggi a livello applicativo, in particolare nel caso di interazioni asincrone). Tra le molte indicazioni, BP2 definisce anche la modalità di gestione degli errori. In particolare, oltre all'utilizzo dei codici di errore HTTP si richiede che il ricevente sia in grado di gestire le SOAP fault [49]_ che quindi devono, obbligatoriamente, essere emesse dall'erogatore a fronte di errori.

Sicurezza
---------

Per quanto riguarda la sicurezza, l'ultimo profilo standard definito da OASIS è il `Basic Security Profile 1.1 <http://www.ws-i.org/Profiles/BasicSecurityProfile-1.1.html>`_ [50]_. Il profilo è datato ma le considerazioni sono ancora valide. Per quanto riguarda le versioni dei protocolli, si devono rispettare i vincoli imposti dal Modello di Interoperabilità 2018 in questo documento.

È importante, nel caso si richiedessero funzionalità di autorizzazione, autenticazione e non ripudio, oltre che di riservatezza (coperta dall'utilizzo obbligatorio di HTTPS [51]_) fare affidamento alle tecnologie di autenticazione ed autorizzazione a livello applicativo. Il Basic Security Profile 1.1, basato sull'estensione WS-Security, suggerisce l'uso di SAML 2.0. Come detto, rispetto alle tecnologie di autenticazione ed autorizzazione, ci sono alcuni domini applicativi per i quali OAuth2 o OpenID sono più appropriati. In questi ultimi casi, fermo restando l'utilizzo della XML Signature definita in WS-Security per quanto riguarda il non ripudio, l'utilizzo di token di autorizzazione ed autenticazione non SAML richiede la definizione di `request header custom <https://developers.google.com/adwords/api/docs/guides/call-structure>`_ [52]_.

Uniformità e naming
-------------------

Non esistono standard riguardanti il naming in ambito SOAP. Le best-practice prevedono l'utilizzo di `CamelCase <https://it.wikipedia.org/wiki/Notazione_a_cammello>`_ [53]_ (con prima lettera maiuscola, anche noto come PascalCase) per endpoint, porte, operazioni e parametri.

Quando le risorse contengono link e riferimenti a risorse esterne, si dovrebbero usare le specifiche indicate in `IANA registered link relations <http://www.iana.org/assignments/link-relations/link-relations.xml>`_ [54]_ trasformando il `Kebab Case <https://it.wikipedia.org/wiki/Kebab_case>`_ [55]_ utilizzato con il CamelCase.


.. discourse::
   :topic_identifier: 3237

	

.. [45] Cf. `https://www.w3.org/TR/soap12-part1/ <https://www.w3.org/TR/soap12-part1/>`_

.. [46] Cf. `https://www.w3.org/TR/wsdl20-primer/ <https://www.w3.org/TR/wsdl20-primer/>`_

.. [47] Cf. `https://www.w3.org/TR/ws-policy/ <https://www.w3.org/TR/ws-policy/>`_

.. [48] Cf. `http://docs.oasis-open.org/ws-brsp/BasicProfile/v2.0/cs01/BasicProfile-v2.0-cs01.html <http://docs.oasis-open.org/ws-brsp/BasicProfile/v2.0/cs01/BasicProfile-v2.0-cs01.html>`_

.. [49] Le SOAP fault devono essere accompagnate anch’esse da un appropriato codice di errore HTTP. Per SOAP fault comuni si può fare riferimento a 'https://www.w3.org/TR/2007/REC-soap12-part2-20070427/#tabresstatereccodes' <https://www.w3.org/TR/2007/REC-soap12-part2-20070427/#tabresstatereccodes>_.

.. [50] Cf. `http://www.ws-i.org/Profiles/BasicSecurityProfile-1.1.html <http://www.ws-i.org/Profiles/BasicSecurityProfile-1.1.html>`_

.. [51] HTTPS è richiesto dal modello di interoperabilità ma non da BP2.

.. [52] Cf. `https://developers.google.com/adwords/api/docs/guides/call-structure <https://developers.google.com/adwords/api/docs/guides/call-structure>`_

.. [53] Cf. `https://it.wikipedia.org/wiki/Notazione\_a\_cammello <https://it.wikipedia.org/wiki/Notazione_a_cammello>`_

.. [54] Cf. `http://www.iana.org/assignments/link-relations/link-relations.xml <http://www.iana.org/assignments/link-relations/link-relations.xml>`_

.. [55] Cf. `https://it.wikipedia.org/wiki/Kebab\_case <https://it.wikipedia.org/wiki/Kebab_case>`_

