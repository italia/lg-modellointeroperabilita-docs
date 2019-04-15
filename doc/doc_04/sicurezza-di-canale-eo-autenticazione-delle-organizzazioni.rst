Sicurezza di canale e/o identificazione delle organizzazioni
============================================================

[IDAC01] Direct Trust Transport-Level Security
----------------------------------------------

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri, a livello di
canale:

-  confidenzialità

-  integrità

-  identificazione dell’erogatore, quale organizzazione

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un `trust`_ tra fruitore
(client) ed erogatore (server), che permette il riconoscimento del
certificato X.509, o la CA emittente dell’erogatore, così come previsto
dal protocollo Transport Layer Security `[5] <bibliografia.html>`__ `[6] <bibliografia.html>`__.

La sequenza dei messaggi di richiesta/risposta avviene dopo 
aver instaurato il canale di trasmissione sicuro.

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Sicurezza di canale e/o Autenticazione dell'Erogatore
   :alt: Sicurezza di canale e/o Autenticazione dell'Erogatore
   
   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply()
      deactivate E
      deactivate F


Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Il canale sicuro tra erogatore e fruitore viene instaurato utilizzando
il protocollo TLS, secondo le modalità specificate alla sezione `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce sul canale sicuro stabilito il messaggio di
   richiesta all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce il risultato.

Come indicato in :RFC:`5246` l’impiego del protocollo TLS garantisce a **livello di canale**:

-  l’autenticazione dell’erogatore identificato mediante il certificato
   X.509

-  la confidenzialità dei dati scambiati

-  l’integrità dei dati scambiati 

L’impiego del protocollo TLS 1.2 o maggiore, mitiga il rischio di:

-  Replay Attack

-  Spoofing


[IDAC02] Direct Trust mutual Transport-Level Security
-----------------------------------------------------

.. _sicurezza_canale_scenario-1:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
canale:

-  confidenzialità

-  integrità

-  identificazione dell’erogatore e del fruitore, quale organizzazioni

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

.. _sicurezza_canale_descrizione-1:

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un `trust`_ tra fruitore
(client) ed erogatore (server), che permette il riconoscimento da
entrambe le parti dei certificati X.509, o le CA emittenti, così come
previsto dal protocollo Transport Layer Security `[5] <bibliografia.html>`__ `[6] <bibliografia.html>`__.

La sequenza dei messaggi di richiesta/risposta avviene dopo 
aver instaurato il canale di trasmissione sicuro.

.. _sicurezza_canale_dettaglio-1:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Sicurezza di canale e/o Autenticazione delle organizzazioni
   :alt: Sicurezza di canale e/o Autenticazione delle organizzazioni
   
   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply()
      deactivate E
      deactivate F

.. _sicurezza_canale_regole-di-processamento-1:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, secondo le modalità
specificate alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce utilizzando canale sicuro stabilito con il il
   messaggio di richiesta all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce un risultato.

Come indicato in :RFC:`5246` l’impiego del protocollo TLS garantisce a **livello di canale**:

-  l’autenticazione di erogatore e fruitore identificati mediante
   certificati X.509

-  la confidenzialità dei dati scambiati

-  l’integrità dei dati scambiati

L’impiego del protocollo TLS 1.2 o maggiore, mitiga il rischio di:

-  Replay Attack

-  Spoofing

.. _`Elenco degli algoritmi`: elenco-degli-algoritmi.html

.. _`trust`: ../doc_04_cap_00.html

.. discourse::
   :topic_identifier: 8906
