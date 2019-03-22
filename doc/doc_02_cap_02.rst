Concetti di Sicurezza
=====================

La sicurezza dei sistemi informatici è l'insieme di pratiche messe in atto al fine di impedire l'accesso non autorizzato, l'uso, la divulgazione, l'interruzione dell'accesso, la modifica, l'ispezione e la distruzione delle informazioni.

Questa sezione si concentra sui meccanismi di sicurezza che vadano oltre il semplice filtraggio di pacchetti basato su indirizzi IP, tipo di protocollo (anche detto circuit-level filtering) o contenuto del dato applicativo (application-level gateway o antivirus) [25]_. In particolare la sezione si concentra sull'utilizzo di protocolli e tecniche di sicurezza basate sulla manipolazione dei messaggi di rete. La sezione farà inoltre riferimento a come i requisiti di sicurezza possano essere variabili a seconda dello scenario applicativo e del caso d'uso.

Meccanismi di base
------------------

Diversi sono i concetti chiave dietro al mondo della sicurezza. In origine il termine faceva riferimento al concetto di triade CIA (Confidenzialità, Integrità e Availability - Disponibilità). Nel tempo altri concetti si sono aggiunti quali l'autenticazione e il non ripudio.

Questa sezione descrive questi concetti introducendo le principali tecniche impiegate per assicurarli. 

Disponibilità
^^^^^^^^^^^^^

Il concetto di disponibilità è stato introdotto nella Sezione 1.3 parlando della QoS. Il concetto di disponibilità è legato strettamente anche a quello di sicurezza, poiché la disponibilità di una interfaccia di servizio può essere legata non solo a cause di natura tecnica ma anche a specifici tipi di attacco (ad es., denial of service).

Confidenzialità
^^^^^^^^^^^^^^^
Con il termine confidenzialità si intende la protezione dei dati e delle informazioni scambiate tra un mittente e un destinatario. La confidenzialità, declinata per il canale di comunicazione, è la proprietà di assicurare che l’informazione scambiata tra due entità colloquianti in rete non possa essere acceduta da soggetti terzi. 

La confidenzialità è ottenuta tramite la cifratura dei dati e delle informazioni (sicurezza di messaggio) o del canale di comunicazione (sicurezza del canale).

In un metodo di cifratura, un messaggio in chiaro (anche chiamato plain text) viene trasformato in un messaggio codificato e viceversa. Gli algoritmi di cifratura si distinguono in meccanismi a chiave simmetrica (o privata o condivisa) e chiave asimmetrica (o pubblica). In entrambi i casi la lunghezza delle chiavi influenza la sicurezza della comunicazioni (chiavi più lunghe sono più sicure) perché proteggono maggiormente da attacchi a forza bruta. Si suppone infatti che ogni meccanismo di cifratura possa essere rotto tramite enumerazione a patto che il tempo necessario (esponenziale nella lunghezza della chiave) non sia troppo lungo rispetto agli scopi dell'attaccante. Un'altra tipologia di attacco ai metodi di cifratura (che si applica in particolar modo ai metodi a chiave simmetrica in cui le password sono generate da umani) sono quelli di tipo dizionario, basati sull'uso di parole di uso comune.

Nei meccanismi di cifratura a chiave privata, entrambe le parti (il mittente ed il destinatario) nel canale di comunicazione condividono la stessa chiave di cifratura che viene impiegata sia per cifrare che per decifrare il messaggio. La cifratura a chiave simmetrica è molto efficiente e viene utilizzata per la riservatezza di grandi quantità di dati (ad es., interi file). È necessario che le due parti abbiano condiviso la chiave privata con un metodo sicuro (ad es., scambiandola fisicamente di persona oppure tramite un meccanismo di cifratura a chiave pubblica, come si vedrà nella Sezione 2.4). Algoritmi noti di cifratura a chiave simmetrica sono RC4, DES, Triple DES, AES, IDEA e Camellia.

