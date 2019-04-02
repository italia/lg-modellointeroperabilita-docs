Considerazioni sulla natura del fruitore
========================================

Come anticipato nei paragrafi precedenti, nel ModI scompare il
concetto di dominio e di porta di dominio, a favore di un approccio in
cui le interfacce di servizio possono essere offerte e dispiegate presso
qualsiasi elemento computazionale in uso presso l’Amministrazione.
Parallelamente, nel ModI, i client applicativi alle interfacce di
servizio possono essere qualsiasi, potenzialmente sia sviluppati
dall’amministrazione stessa (ad esempio, una app mobile o una Web app
per offrire il servizio) o da terze parti; questa a sua volta possono
essere altre amministrazioni, con le quali esiste una relazione
fiduciaria, oppure vere e proprie entità esterne (aziende, enti no
profit, associazioni, il singolo sviluppatore, ecc.). È chiaro che se da
un lato l’esposizione di interfacce di servizio spinge verso un modello
aperto in cui “chiunque” potenzialmente possa sviluppare client
applicativi alle stesse, al fine di innovare digitalmente i servizi
della pubblica amministrazione, dall’altro ci sono dei requisiti di
sicurezza, rispetto delle legislazione esistente, relazioni fiduciarie
tra chi offre l’interfaccia di servizio e chi la utilizza che vanno
dettagliatamente approfondite caso per caso. La tecnologia con cui
esporre le interfacce di servizio ha sicuramente un ruolo, in quanto
l’esposizione di interfacce di servizio REST sicuramente semplifica -
stante l’attuale panorama dello sviluppo software - applicazioni
orientate all’utente finale, mentre SOAP, d’altro canto, proprio in
quanto middleware, è più orientato a modalità sistema informatico -
sistema informatico (cosiddetta *integrazione di tipo enterprise*).

Altra dimensione da tenere in considerazione è la tipologia di client
applicativo all’interfaccia di servizio. Interfacce di servizio REST -
sempre stante l’attuale panorama dello sviluppo applicativo - sono
particolarmente adatte ad essere utilizzate da client mobile/Web;
viceversa, client mobili oggi riescono ad interagire con interfacce di
servizio SOAP con un maggiore sforzo in termini di sviluppo
applicativo [1]_. Di contro, in applicazioni in cui software di
un’amministrazione ha la necessità di invocare interfacce applicative
offerte da un’altra (*integrazione di tipo enterprise*), SOAP essendo
una specifica per middleware, rende estremamente agevole lo sviluppo, e
questo permette il riuso di tutte le interfacce di servizio che sono
state sviluppate negli anni da parte delle pubbliche amministrazioni
secondo SPCoop.

.. [1]
   Ciò è dovuto al semplice fatto che i framework di sviluppo di
   applicazioni mobili si sono orientati verso REST, mentre il supporto
   allo sviluppo di client SOAP viene scarsamente supportato dai
   framework, e quindi pur se tecnicamente fattibile, risulta più
   costoso in termini di sforzo di sviluppo. Cf.
   https://stackoverflow.com/questions/297586/how-to-call-a-soap-web-service-on-android,
   https://www.nascenia.com/consuming-soap-webservices-from-ios/,
   https://www.codeproject.com/Tips/622376/iOS-Soap-Webservice-Calling-and-Parsing-the-Resp-2
