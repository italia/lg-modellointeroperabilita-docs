Scenario pregresso dell'interoperabilità nella PA
=================================================

Nell'ottobre 2005 il CNIPA (oggi Agenzia per l'Italia digitale - AgID) ha pubblicato un insieme di documenti che costituiscono il riferimento tecnico per l'interoperabilità fra le PA. Tali documenti delineano il quadro tecnico-implementativo del Sistema pubblico di cooperazione (SPCoop), `framework di interoperabilità a livello applicativo <http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/sistema-pubblico-connettivita/cooperazione-applicativa>`__ [8]_.

SPCoop ha costituito il modello concettuale ed architetturale della cooperazione applicativa tra differenti Amministrazioni e/o soggetti pubblici italiani. Tale sistema era organizzato in modo da:

-   supportare una modalità di erogazione dei servizi articolata per procedimenti istituzionali;

-   essere paritetico fra tutti i soggetti cooperanti;

-   essere indipendente dagli assetti organizzativi dei soggetti cooperanti;

-   lasciare a ciascun soggetto cooperante la responsabilità dei servizi erogati e dei dati forniti;

-   garantire a ciascun soggetto autonomia nella gestione dei propri sistemi e nella definizione ed attuazione delle politiche di sicurezza del proprio sistema informativo;

-   lasciare a ciascun soggetto la responsabilità delle autorizzazioni per l'accesso ai propri dati e/o servizi.

In sintesi, alla base di SPCoop vi erano i seguenti principi:

1. 	*cooperazione tra amministrazioni* attraverso la erogazione e fruizione di servizi offerti tramite un unico elemento logico denominato *Porta di Dominio;*

2.  *ambito di responsabilità* delle singole Amministrazioni dei servizi erogati che costituiscono il *Dominio di servizi applicativi* della stessa Amministrazione;

3. 	*accordi di servizio* quale rappresentazione formale della cooperazione tra erogatore/i e fruitore/i costituiti sulla base di un fondamento normativo;

4.	*tecnologie di cooperazione:* i servizi erano erogati come web service basati sugli standard che in quel momento erano consolidati ed in uso (SOAP, WSDL, UDDI).

Con l'obiettivo di assicurare agli utenti di avere una visione integrata dei servizi di ogni PA, le tematiche coperte da SPCoop sono state tutte quelle che interessano l\'interoperabilità dei sistemi a diversi livelli, ovvero:

-   interoperabilità applicativa;

-   catalogazione dei servizi;

-   semantica dei dati e dei servizi;

-   identità digitale.

Lo scenario normativo di SPCoop è quello inquadrato dal DPCM 1 aprile 2008, recante regole tecniche e di sicurezza del Sistema pubblico di connettività (SPC), di cui SPCoop era un componente fondamentale, poi compiutamente delineato sul piano tecnico-implementativo da una suite di linee guida di seguito richiamate:

-   Interoperabilità applicativa

    -   Specifiche della busta di e-gov

    -   Specifiche della porta di dominio

    -   Linee guida busta di e-gov

    -   Qualificazione della porta di dominio

    -   Qualificazione porta di dominio con concorso delle regioni

-   Catalogazione dei servizi

    -   Specifiche dell\'accordo di servizio

    -   Specifiche del Registro SICA

    -   Raccomandazioni stesura accordi di servizio

-   Semantica dei dati e dei servizi

    -   Nomenclatura e semantica

-   Identità digitale

    -   GFID - Gestione federata delle identità digitali

In particolare SPCoop prevedeva:

-   Tutti i servizi applicativi di una PA erano offerti attraverso un unico elemento denominato *Porta di Dominio*, che svolgeva funzioni di proxy e dispatcher assicurando l'implementazione del protocollo applicativo denominato *Busta e-Gov*, un\'estensione dello standard SOAP.

-   I servizi infrastrutturali per la gestione di tutti gli aspetti legati agli *accordi di servizio*, nel loro insieme denominati *Servizi* *SICA*, prevedevano:

    -   *Servizi di Registro*: la componente, realizzata a partire dallo standard UDDI, entro cui erano registrati gli Accordi di Servizio organizzati in modo distribuito prevedendo due livelli, ovvero Generale, che contiene la totalità degli *accordi di servizio*, e Secondario, contenente delle viste definite secondo differenti criteri;

    -   *Catalogo degli Schemi/Ontologie*, che offre gli strumenti per ragionare sulla semantica dei servizi e delle informazioni da essi veicolati;

    -   *Servizi di Sicurezza* assicuravano le funzionalità per la qualificazione degli elementi del sistema e garantire gli opportuni requisiti di autenticità, riservatezza, integrità, non ripudio e tracciabilità dei messaggi scambiati.

Il tempo trascorso dalla definizione del modello e il mutato quadro tecnico, organizzativo e normativo rendono necessario l'aggiornamento del modello, obiettivo appunto della presente iniziativa, come anticipato nel 2017 attraverso la Determinazione 219/2017 - `Linee guida per transitare al nuovo modello di interoperabilità <http://www.agid.gov.it/sites/default/files/upload\_avvisi/linee\_guida\_passaggio\_nuovo\_modello\_interoperabilita.pdf>`__ [9]_.

L'esperienza maturata con SPCoop, di seguito sintetizzata, deve essere considerata nella definizione del ModI 2018.

**Cosa ha funzionato**

-   La definizione di un quadro comune per l'implementazione dei meccanismi di interoperabilità tra i sistemi delle Pubbliche Amministrazioni permette di orientare gli sforzi per la realizzazione di servizi pubblici sulla logica propria degli stessi.

-   Il coordinamento, anche delegato ad organi intermedi quali elementi di aggregazione di un insieme omogeneo di Amministrazioni, permette di favorire l'applicazione del modello condiviso.

-   Il sistema di gestione federata delle identità digitali, nonostante si ponesse come un elemento fortemente innovativo, è stato utilizzato a livello regionale e ha consentito di disegnare su tali basi tecniche il futuro SPID.

**Cosa deve essere cambiato**

-   Le tecnologie e gli standard utilizzati dal modello SPCoop richiedono un consistente aggiornamento in considerazione delle innovazioni intervenute in tali ambiti.

-   È necessario un modello di governance che permetta di gestire le specificità dei singoli domini applicativi determinati dalle caratteristiche delle amministrazioni e dei soggetti terzi coinvolti.

**Cosa deve essere abbandonato**

-   L'adozione di un'unica modalità per attuare l'interoperabilità dei sistemi non permette di considerare la molteplicità e la specificità delle esigenze di scambio tra le Pubbliche Amministrazioni e di queste con i cittadini e le imprese.

-   La necessità di componenti infrastrutturali disegnati per la sola Pubblica Amministrazione italiana (come Porta di Dominio e Registro SICA) determina che la spesa per il loro sviluppo ed evoluzione sia totalmente a carico della Pubblica Amministrazione.


.. discourse::
   :topic_identifier: 3233

	
.. [8] Cf. `http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/sistema-pubblico-connettivita/cooperazione-applicativa <http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/sistema-pubblico-connettivita/cooperazione-applicativa>`__

.. [9] Cf. `http://www.agid.gov.it/sites/default/files/upload\_avvisi/linee\_guida\_passaggio\_nuovo\_modello\_interoperabilita.pdf <http://www.agid.gov.it/sites/default/files/upload\_avvisi/linee\_guida\_passaggio\_nuovo\_modello\_interoperabilita.pdf>`__
    