Nei meccanismi di cifratura a chiave pubblica, vengono utilizzate due chiavi diverse per la cifratura e la decifratura dei messaggi. In particolare si supponga che il destinatario abbia una coppia di chiavi di cui una è privata (conosciuta solo al destinatario) ed una è pubblica (conosciuta a tutti e liberamente inviata sulla rete anche in chiaro). Al fine di inviare un messaggio su di un canale sicuro, il mittente cifra il messaggio utilizzando la chiave pubblica del destinatario, ma questo potrà essere decifrato solo dal destinatario utilizzando la chiave privata. Per il destinatario infatti chiave pubblica e chiave privata sono state generate in modo da essere complementari. Il meccanismo a chiave pubblica risolve il problema della condivisione delle chiavi poiché la chiave pubblica può essere inviata su Internet senza pericolo (non può essere utilizzata per decifrare il
messaggio). Come difetto, la crittografia a chiave pubblica soffre di basse prestazioni e per questo motivo viene utilizzata o nelle fasi preliminari necessarie a concordare una chiave privata di sessione condivisa (come nel caso di TLS) oppure per i meccanismi di firma digitale (quindi non a scopo di cifratura). L'algoritmo più diffuso per la cifratura a chiave pubblica è RSA (dai nomi degli inventori Rivest, Shamir e Adleman).

Integrità e Firma Digitale
^^^^^^^^^^^^^^^^^^^^^^^^^^

Un messaggio in transito su una rete informatica può subire delle modifiche (ad esempio tramite attacchi di tipo man-in-the-middle). I meccanismi a chiave pubblica possono essere utilizzati ai fini di produrre delle prove, dette firme digitali, utili a verificare che il messaggio ricevuto sia uguale a quello inviato.

Il meccanismo di firma digitale prevede di inviare assieme al messaggio, un secondo messaggio (detto firma digitale) ottenuto dal primo:

-   calcolando un riassunto (digest) del messaggio tramite tecniche cosiddette di hashing;

-   cifrando il riassunto utilizzando la chiave privata del mittente.

Le tecniche di hashing utilizzate per la firma digitale sono progettate secondo diversi criteri. Tra cui:

-   devono essere funzioni cosiddette one-way. Deve cioè essere facile calcolare il riassunto ma difficile risalire dal riassunto al testo originale. Questo viene anche facilitato dal fatto che i riassunti hanno solitamente lunghezza fissa;

-   devono fare sì che piccolissime modifiche al messaggio in input generino significative differenze nel riassunto.

La tecnica di hashing più utilizzata per la firma digitale è Secure Hash Algorithm - SHA (disponibile in diverse versioni). Nel momento in cui un messaggio viene ricevuto, il destinatario utilizza la chiave pubblica
del mittente per decifrare la firma digitale e verificare che essa corrisponda al riassunto del messaggio. La combinazione di tecniche di hashing e di cifratura a chiave pubblica assicura che un attaccante non
possa modificare il messaggio e generare una firma valida per lo stesso, assicurando quindi l'integrità del messaggio stesso.

Non Ripudio e Public Key Infrastructure - PKI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il meccanismo di firma digitale descritto in Sezione 2.1.3 assicura l'integrità del messaggio ma non ne assicura l'autenticità della fonte. In pratica, chi riceve un messaggio è sicuro che esso non ha subito modifiche durante il transito ma non è sicuro dell'identità del mittente. Il messaggio ricevuto non potrà quindi essere utilizzato ai fini del non ripudio, cioè come prova che uno specifico soggetto è il vero mittente del messaggio. Il problema principale risiede nella maniera in cui la chiave pubblica di un soggetto viene distribuita.
Essa, come detto, viene posta pubblicamente su Internet ma niente vieta ad un attaccante di creare una coppia chiave pubblica / chiave privata e distribuire quest'ultima fingendosi un altro soggetto ed inviare per conto di questo, in maniera fraudolenta, dei messaggi. In altre parole chi riceve il messaggio non ha modo di verificare l'autenticità della chiave pubblica che sta utilizzando. A tal fine il meccanismo introdotto è quello della Public Key Infrastructure - PKI.

Nella PKI oltre al mittente ed al destinatario del messaggio, viene aggiunta una terza parte detta Certification Authority (Autorità di Certificazione) la quale emette dei certificati. Un certificato è un documento in chiaro contenente informazioni riguardanti l'identità dell'intestatario del certificato e la sua chiave pubblica e viene firmato dalla certification authority utilizzando la propria chiave privata.

