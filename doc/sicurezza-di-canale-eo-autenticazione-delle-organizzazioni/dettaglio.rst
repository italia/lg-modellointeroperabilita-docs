2.3. Dettaglio
==============

|image0|

2.3.0.1. Flusso delle interazioni
---------------------------------

Tra erogatore e fruitore viene instaurato un canale di trasmissione
sicuro; il flusso dei messaggi avviene secondo la sequenza:

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

**B: Risultato**

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

2.3.0.2. Regole di processamento
--------------------------------

Il canale sicuro tra erogatore e fruitore viene instaurato utilizzando
il protocollo TLS, secondo le modalità specificate alla sezione `Elenco
degli algoritmi <#elenco-degli-algoritmi>`__ .

**A: Richiesta**

1. Il richiedente costruisce un messaggio di richiesta.

2. Il richiedente spedisce sul canale sicuro stabilito il messaggio di
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

.. |image0| image:: ./media/image3.png
   :width: 2.34375in
   :height: 1.28125in
