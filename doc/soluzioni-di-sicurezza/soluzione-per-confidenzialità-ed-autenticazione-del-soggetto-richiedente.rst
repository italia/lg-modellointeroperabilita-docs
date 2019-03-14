5.1. Soluzione per confidenzialità ed autenticazione del soggetto richiedente
=============================================================================

.. _scenario-8:

5.1.1. Scenario
---------------

Dare seguito ad uno scambio tra richiedente ed erogatore che garantisca:

-  la confidenzialità a livello di canale

-  l’autenticazione del soggetto Fruitore

Il soggetto fruitore potrebbe non coincidere con l’unità organizzativa
richiedente, ma comunque appartenere alla stessa.

Questa soluzione utilizza i seguenti profili:

-  **M2MC01**

-  **M2MS01** o in alternativa **M2MR01**

5.1.2. Precondizioni
--------------------

Si assume l’esistenza di un trust tra richiedente ed erogatore che
stabilisce:

-  riconoscimento da parte dell’erogatore dei certificati X.509, o la CA
   emittente, relative al soggetto fruitore

-  riconoscimento da parte del richiedente del certificato X.509, o la
   CA emittente, relative al soggetto erogatore

Il meccanismo con cui è stabilito il trust non condiziona quanto
descritto nella sezione.

.. _flusso-delle-interazioni-8:

5.1.3. Flusso delle interazioni
-------------------------------

**A: Richiesta**

Il messaggio di richiesta viene firmato utilizzando il profilo
**M2MS01** nel caso di utilizzo di SOAP o **M2MR01** nel caso di
utilizzo di REST, per garantire:

-  l’autenticazione dell’identità del soggetto fruitore

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio viene trasmesso su un canale sicuro utilizzando il profilo
**M2MC01** per garantire:

-  la confidenzialità a livello di canale.

**B: Risposta**

L’erogatore da seguito a quanto previsto nel profilo **M2MS01** nel caso
di utilizzo di SOAP o **M2MR01** nel caso di utilizzo di REST