La chiave pubblica della certification authority è installata nei sistemi operativi (e distribuita solitamente tramite gli aggiornamenti degli stessi), viene utilizzata per verificare che la chiave pubblica del mittente sia autentica. Il mittente invia assieme al messaggio firmato il suo certificato che viene validato utilizzando la chiave pubblica della certification authority che ha emesso il certificato stesso.

Il meccanismo PKI è sicuro fino a quando un attaccante non è in grado di installare sulle macchine del destinatario una public key fasulla per le certification authority. Per ovviare a questi problemi sono necessari dei meccanismi di sicurezza a livello di macchina che sono fuori dal perimetro di questo documento. Lo standard comunemente usato per i certificati è X.509.

Nel Modello di Interoperabilità, le amministrazioni dovranno acquistare certificati commerciali. Negli ultimi anni alternative all'approccio PKI sono state proposte (ad es., Web of Trust) ma il Modello attualmente ne vieta l'utilizzo.

Autenticazione
^^^^^^^^^^^^^^

In un ambiente di calcolo distribuito, l'autenticazione è il meccanismo tramite il quale client e erogatore accertano le identità degli specifici utenti e sistemi per conto dei quali stanno operando. Quando la prova di autenticazione è bidirezionale si parla di mutua autenticazione.

L'autenticazione è spesso ottenuta in due fasi:

1.  Si definisce un contesto di autenticazione effettuando una chiamata ad una entità di autenticazione diversa dall'erogatore;

2.  Il contesto di autenticazione è impiegato per autenticarsi con l'altra parte della comunicazione.

Si noti come il meccanismo di non ripudio basato su PKI e firma digitale presentato in Sezione 2.1.4 sia un metodo di autenticazione ed in tal modo è usato in protocolli di strato di trasporto quali TLS (vedi Sezione 2.4) al fine di garantire non ripudio. Esistono poi dei protocolli di autenticazione a livello applicativo che forniscono dei vantaggi rispetto all'autenticazione basata su PKI: 

-   L'autenticazione basata su PKI solitamente non autentica solo i soggetti ma anche le macchine coinvolte (ad es., il certificato di un sito Internet contiene anche i nomi DNS su cui il sito risponderà);

-   Possibilità di Single-Sign On - SSO. Il contesto di autenticazione definito con protocolli di strato applicativo può essere riutilizzato nell'interazione con diverse interfacce di servizio. Questo è dovuto al fatto che il client assume l'identità della persona o del soggetto per cui è stato creato il contesto di autenticazione;

-   L'utilizzo di certificati è scomodo per l'utente finale e questo rende la mutua autenticazione basata su firma digitale meno adatta ai casi in cui siano utenti umani ad autenticarsi;

-   Non sempre la funzionalità di non ripudio è richiesta e l'uso di certificati lato client risulta costoso.

A seconda dell'interfaccia di servizio utilizzata, l'autenticazione può essere debole o forte. Per autenticazione forte si intende una autenticazione che richiede almeno due fattori (ad es., nome utente/password e one-time password - OTP). I protocolli per autenticazione ed autorizzazione a livello applicativo più diffusi sono oggetto della Sezione 2.3.

Autorizzazione
^^^^^^^^^^^^^^

I meccanismi di autorizzazione in ambienti distribuiti definiscono quali risorse possono essere accedute da uno specifico utente. Tipiche politiche di autorizzazione permettono l'accesso a specifiche collezioni a specifici gruppi di utenti autenticati sulla base di ruoli, gruppi e privilegi. L'autenticazione degli utenti è quindi una componente fondamentale nell'autorizzazione anche se i requisiti di autenticazione (forte o debole) possono cambiare a seconda del protocollo. Le politiche di autorizzazione sono le più svariate e possono interessare ad esempio l'ora del giorno in cui specifici utenti possono accedere a specifiche risorse oppure il rate massimo di chiamate concesse ad un utente.

Minacce alla sicurezza dei sistemi informatici
----------------------------------------------

