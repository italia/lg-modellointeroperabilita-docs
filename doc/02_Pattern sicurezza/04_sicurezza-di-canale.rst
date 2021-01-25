Sicurezza di canale e/o identificazione delle organizzazioni
============================================================


[ID_AUTH_CHANNEL_01] Direct Trust Transport-Level Security
----------------------------------------------------------

Comunicazione tra fruitore ed erogatore che assicuri, a livello di
canale:

-  confidenzialità;

-  integrità;

-  identificazione dell’erogatore, quale organizzazione;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing.

.. _id-auth-channel-01-descrizione:

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un trust tra fruitore ed
erogatore, che permette il riconoscimento del certificato X.509, o la CA
emittente dell’erogatore, così come previsto dal protocollo Transport
Layer Security.

La sequenza dei messaggi di richiesta/risposta avviene dopo aver
instaurato il canale di trasmissione sicuro.

.. mermaid::

   sequenceDiagram
   activate Fruitore
   activate Erogatore
   Fruitore->>+Erogatore: 1. Request()
   Erogatore-->>Fruitore: 2. Response
   deactivate Erogatore
   deactivate Fruitore

*Figura 1 - Sicurezza di canale e/o Autenticazione dell’erogatore*

.. _id-auth-channel-01-regole-di-processamento:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Il canale sicuro tra erogatore e fruitore viene instaurato utilizzando
il protocollo TLS, secondo le modalità specificate al capitolo 7
Elementi di sicurezza.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta;

2. Il fruitore spedisce sul canale sicuro stabilito il messaggio di
   richiesta; all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce il risultato.

Come indicato in :rfc:`5246` l’impiego del protocollo TLS garantisce a
livello di canale:

-  l’autenticazione dell’erogatore identificato mediante il certificato
   X.509;

-  la confidenzialità dei dati scambiati;

-  l’integrità dei dati scambiati.

L’impiego del protocollo TLS, mitiga il rischio di:

-  Replay Attack;

-  Spoofing.

[ID_AUTH_CHANNEL_02] Direct Trust mutual Transport-Level Security
-----------------------------------------------------------------

Comunicazione tra fruitore ed erogatore che assicuri a livello di
canale:

-  confidenzialità;

-  integrità;

-  identificazione dell’erogatore e del fruitore, quale organizzazioni;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing.

.. _id-auth-channel-02-descrizione:

Descrizione
^^^^^^^^^^^

Il presente profilo assume l’esistenza di un trust tra fruitore (client)
ed erogatore (server), che permette il riconoscimento da entrambe le
parti dei certificati X.509, o le CA emittenti, così come previsto dal
protocollo Transport Layer Security.

La sequenza dei messaggi di richiesta/risposta avviene dopo aver
instaurato il canale di trasmissione sicuro.

.. mermaid::

    sequenceDiagram
     
    activate Fruitore
	activate Erogatore
    Fruitore->>+Erogatore: 1. Request()
    Erogatore-->>Fruitore: 2. Response
    deactivate Erogatore
     deactivate Fruitore

*Figura 2 - Sicurezza di canale e/o Autenticazione delle organizzazioni*

.. _id-auth-channel-02-regole-di-processamento:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, secondo le modalità
specificate al capitolo 7 Elementi di sicurezza.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce utilizzando canale sicuro stabilito con il il
   messaggio di richiesta all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce il risultato.

Come indicato in :rfc:`5246` l’impiego del protocollo TLS garantisce a
livello di canale:

-  l’autenticazione di erogatore e fruitore identificati mediante
   certificati X.509;

-  la confidenzialità dei dati scambiati;

-  l’integrità dei dati scambiati.

L’impiego del protocollo TLS, mitiga il rischio di:

-  Replay Attack;

-  Spoofing.

