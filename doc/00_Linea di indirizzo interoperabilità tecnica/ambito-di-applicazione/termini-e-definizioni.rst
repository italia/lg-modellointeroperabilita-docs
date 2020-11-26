Termini e definizioni
=====================

+-----------------------------------+-----------------------------------+
| **[AgID]**                        | Agenzia per l’Italia Digitale     |
+-----------------------------------+-----------------------------------+
| **[CAD]**                         | Codice Amministrazione Digitale,  |
|                                   | D.lgs. 7 marzo 2005, n. 82        |
+-----------------------------------+-----------------------------------+
| **[PA]**                          | Pubblica Amministrazione Italiana |
+-----------------------------------+-----------------------------------+
| **[UML]**                         | Linguaggio di modellazione        |
|                                   | unificato (Unified Modeling       |
|                                   | Language)                         |
+-----------------------------------+-----------------------------------+
| **[API]**                         | Application Programming Interface |
+-----------------------------------+-----------------------------------+
| **[EIF]**                         | European Interoperability         |
|                                   | Framework                         |
+-----------------------------------+-----------------------------------+
| **[HTTP]**                        | Hypertext Transfer Protocol       |
+-----------------------------------+-----------------------------------+
| **[W3C]**                         | World Wide Web Consortium         |
+-----------------------------------+-----------------------------------+
| **[XML]**                         | eXtensible Markup Language        |
+-----------------------------------+-----------------------------------+
| **[RPC]**                         | Remote Procedure Call             |
+-----------------------------------+-----------------------------------+
| **[SOAP]**                        | Simple Object Access Protocol     |
+-----------------------------------+-----------------------------------+
| **[REST]**                        | Representational State Transfer   |
+-----------------------------------+-----------------------------------+
| **[BP]**                          | WS-I Basic Profile - (Web         |
|                                   | Services Interoperability         |
|                                   | Specification)                    |
+-----------------------------------+-----------------------------------+
| **[WSDL]**                        | Web Services Description Language |
+-----------------------------------+-----------------------------------+
| **[JWT]**                         | JSON Web Tokens                   |
+-----------------------------------+-----------------------------------+
| **[IDPS]**                        | Interoperable Digital Public      |
|                                   | Services                          |
+-----------------------------------+-----------------------------------+
| **[Erogatore]**                   | Uno dei soggetti di cui           |
|                                   | all'articolo 2, comma 2 del CAD   |
|                                   | che rende disponibile e-service   |
|                                   | ad altre organizzazioni, per la   |
|                                   | fruizione di dati in suo possesso |
|                                   | o l’integrazione dei processi da  |
|                                   | esso realizzati                   |
+-----------------------------------+-----------------------------------+
| **[Fruitore]**                    | Un’organizzazione che utilizza    |
|                                   | gli e-service messi a             |
|                                   | disposizione da un dei soggetti   |
|                                   | di cui all'articolo 2, comma 2    |
|                                   | del CAD                           |
+-----------------------------------+-----------------------------------+
| **[e-service]**                   | I servizi digitali, realizzati da |
|                                   | un erogatore per assicurare       |
|                                   | l’accesso ai propri dati e/o      |
|                                   | l’integrazione dei propri         |
|                                   | processi attraverso l'interazione |
|                                   | dei suoi sistemi informatici con  |
|                                   | quelli dei fruitori, trovano      |
|                                   | attuazione nell’implementazione   |
|                                   | di API                            |
+-----------------------------------+-----------------------------------+
| **[ModI]**                        | Modello di Interoperabilità delle |
|                                   | Pubbliche Amministrazioni         |
|                                   | Italiane                          |
+-----------------------------------+-----------------------------------+
| **[XML-RPC]**                     | XML-Remote Procedure Call         |
+-----------------------------------+-----------------------------------+
| **[QoS]**                         | Quality of Service                |
+-----------------------------------+-----------------------------------+
| **[SLI]**                         | Service Level Indicator           |
+-----------------------------------+-----------------------------------+
| **[SLO]**                         | Service Level Objective           |
+-----------------------------------+-----------------------------------+
| **[SLA]**                         | Service Level Agreement           |
+-----------------------------------+-----------------------------------+
| **[API-First]**                   | L'API-first è un approccio in cui |
|                                   | le PA considerano le API come     |
|                                   | mezzo principale per perseguire i |
|                                   | propri obiettivi, interagendo con |
|                                   | i propri stakeholder sin dalla    |
|                                   | fase di progettazione             |
+-----------------------------------+-----------------------------------+
| **[Contract-First]**              | Contract-first è un approccio che |
|                                   | prevede di dare seguito           |
|                                   | all'interazione di più sistemi    |
|                                   | informatici definendo le API      |
|                                   | condivise attraverso un Interface |
|                                   | Description Language (IDL)        |
+-----------------------------------+-----------------------------------+
| **[WS-*]**                        | Lo stack degli standard emanati   |
|                                   | relativi alle tecnologie SOAP,    |
|                                   | tra cui SOAP, WSDL, WS-Security,  |
|                                   | WS-Addressing e WS-I              |
+-----------------------------------+-----------------------------------+
| **[Enti Capofila]**               | Gli enti capofila sono pubbliche  |
|                                   | amministrazioni che si propongono |
|                                   | nel ModI quali soggetti           |
|                                   | responsabili delle attività di    |
|                                   | gestione sul Catalogo degli       |
|                                   | e-service, delle API e degli      |
|                                   | accordi di interoperabilità nelle |
|                                   | veci di altre Pubbliche           |
|                                   | Amministrazioni                   |
+-----------------------------------+-----------------------------------+

