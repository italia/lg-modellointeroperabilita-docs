2.4. [M2MC02] Direct Trust mutual Transport-Level Security
==========================================================

.. _scenario-1:

2.4.1. Scenario
---------------

Comunicazione tra richiedente ed erogatore che assicuri a livello di
canale:

-  confidenzialità

-  integrità

-  autenticazione dell’erogatore e del fruitore, quale organizzazione

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

.. _descrizione-1:

2.4.2. Descrizione
------------------

Il presente profilo assume l’esistenza di un trust tra richiedente
(client) ed erogatore (server), che permette il riconoscimento da
entrambe le parti dei certificati X.509, o le CA emittenti, così come
previsto dal protocollo Transport-Level Security [5][6].

La sequenza dei messaggi di richiesta/risultato avviene a seguito
dell’instaurazione di un canale di trasmissione sicuro in cui sono state
autenticate entrambe le organizzazioni.

.. _dettaglio-1:

2.4.3. Dettaglio
----------------

|image0|

.. _flusso-delle-interazioni-1:

2.4.3.1. Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tra erogatore e fruitore viene instaurato un canale di trasmissione
sicuro; il flusso dei messaggi avviene secondo la sequenza:

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

**B: Risultato**

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

.. _regole-di-processamento-1:

2.4.3.2. Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, secondo le modalità
specificate alla sezione `Elenco degli
algoritmi <#elenco-degli-algoritmi>`__ .

**A: Richiesta**

1. Il richiedente costruisce un messaggio di richiesta.

2. Il richiedente spedisce utilizzando canale sicuro stabilito con il il
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

.. |image0| image:: ./media/image6.png
   :width: 2.34375in
   :height: 1.28125in
