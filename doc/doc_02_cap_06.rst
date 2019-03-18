Considerazioni comparative
==========================

Un primo criterio per orientarsi tra le tecnologie di integrazione presentate nelle Sezioni 3, 4 e 5 è quella di distinguere le tecnologie adatte per una interazione sincrona da quelle adatte ad una interazione asincrona. Riguardo a questa distinzione si può fare riferimento alla seguente tabella:

+---------------------------+----------+----------+---------------------+
|                           | **SOAP** | **REST** | **Message Broker**  |
+---------------------------+----------+----------+---------------------+
| **Interazione Sincrona**  |   ✓      |    ✓     |                     |
+---------------------------+----------+----------+---------------------+  
| **Interazione Asincrona** |  ✓\*     |   ✓\*    |    ✓                |
+---------------------------+----------+----------+---------------------+

SOAP (inteso come stack WS-\*), come si evince dalla tabella, può essere utilizzato sia per interazioni sincrone che per interazioni asincrone. 

In particolare, in SOAP, l'interazione asincrona può essere ottenuta sia su protocolli di trasporto sincroni che su protocolli di trasporto asincroni. Nonostante la specifica supporti questo genere di interazioni, il supporto di middleware e framework di sviluppo a queste funzionalità è limitato. Per quanto riguarda REST invece, nonostante non originariamente previsto dalla specifica, si è visto in Sezione 5 come esso venga utilizzato come interfaccia di servizio per message broker.

Per quanto riguarda l'interazione sincrona (stile chiamata a procedura o accesso CRUD a risorsa), diverse considerazioni tecnologiche devono essere effettuate. SOAP e REST utilizzano HTTP in due modi differenti.

Mentre SOAP lo utilizza come un protocollo di trasporto, REST lo utilizza come un protocollo applicativo. La diffusione dell\'accesso alla rete ha aumentato il carico sulle infrastrutture IT, inoltre reti migliori hanno aumentato le aspettative in termini di latenza. L\'IETF nel tempo ha risposto a queste esigenze:

-   migliorando la semantica di HTTP, facendo leva sui campi Header, Status e Method `RFC7230 <https://tools.ietf.org/html/rfc7230>`_ [85]_, `RFC7231 <https://tools.ietf.org/html/rfc7231>`_ [86]_;

-   codificando le semantiche di caching `RFC7234 <https://tools.ietf.org/html/rfc7234>`_ [87]_ e controllo della concorrenza `RFC7232 <https://tools.ietf.org/html/rfc7232>`_ [88]_ per facilitare l\'implementazione di interfacce di servizio stateless, che possano scalare senza che i bilanciatori conoscano la logica applicativa;

-   orientandosi verso formati più leggeri (ad es., JSON).

Queste innovazioni fanno preferire l\'approccio REST:

