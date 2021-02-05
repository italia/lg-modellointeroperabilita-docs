Pattern non bloccante RPC PUSH (basato su callback)
===================================================

Questo caso particolare, denominato RPC PUSH, è utilizzabile nel caso in
cui il fruitore abbia a sua volta la possibilità di esporre una
interfaccia di servizio per la ricezione delle risposte.

.. mermaid::

   sequenceDiagram
     activate Fruitore
     activate Erogatore
     Fruitore->>+Erogatore: 1. Request(callback endpoint)
     Erogatore-->>Fruitore: 2. CorrelationID
     Erogatore->>Fruitore: 3. Reply(CorrelationID)
     Fruitore-->>Erogatore: 4. Ack
     deactivate Erogatore
     deactivate Fruitore

*Figura 2 - Interazione non bloccante tramite callback*

In questo pattern (vedi figura), la richiesta del fruitore contiene un
riferimento al servizio da chiamare al momento della risposta. Si
suppone infatti che i fruitori espongano a loro volta delle interfacce
con segnatura standard. Al momento del ricevimento della richiesta
(passo 1), l’erogatore risponde (passo 2) riconoscendo l’avvenuta
ricezione (acknowledgement o in breve ack) ed indica un CorrelationID
(ID di correlazione), generato lato erogatore, che permetta al fruitore,
una volta ricevuta la risposta, di accoppiarla alla richiesta originale.
Quando il processamento è terminato infatti, l’erogatore (passo 3)
chiama il fruitore (invertendo quindi i ruoli chiamato/chiamante)
riportando l’esito ed indicando il CorrelationID. Il fruitore riconosce
(sempre mediante un messaggio di ack) la ricezione della risposta (passo
4).

.. toctree::
  :maxdepth: 3

  01_nonblock_push/01_nonblock_push_rest.rst
  01_nonblock_push/02_nonblock_push_soap.rst

.. forum_italia::
   :topic_id: 21455
   :scope: document
