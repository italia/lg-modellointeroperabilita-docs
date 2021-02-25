[ID_AUTH_CHANNEL_02] Direct Trust mutual Transport-Level Security
-----------------------------------------------------------------

Comunicazione tra fruitore ed erogatore che assicuri a livello di
canale:

-  confidenzialità;

-  integrità;

-  identificazione dell’erogatore e del fruitore, quale organizzazioni;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing.

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

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, 
secondo quanto indicato nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce utilizzando il canale sicuro stabilito con il
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

.. forum_italia::
   :topic_id: 21467
   :scope: document