-   Quando è possibile esprimere la logica applicativa tramite la semantica HTTP, poiché si guadagna:

    -   espressività (ad es., il contesto d\'utilizzo è chiarito da Method e Status);

    -   mobile-ready (esporre un\'API in un\'app con un http-wrapper);

    -   performance e scalabilità (ad es., possibilità di ruotare le chiamate in base al Method, senza inspection applicativa).

-   Quando le API devono essere fruibili anche da mobile/web;

-   L'accesso avviene in maniera prevalente con operazioni di tipo CRUD sui dati.

Quindi rispetto a quanto discusso  in “Presentazione del Modello di Interoperabilità 2018” sui paradigmi di cooperazione, questo suggerisce l'uso di REST nei casi di condivisione di dati e di composizione applicativa, quando le operazioni componenti sono prevalentemente orientate a fornire dati. Il servizio digitale corrispondente all'interfaccia di servizio è prevalentemente informativo (cf. Sezione 1).

L'utilizzo di SOAP è suggerito:

-   Quando la semantica HTTP non è sufficiente ad esprimere la logica applicativa ed è necessario usare un protocollo di messaging ulteriore con dei propri header;

-   Se la specifica applicazione richiede la creazione di interfacce di servizio principalmente *stateful*, cioè l'accesso ad informazioni di contesto o la gestione dello stato della conversazione [89]_. SOAP prevede estensioni (eg. relative al concetto di transazione) che con altri approcci (ad es., REST) devono essere costruite ad hoc per la specifica applicazione.

-   Nel caso si necessiti di processamento asincrono che non sia possibile implementare con semantiche HTTP;

-   Quando servono specifiche assicurazioni circa la QoS (quali quelle fornite dall'estensione WS-ReliableMessaging).

Quindi rispetto a quanto discusso in “Presentazione del Modello di Interoperabilità 2018” sui paradigmi di cooperazione, questo suggerisce l'uso di SOAP nei casi di processo inter-PA e di composizione applicativa quando le operazioni componenti offrono delle logiche complesse.

La tabella seguente riporta alcuni aspetti tecnologici che devono essere tenuti in considerazione (le celle in cui è presente "-" indicano che l'aspetto in questione non è considerato e standardizzato, e quindi è a cura dello specifico progetto/applicazione indirizzarlo attraverso sviluppi ad hoc)

+-----------------------+-----------------------+-----------------------+
|                       | **SOAP (WS-\*)**      | **REST**              |
+=======================+=======================+=======================+
| **Formato Payload**   | XML                   | Tutti (JSON nella     |
|                       |                       | maggior parte dei     |
|                       |                       | casi)                 |
+-----------------------+-----------------------+-----------------------+
| **Identificazione     | URI, WS-Addressing    | URI                   |
| delle operazioni**    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Descrizione delle   | WSDL                  | RAML, OpenAPI         |
| interfacce di         |                       |                       |
| servizio**            |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Affidabilità**      | WS-ReliableMessaging  | \-                    |
+-----------------------+-----------------------+-----------------------+
| **Sicurezza**         | HTTPS, WS-Security    | HTTPS, JWT            |
+-----------------------+-----------------------+-----------------------+
| **Transazioni**       | WS-AtomicTransaction, | \-                    |
|                       | WS-BusinessActivity   |                       |
+-----------------------+-----------------------+-----------------------+
| **Composizione di     | WS-Choreography       | \-                    |
| interfacce di         |                       |                       |
| servizio**            | WS-BPEL               |                       |
+-----------------------+-----------------------+-----------------------+

In letteratura, talvolta si indica con contract-first una metodologia di progetto che parte dalla specifica dell’interfaccia senza considerare possibili vincoli di implementazione, e successivamente si occupa di come realizzare tale interfaccia al di sopra di eventuali realizzazioni esistenti. In alternativa, si parla di contract-last (che potremmo anche indicare come implementation-first) quando invece eventuali vincoli di realizzazione guidano la specifica dell’interfaccia. SOAP supporta naturalmente entrambi gli approcci, in quanto lo sviluppo di un’interfaccia di servizio origina dalla definizione dell’interfaccia o dalle segnature dei metodi utilizzati nello sviluppo, mentre in REST l’interfaccia è definita dagli http verb associati alle operazioni CRUD, riportando il contratto alla definizione delle risorse. La differenza appare ininfluente nel caso di progettazione e realizzazione di sistemi nuovi, ma non in presenza di sistemi legacy. Quando l’interfaccia di servizio è vincolata dalla presenza di un sistema esistente o legacy, essa è definita a posteriori rispetto all’implementazione. In questo caso non essere limitati dai verb http (eg. usando SOAP) appare semplificare il lavoro di modellazione e realizzazione dell’interfaccia di servizio evitando di mappare risorse su procedure legacy.

Talvolta si parla di REST indicandolo come contract-less (REST) [90]_, proprio ad indicare il fatto che l’interfaccia è definita dagli http verb; a rigore però vanno comunque progettate le giuste risorse da esporre su cui effettuare operazioni CRUD, e quindi più  che essere senza contratto, è il contratto che ha una forma differente.

Nel modo REST, il principio secondo cui l’interfaccia di servizio (in questo caso l’API) deve essere il primo artefatto di progettazione, viene recentemente indicato come `API-first <https://www.programmableweb.com/api-university/understanding-api-first-design>`_ [91]_ ed è largamente adottato da molte organizzazioni private, ed anche `framework di interoperabilità nazionali come quello inglese <https://www.programmableweb.com/news/why-uks-government-data-service-takes-api-first-approach-to-datagovuk/elsewhere-web/2016/09/02>`_ [92]_.

Nel caso invece di nuovi sistemi, la progettazione dell'interfaccia può essere effettuata sia in un'ottica contract-first che contract-less. In un'ottica contract-first, la specifica dell'interfaccia viene effettuata
a tavolino a partire dalle macro-operazioni che si vogliono offerte dal sistema finale. Nel caso di accesso basato su risorsa (in ottica ROA), essendo in realtà le operazioni da effettuare già predefinite
(operazioni CRUD), il tipo di progettazione è contract-less. Vanno però definite le risorse che il sistema deve esporre, quindi una qualche forma di progettazione preventiva all'implementazione è comunque
prevista (cioè, la specifica delle risorse).

Nel progetto di interfacce di servizio SOAP occorre definire, oltre alle macro-operazioni, anche le strutture XML per la rappresentazione dei dati. Le operazioni possono essere raggruppate in base a caratteristiche quali: area funzionale (o area di business), requisiti di sicurezza (ad es. meccanismi di autenticazione ed autorizzazione), oppure in base a fattori organizzativi quali la frequenza dei cambiamenti o pattern di gestione delle versioni. Il principio alla base di questo raggruppamento è quello di impattare il minor numero di fruitori quando avviene un cambiamento.

Nel progetto di interfacce di servizio REST invece occorre:

-   Identificare le risorse che l'interfaccia di servizio manipolerà. Queste risorse sono solitamente i concetti base che stanno dietro ad un processo (ad es., un ordine di acquisto).

-   Progettare gli URI seguendo i principi introdotti nella sezione relativa alla tecnologia REST.

-   Scegliere il tipo di operazione disponibile per ognuna delle URI.

-   Scegliere i collegamenti tra risorse da fornire nelle risposte. In quest'ottica l'approccio HATEOAS può risultare utile.

-   Progettare le strutture JSON per la rappresentazione dei dati.

Il ModI 2018, come discusso nella Sezione 1, prevede che la progettazione parta dalla definizione delle interfacce di servizio, indipendentemente dalla tecnologia di realizzazione sia SOAP che REST, anche se con accorgimenti tecnici differenti nella sua realizzazione.


.. discourse::
   :topic_identifier: 3240

	
.. [85] Cf. `https://tools.ietf.org/html/rfc7230 <https://tools.ietf.org/html/rfc7230>`_

.. [86] Cf. `https://tools.ietf.org/html/rfc7231 <https://tools.ietf.org/html/rfc7231>`_

.. [87] Cf. `https://tools.ietf.org/html/rfc7234 <https://tools.ietf.org/html/rfc7234>`_

.. [88] Cf. `https://tools.ietf.org/html/rfc7232 <https://tools.ietf.org/html/rfc7232>`_

.. [89] Come nel caso di processi amministrativi sia completamente automatizzati (short-running) sia con intervento umano o comunque long-running.

.. [90] Cf. Cesare Pautasso, Olaf Zimmermann, Frank Leymann: Restful web services vs. \"big\" web services: making the right architectural decision. WWW 2008: 805-814.

.. [91] Cf. `https://www.programmableweb.com/api-university/understanding-api-first-design <https://www.programmableweb.com/api-university/understanding-api-first-design>`_
    In termini colloquiali, il principio può essere parafrasato in questi termini:

    - L'API è la prima interfaccia dell'applicazione

    - L'API viene prima dell'implementazione

    - L'API deve essere descritta (ed addirittura essere auto-descrittiva, se possibile e fattibile)

.. [92] Cf. `https://www.programmableweb.com/news/why-uks-government-data-service-takes-api-first-approach-to-datagovuk/elsewhere-web/2016/09/02 <https://www.programmableweb.com/news/why-uks-government-data-service-takes-api-first-approach-to-datagovuk/elsewhere-web/2016/09/02>`_
