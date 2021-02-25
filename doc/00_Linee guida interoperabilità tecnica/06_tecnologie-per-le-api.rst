Tecnologie per le API
=====================

Un aspetto che si vuole qui richiamare è la relazione tra l’interno e
l’esterno del sistema informativo di una Pubblica Amministrazione, e
come questo confine abbia impatti sugli e-service in termini di
funzionalità e sicurezza.

Nel precedente modello di interoperabilità (il cosiddetto SPCoop del
2005) era stato definito il concetto di *dominio* di un’amministrazione, a
indicare l’insieme delle risorse (dati e servizi) e delle politiche che
un’amministrazione assicurava per dare seguito alla cooperazione con
altre. Il confine tra i domini delle amministrazioni era istanziato
fisicamente da uno specifico elemento architetturale, la Porta di
Dominio (PdD).

Nel nuovo framework di interoperabilità, l’istanziazione della PdD come
punto unico di accesso a un’interfaccia viene meno. Tuttavia,
concettualmente il confine del dominio dell’amministrazione continua a
esistere ed è importante considerarlo nella progettazione degli
e-service. Gli e-service sono offerti da qualsiasi server applicativo,
senza essere vincolati a essere raggiungibili attraverso un unico
gateway.

Quindi, ogni server applicativo offre e-service, tuttavia è comunque
significativo distinguere se gli stessi sono offerti per interoperare:

1. all’interno del dominio (da parte di client applicativi offerti dalla
   stessa amministrazione (ad es., un’applicazione Web o una mobile verso il back-end,
   integrazione tra banche dati nel back-end, ecc);

2. verso altre amministrazioni o altri soggetti con cui è stabilita una
   relazione di fiducia.

Le Pubbliche Amministrazioni, nella loro autonomia organizzativa
possono adottare queste Linee Guida
anche per i servizi sviluppati all’interno del proprio dominio.
Adottare il principio API-first per i servizi interni
permette di riutilizzare le componenti e di integrarle più
facilmente con quelle delle altre organizzazioni in caso di necessità.
Le regole tecniche inoltre permettono di applicare criteri di qualità
uniformi per tutti i servizi ICT, consolidando le prassi di sicurezza,
migliorando la qualità della spesa e
mitigando i rischi anche interni legati alla protezione dei dati personali.

Una trattazione completa dei paradigmi per la progettazione e
realizzazione delle API esula dagli scopi del presente documento. La
breve discussione che viene presentata in questa sezione vuole ricordare
a chi legge le differenti tecnologie per la realizzazione di API e il
modello architetturale sottostante (RPC-like o resource-oriented).

Le API possono essere progettate secondo due paradigmi:

Remote Procedure Call (RPC)-like.
   In questo paradigma, un’interfaccia
   di servizio espone una serie di operazioni (metodi) che permettono
   l’invocazione delle operazioni offerte dall’interfaccia. Il
   significato dell’operazione è informalmente espresso dal nome
   dell’operazione, dal numero e dal tipo dei suoi parametri, dal tipo
   del valore di ritorno (il tutto viene detto tecnicamente firma o
   signature). Approcci formali prevedono che tale significato venga
   eventualmente anche descritto in opportuni documenti di
   accompagnamento e/o attraverso specifiche formali dell’interfaccia di
   servizio. Ogni operazione può quindi rappresentare, sia semplici
   operazioni di computazione, sia operazioni potenzialmente di lunga
   durata, sia operazioni di accesso a dati, ecc. Il paradigma è detto
   RPC-like in quanto le API ricordano le librerie di chiamata a
   procedura e quindi l’interfaccia, metaforicamente, è di fatto una
   libreria di funzioni.

Resource-oriented.
   In questo paradigma, l’interfaccia di servizio
   offre operazioni di creazione, lettura, aggiornamento e cancellazione
   di risorse. In inglese, Create, Read, Update, Delete, da cui
   l’acronimo da cui prende il nome il paradigma: CRUD. Una risorsa è un
   qualsiasi oggetto informativo che possiede uno stato. In questo
   paradigma, l’interfaccia di servizio è metaforicamente un accesso
   diretto a una base informativa, e le uniche operazioni possibili sono
   appunto le modifiche a tali risorse.

Parallelamente, esistono delle tecnologie con cui poter naturalmente
realizzare API, che sono:

#. SOAP e il cosiddetto stack WS\-\*
#. lo stile architetturale REST, basato su HTTP.

Un Web service SOAP 
   espone un insieme di metodi richiamabili da
   remoto da parte di un client. SOAP definisce una struttura dati per
   lo scambio di messaggi tra applicazioni, codificata in XML; di fatto
   SOAP utilizza HTTP come protocollo di trasporto, ma non è limitato né
   vincolato ad esso.

Un Web service che sfrutta l’architettura REST 
   adotta il modello basato su *risorse* secondo le seguenti caratteristiche:

   -  individuazione delle risorse mediante il formalismo dei Uniform
      Resource Identifier (URI);

   -  operazioni sulle risorse effettuate sulla rappresentazione del
      loro stato;

   -  CRUD sulle risorse mediante HTTP utilizzando i metodi nella
      semantica prevista dal protocollo stesso.

L’approccio REST evidenzia le caratteristiche del Web come piattaforma
leggera per l’elaborazione distribuita. Non è in prima istanza
necessario aggiungere nulla a quanto è già esistente sul Web per
consentire ad applicazioni remote di interagire.

Si noti che nell’applicazione pratica di REST si assiste al suo uso in
modalità non del tutto canoniche. Ogni deviazione rispetto alle
caratteristiche previste da REST porta alla realizzazione di
architetture ibride tra il paradigma RESTful Web service e quello dei
Web service RPC-like. In merito ai modelli ibridi che si possono
presentare, esiste una classificazione, il cosiddetto Richardson
Maturity Model 3 che prevede quattro livelli, da 0 a 3, in accordo al
grado di aderenza ai dettami REST. In particolare, si possono presentare
i casi seguenti:

Livello 0
   per servizi che semplicemente usano HTTP come protocollo
   di trasporto applicativo (tunnel HTTP). In questo caso il sistema non
   ha niente del modello REST.

Livello 1
   per i servizi che operano sulle risorse definite secondo
   la sintassi e la semantica previste per le URI, sulle quali si opera
   invocando delle operazioni (metodi) che agiscono su di esse.

Livello 2
   per i servizi che operano su risorse definite secondo la
   sintassi e la semantica previste per le URI, sulle quali si opera
   sulla rappresentazione del loro stato per mezzo del protocollo HTTP
   usando la semantica dei metodi (verbi) come previsti dal protocollo.

Livello 3
   come per il livello 2, con in aggiunta la possibile
   presenza di controlli ipermediali nella rappresentazione delle
   risorse.

Le Linee Guida accolgono l’implementazione di API REST
classificabili al livello 1 del Richardson Maturity Model.

**Le Linee Guida accolgono indifferentemente SOAP e REST quali
tecnologie per l’implementazione delle API. La scelta della tecnologia
da utilizzare è lasciata alle Pubbliche Amministrazioni che
costituiscono un dominio di interoperabilità sulla base delle specifiche
esigenze.**

.. forum_italia::
   :topic_id: 21442
   :scope: document
