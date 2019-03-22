Sicurezza di canale e/o Autenticazione delle organizzazioni
============================================================

[M2MC01] Direct Trust Transport-Level Security
----------------------------------------------

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri, a livello di
canale:

-  confidenzialità

-  integrità

-  autenticazione dell’erogatore, quale organizzazione

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un trust tra fruitore
(client) ed erogatore (server), che permette il riconoscimento del
certificato X.509, o la CA emittente dell’erogatore, così come previsto
dal protocollo Transport-Level Security `[5] <bibliografia.html>`__ `[6] <bibliografia.html>`__.

La sequenza dei messaggi di richiesta/risultato avviene a seguito
dell’instaurazione di un canale di trasmissione sicuro in cui
l’erogatore è autenticato.

Dettaglio
^^^^^^^^^

.. figure:: index/image1.png
   :align: center
   
Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

Tra erogatore e fruitore viene instaurato un canale di trasmissione
sicuro; il flusso dei messaggi avviene secondo la sequenza:

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

**B: Risultato**

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Il canale sicuro tra erogatore e fruitore viene instaurato utilizzando
il protocollo TLS, secondo le modalità specificate alla sezione `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce sul canale sicuro stabilito il messaggio di
   richiesta all’interfaccia di servizio dell’erogatore.

**B: Risultato**

3. L’erogatore elabora il messaggio e restituisce il risultato.

L’impiego del protocollo TLS garantisce a livello di canale:

-  l’autenticazione dell’erogatore identificato mediante il certificato
   X.509

-  la confidenzialità dei messaggi scambiati

-  l’integrità dei messaggi scambiati

L’impiego del protocollo TLS 1.2 o maggiore, garantisce un’efficace
difesa dalle minacce, quali ad esempio:

-  Replay Attack

-  Spoofing


[M2MC02] Direct Trust mutual Transport-Level Security
-----------------------------------------------------

.. _scenario-1:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
canale:

-  confidenzialità

-  integrità

-  autenticazione dell’erogatore e del fruitore, quale organizzazione

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

.. _descrizione-1:

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un trust tra fruitore
(client) ed erogatore (server), che permette il riconoscimento da
entrambe le parti dei certificati X.509, o le CA emittenti, così come
previsto dal protocollo Transport-Level Security `[5] <bibliografia.html>`__ `[6] <bibliografia.html>`__.

La sequenza dei messaggi di richiesta/risultato avviene a seguito
dell’instaurazione di un canale di trasmissione sicuro in cui sono state
autenticate entrambe le organizzazioni.

.. _dettaglio-1:

Dettaglio
^^^^^^^^^

.. figure:: index/image1.png
   :align: center

.. _flusso-delle-interazioni-1:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

Tra erogatore e fruitore viene instaurato un canale di trasmissione
sicuro; il flusso dei messaggi avviene secondo la sequenza:

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

**B: Risultato**

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-1:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, secondo le modalità
specificate alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce utilizzando canale sicuro stabilito con il il
   messaggio di richiesta all’interfaccia di servizio dell’erogatore.

**B: Risultato**

3. L’erogatore elabora il messaggio e restituisce un risultato.

L’impiego del protocollo TLS garantisce a livello di canale:

-  l’autenticazione di erogatore e fruitore identificati mediante
   certificati X.509

-  la confidenzialità dei messaggi scambiati

-  l’integrità dei messaggi scambiati

L’impiego del protocollo TLS 1.2 o maggiore, garantisce un’efficace
difesa dalle minacce, quali ad esempio:

-  Replay Attack

-  Spoofing

.. discourse::
   :topic_identifier: 8906