Nelle sezioni precedenti alcune minacce alla sicurezza sono state accennate. In questa sezione approfondiamo le diverse tipologie di attacchi. Non ci soffermeremo sugli attacchi basati su malware, ma ci limiteremo agli attacchi basati sull'uso dei protocolli di rete. I tipi di attacchi più comuni sono i seguenti:

-   *Eavesdropping*. È un tipo di attacco passivo (senza modifica dei dati) in cui un attaccante riesce a rubare informazioni leggendo dati da una connessione non cifrata. I protocolli che assicurano confidenzialità difendono da questo tipo di attacco.

-   *Modifica dei dati*. Un attaccante potrebbe riuscire a modificare i pacchetti in transito nella rete. I meccanismi di firma digitale difendono da questo tipo di attacco.

-   *Identity spoofing*. In questo tipo di attacco, l'attaccante finge di essere un altro utente. Questo tipo di attacco è risolto mediante meccanismi di autenticazione.

-   *Attacchi su base password*. In questo caso l'attaccante cerca di ottenere delle password, utilizzate ad esempio ai fini di autenticazione ed autorizzazione. Come già anticipato, gli attacchi basati su password si basano o su forza bruta oppure su metodi di tipo dizionario. Questo tipo di attacchi si evitano impostando politiche forti riguardo alle password utilizzate e metodi di autenticazione forte (a più fattori).

-   *Denial of service - DoS*. In questo tipo di attacco l'attaccante mira a rendere non operativa una interfaccia di servizio inondandola di richieste e minandone quindi l'accessibilità. Difendersi da questi tipi di attacchi è in genere molto difficile (specialmente nella variante distribuita DDoS).

-   *Attacchi man-in-the-middle*. In questo caso un attaccante si intromette come terza parte in una conversazione tra mittente e destinatario modificando i messaggi scambiati. Gli attacchi man-in-the-middle si combattono tramite tecniche di cifratura ed integrità degli scambi.

In alcuni casi, gli attaccanti possono sfruttare delle falle scoperte nei protocolli o nelle implementazioni. È quindi di fondamentale importanza tenere aggiornati i sistemi ed utilizzare quando possibile versioni aggiornate dei protocolli.

Protocolli per autenticazione e autorizzazione
----------------------------------------------

Nel caso di autenticazione ed autorizzazione, occorre distinguere gli approcci utilizzati nello scenario human-to-machine e quelli utilizzati nello scenario machine-to-machine. I protocolli più comuni in ambito Web per autenticazione ed autorizzazione nel caso human-to-machine sono:

-   `OAuth2 <https://tools.ietf.org/html/rfc6749>`_ [26]_ è uno standard per l'autorizzazione;

-   `OpenID <http://openid.net/developers/specs/>`_ [27]_ è uno standard pensato per la sola autenticazione. L'ultima versione, denominata `OpenID Connect <http://openid.net/connect/>`_ [28]_, è costruita su OAuth2 in termini di scambio di messaggi;

-   Security Assertion Markup Language - `SAML <http://saml.xml.org/saml-specifications>`_ [29]_ (la versione corrente è la 2) è il protocollo più vecchio in circolazione e copre l'autenticazione e in parte l'autorizzazione;

-   eXtensible Access Control Markup Language - `XACML <http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html>`_ [30]_ complementare a SAML per la gestione esaustiva degli aspetti di autorizzazione.

Nei protocolli human-to-machine, un client riceve autorizzazioni ad usare un certo tipo di risorsa per conto di un utente umano tramite le credenziali di quest'ultimo. La richiesta del token/assertion è effettuata per mezzo di uno user-agent (cioè un browser o una app mobile) che funge da intermediario.

Il ModI obbliga all'utilizzo di SPID per l'autenticazione human-to-machine o degli altri metodi indicati nell\'`art. 64 del Codice per l'Amministrazione Digitale <http://www.agid.gov.it/cad/art-64-sistema-pubblico-gestione-identita-digitali-modalita-accesso-ai-servizi-erogati-rete>`_ [31]_ che includono anche la Carta d'Identità Elettronica - CIE e la Carta Nazionale dei Servizi - CNS. 

`SPID <http://spid-regole-tecniche.readthedocs.io/en/latest/>`_ [32]_ è attualmente basato su SAML ma il supporto per OpenID Connect è in fase di definizione al fine di supportare in maniera più semplice l'autenticazione da piattaforme mobili.