4. .. rubric:: 
      Principi generali
      :name: principi-generali

   6. .. rubric:: Interazioni
         :name: interazioni

L’ambito di applicazione della Linea di indirizzo, in coerenza con il
ModI, comprende i tre tipi di interazioni previste nell’EIF che vedono
coinvolte Pubbliche Amministrazioni, cittadini e imprese.

Le interazioni prevedono che i soggetti coinvolti possano svolgere la
funzione di erogatore di servizi, quando il soggetto mette a
disposizione servizi digitali utilizzati da altri soggetti, e la
funzione di fruitore, quando il soggetto utilizza i servizi digitali
messi a disposizione da un altro soggetto.

|image0|

*Figura 1 - Ambito di applicazione del modello di interoperabilità*

I soggetti fruitori possono utilizzare i servizi digitali in maniera
trasparente all’erogatore, attraverso:

-  una soluzione software attivata da un attore umano (user
   agent/human);

-  un sistema applicativo automatico (server/machine), anche allo scopo
   di definire nuovi servizi a valore aggiunto.

   7. .. rubric:: Application Programming Interface (API)
         :name: application-programming-interface-api

Con Application Programming Interface (API) si indica ogni insieme di
procedure/funzionalità/operazioni disponibili al programmatore, di
solito raggruppate a formare un insieme di strumenti specifici per
l’espletamento di un determinato compito. Spesso, con tale termine si
intendono le librerie software disponibili in un certo linguaggio di
programmazione. Una buona API fornisce una “scatola nera”, cioè un
livello di astrazione che evita al programmatore di conoscere i dettagli
implementativi dell’API stessa. Questo permette di ri-progettare o
migliorare le funzioni all’interno dell’API, senza cambiare il codice
che si affida ad essa. La finalità di un’API è di ottenere un’astrazione
a più alto livello, di solito tra lo strato sottostante l’API e i suoi
consumatori (client).

Con Web API si indicano le API rese disponibili al client attraverso
Internet (prevalentemente sul Web, che si basa sul protocollo HTTP).

Per il World Wide Web Consortium (W3C), un web service è qualsiasi
software disponibile su Internet che standardizza la sua interfaccia
tramite la codifica eXtensible Markup Language (XML). Un client
interroga un servizio web inviando una richiesta in formato XML; il
servizio web ritorna una risposta utilizzando l’analogo formato. Client
e web service comunicano attraverso una rete che li connette e sfruttano
generalmente il protocollo applicativo HTTP. I web service si basano
principalmente su standard come XML-Remote Procedure Call (XML-RPC) e
Simple Object Access Protocol (SOAP). Quindi, un web service è un
possibile modo di realizzare una Web API. A partire dalla seconda metà
degli anni 2000, creando possibili confusioni, il termine Web API è
stato utilizzato come alternativa a web service per indicare altri
approcci/protocolli/tecnologie, come le API REpresentational State
Transfer (REST) per realizzare API senza utilizzare XML-RPC e SOAP.

Nell’ambito della Linea di indirizzo, accettando la nomenclatura in uso
a livello europeo e più in generale nel contesto internazionale, si
utilizza il termine generico API per indicare indifferentemente le Web
API, i web service e le API REST, lasciando al contesto in cui lo stesso
è utilizzato la declinazione del significato esplicito.

La Linea di indirizzo individua le modalità con cui le Pubbliche
Amministrazioni implementano le proprie API quale elemento tecnologico
di base del ModI attraverso cui le Pubbliche Amministrazioni rendono
disponibile gli e-service utilizzati dai sistemi informatici di altre
Pubbliche Amministrazioni, cittadini e imprese.

.. |image0| image:: ./media/image1.png
   :width: 4.125in
   :height: 2.90278in