In questo senso vale la pena esplorare le differenze principali tra SAML ed OpenID Connect (in breve Connect). Dal punto di vista della terminologia i due protocolli utilizzano termini differenti per gli stessi componenti:

-   Identity Provider (SAML) o OpenID Provider (Connect) sono le entità che certificano l'identità dell'utente;

-   Service Provider (SAML) o Relying Party (Connect) sono le interfacce di servizio, le app mobili o i siti presso cui l'utente vuole autenticarsi;

-   Asserzioni (SAML) o Token (Connect) sono dei documenti firmati dall'Identity Provider (SAML) o dall'OpenID Provider (Connect) che contengono le informazioni circa l'utente identificato e le autorizzazioni che possiede.

La tabella seguente riassume le caratteristiche dei protocolli per l'interazione human-to-machine:

+-----------------------------+---------------------+--------------------------------+
|                             | **OpenID Connect**  | **SAML + XACML**               |
+-----------------------------+---------------------+--------------------------------+
| **Formato token/assertion** |  JSON               |  XML                           |
+-----------------------------+---------------------+--------------------------------+
| **Autorizzazione**          |                     |  ✓                             |
+-----------------------------+---------------------+--------------------------------+
| **Autenticazione**          |  ✓                  |  ✓                             |
+-----------------------------+---------------------+--------------------------------+
| **Rischi per la sicurezza** |  Phishing [33]_     |   XML Signature Wrapping [34]_ |
+-----------------------------+---------------------+--------------------------------+

Uno scenario interessante nell'ambito dell'integrazione A2A e A2B è quello legato alla federazione di domini (ad es., due diverse amministrazioni) in cui alcuni utenti di un dominio devono essere autenticati ed autorizzati per accedere a risorse dell'altro dominio (una federazione può includere anche più di due domini). In ambito SOAP, gli standard più utilizzati sono `WS-Federation <http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation-1.2-spec-os.html>`_ [35]_ & `WS-Trust <http://docs.oasis-open.org/ws-sx/ws-trust/v1.4/ws-trust.html>`_ [36]_ (vedi Sezione 3 per l'inquadramento nello stack WS-\*). Soluzioni su altre tecnologie vengono sviluppate ad hoc.

Per quanto riguarda lo scenario machine-to-machine invece, come si vedrà nella sezione 2.4, l'autenticazione può avvenire a livello di trasporto utilizzando TLS.

Per quanto riguarda l'autorizzazione machine-to-machine invece è possibile utilizzare il protocollo OAuth2 nello specifico del flusso `Client Credential Grant <https://tools.ietf.org/html/rfc6749#section-4.4>`_ [37]_. Tale flusso a differenza di quello standard non richiede la presenza di uno user-agent. Il client possiede invece delle proprie credenziali che vengono utilizzate per richiedere il token all'authorization server.

Protocolli per integrità e confidenzialità
------------------------------------------

Per ragioni storiche lo stack TCP/IP non ha di base funzionalità di sicurezza. I messaggi viaggiano in chiaro sulla rete. Poiché le tecnologie per l'integrazione che verranno introdotte utilizzano HTTP come principale protocollo di trasporto o applicativo [38]_, è importante che il canale di comunicazione sia protetto. La IETF definisce come standard per la securizzazione di TCP il protocollo Transport Layer Security - TLS. Con il termine HTTPS si definisce l'utilizzo di HTTP su canale TLS. Tutte le interfacce di servizio esposte nel ModI devono essere basate su HTTPS. Il protocollo TLS (ed il suo predecessore deprecato Secure Sockets Layer - SSL) assicurano su TCP confidenzialità (tramite cifratura) ed integrità (tramite firma digitale e PKI). Come introdotto in Sezione 2.1.5, il meccanismo di firma digitale assicura anche autenticazione ma questa è fatta machine-to-machine.

Il protocollo TLS (versione stabile corrente 1.2, draft 1.3 presentato a marzo) si basa come detto sull'utilizzo della firma digitale per lo scambio di una chiave di sessione da utilizzare come chiave simmetrica.

Per quanto riguarda i singoli algoritmi utilizzati:

-   Per lo scambio della chiave di sessione, TLS supporta numerose tecniche. Tra quelle proposte, si impone l'uso di tecniche che evitano attacchi man-in-the-middle e forniscono la cosiddetta forward secrecy (cioè che la scoperta di una chiave privata usata nello scambio non permette di scoprire la chiave di sessione). Gli algoritmi di scambio delle chiavi permessi sono quindi ephemeral Diffie--Hellman - DHE ed ephemeral Elliptic Curve Diffie--Hellman - ECDHE.

-   Per la cifratura TLS supporta numerosi algoritmi. Si suggeriscono i protocolli attualmente supportati nello standard TLS 1.3 e che sono considerati sicuri: Advanced Encryption Standard - AES (nella versioni GCM e CCM).

-   Per l'integrità si suggerisce l'uso di SHA almeno a 256 bit (quindi a partire dal cosiddetto SHA-2).

+-----------------------------------------------------------------------+
| Nel Modello di Interoperabilità, a prescindere dal profilo di         |
| autenticazione ed autorizzazione scelta (che dipende dal caso d'uso), |
| il protocollo di trasmissione:                                        |
|                                                                       |
| -   DEVE essere basato su HTTP \>= 1.1;                               |
|                                                                       |
| -   DEVE essere cifrato tramite TLS \>= 1.2;                          |
|                                                                       |
| -   DEVE essere firmato con SHA-256 o superiore                       |
|                                                                       |
| -   DEVE essere conforme alle misure minime AgID Basic Security       |
|     Controls [41]_;                                                   |
|                                                                       |
| -   Gli erogatori di interfacce di servizio DEVONO utilizzare         |
|     l\'header HSTS (HTTP Strict Transport Security) per evitare       |
|     attacchi di tipo SSL Strip (tipo di attacco Man-in-the-middle).   |
|                                                                       |
| Inoltre, ogni certificato TLS utilizzato per erogare interfacce di    |
| servizio:                                                             |
|                                                                       |
| -   NON DEVE essere self-signed (ad es., CA:true);                    |
|                                                                       |
| -   DEVE contenere i seguenti elementi: Subject, Key Identifier,      |
|     Serial Number ed Issuer;                                          |
|                                                                       |
| -   DEVE avere il parametro keyUsage_ con i seguenti bit:             |
|     `digitalSignature, keyEncipherment` [42]_;                        |
|                                                                       |
| -   DOVREBBE contenere i riferimenti al DNS dei domini serviti;       |
|                                                                       |
| -   Un certificato usato ai fini di non ripudio DEVE avere inoltre il |
|     parametro keyUsage con il bit nonRepudiation settato.             |
+-----------------------------------------------------------------------+

Numerose sono le minacce alla sicurezza a cui è esposto TLS (in special modo con vecchie versioni del protocollo accoppiate ad algoritmi per cifratura ed integrità vulnerabili). L'IETF nel 2015 ha rilasciato a riguardo una RFC informativa [43]_. Per questo motivo, in determinati scenari che richiedono elevati standard di sicurezza, si aggiunge talvolta un ulteriore strato di sicurezza a livello applicativo.

Nel modello SPCoop si richiedeva che in ogni caso HTTPS fosse utilizzato con autenticazione mutual-TLS (vedi Sezione 2.3). Nel tempo sono emersi scenari di interazione con requisiti di sicurezza inferiori (ad es., solo HTTPS non-mutual-TLS), che non giustificano la complessità di un sistema a mutua autenticazione (ad es., accessi in sola consultazione, applicazioni Web o sistemi IoT [44]_) a livello di trasporto. Fermo l'obbligo di usare HTTPS, nasce l'esigenza di venire incontro a diversi scenari e definire per essi modelli di autenticazione e di trust differenziati. Questi aspetti verranno definiti in "Pattern e Profili di Interoperabilità".


.. discourse::
   :topic_identifier: 3236

	
.. [25] Per questi si faccia riferimento alla letteratura, ad es., William Stallings (2017): Cryptography And Network Security, 7th edition.

.. [26] Cf. `https://tools.ietf.org/html/rfc6749 <https://tools.ietf.org/html/rfc6749>`_

.. [27] Cf. `http://openid.net/developers/specs/ <http://openid.net/developers/specs/>`_

.. [28] Cf. `http://openid.net/connect/ <http://openid.net/connect/>`_

.. [29] Cf. `http://saml.xml.org/saml-specifications <http://saml.xml.org/saml-specifications>`_

.. [30] Cf. `http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html <http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html>`_

.. [31] Cf. `http://www.agid.gov.it/cad/art-64-sistema-pubblico-gestione-identita-digitali-modalita-accesso-ai-servizi-erogati-rete <http://www.agid.gov.it/cad/art-64-sistema-pubblico-gestione-identita-digitali-modalita-accesso-ai-servizi-erogati-rete>`_

.. [32] Cf. `http://spid-regole-tecniche.readthedocs.io/en/latest/ <http://spid-regole-tecniche.readthedocs.io/en/latest/>`_

.. [33] Per phishing si intende il tentativo di un attaccante di fingersi qualcun altro. Nel caso di OpenID Connect, in particolare, sia per quanto riguarda OpenID che OAuth2, diversi attacchi sono stati rivelati che permettono ad una relying party di redirezionare l'utente verso un identity provider falso.

.. [34] L'XML Signature Wrapping è una vulnerabilità non legata direttamente al protocollo ma presente in alcune implementazioni ed in diverse forme
    (cf., `https://blog.netspi.com/attacking-sso-common-saml-vulnerabilities-ways-find/ <https://blog.netspi.com/attacking-sso-common-saml-vulnerabilities-ways-find/>`_ ).
    Il tool SAML Raider può essere utilizzato per verificare la presenza della vulnerabilità.

.. [35] Cf. `http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation-1.2-spec-os.html <http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation-1.2-spec-os.html>`_

.. [36] Cf. `http://docs.oasis-open.org/ws-sx/ws-trust/v1.4/ws-trust.html <http://docs.oasis-open.org/ws-sx/ws-trust/v1.4/ws-trust.html>`_

.. [37] Cf. `https://tools.ietf.org/html/rfc6749#section-4.4 <https://tools.ietf.org/html/rfc6749#section-4.4>`_

.. [38] Ai fini dell'interoperabilità su Internet, la scelta di HTTP permette integrazione senza necessitare di regole particolari di inoltro o di definire Virtual Private Network - VPN.

.. .. [39] Circolare AgiD 18 aprile 2017, n.2/2017 `http://www.gazzettaufficiale.it/eli/id/2017/05/05/17A03060/sg <http://www.gazzettaufficiale.it/eli/id/2017/05/05/17A03060/sg>`_

.. .. [40] Cf. `https://tools.ietf.org/html/rfc5280\#section-4.2.1.3 <https://tools.ietf.org/html/rfc5280#section-4.2.1.3>`_

.. [41] Circolare AgID 18 aprile 2017, n.2/2017 `http://www.gazzettaufficiale.it/eli/id/2017/05/05/17A03060/sg <http://www.gazzettaufficiale.it/eli/id/2017/05/05/17A03060/sg>`_

.. [42] Cf. `https://tools.ietf.org/html/rfc5280\#section-4.2.1.3 <https://tools.ietf.org/html/rfc5280#section-4.2.1.3>`_

.. [43] Cf. `https://tools.ietf.org/html/rfc7457 <https://tools.ietf.org/html/rfc7457>`_

.. [44] Un esempio potrebbe essere una interfaccia di servizio di un comune che permette di avere in tempo reale la situazione dei posti liberi nei parcheggi comunali. Un sistema di trasporto integrato regionale accede al dato su tutti i parcheggi dei comuni della regione e mostra in tempo reale la situazione aggregata dei parcheggi disponibili. In questo scenario, l'informazione scambiata (numero posti liberi) è poco sensibile e eventuali apparati installati presso i parcheggi non giustificano il costo necessario di una configurazione a prova di non ripudio ed una mutua autenticazione TLS. Esempi di tali scenari (con standard diversi da SPCoop) sono emersi in E015, sviluppato in occasione di Expo nella Regione Lombardia.


.. _keyUsage: https://tools.ietf.org/html/rfc5280#section-4.2.1.3
