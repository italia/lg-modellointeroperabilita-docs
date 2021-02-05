Pattern bloccanti
=================

Lo sviluppo di una interfaccia bloccante di tipo RPC-like si richiede
nei casi in cui:

-  L’esecuzione del metodo è poco onerosa computazionalmente e può
   essere portata immediatamente a termine dall’erogatore.

-  Il contesto rende complessa l’implementazione delle modalità non
   bloccanti. Ad esempio, non è possibile per il fruitore esporre una
   propria interfaccia di servizio ed il fruitore non può farsi carico
   di mantenere il contesto necessario ad effettuare attesa attiva.

.. mermaid::

   sequenceDiagram
   activate Fruitore
   activate Erogatore
   Fruitore->>+Erogatore: 1. Request()
   Erogatore-->>Fruitore: 2. Response
   deactivate Erogatore
   deactivate Fruitore

*Figura 1 - Interazione bloccante RPC*

In questo pattern si ha una risposta da parte dell’erogatore contestuale
alla richiesta del fruitore. La figura mostra lo schema di questa
interazione.

Nel seguito, per gli esempi proposti si fa riferimento ad
un’amministrazione denominata **ente.example** che offre un’interfaccia
di servizio secondo le due diverse tecnologie REST o SOAP. Inoltre, per
quanto riguarda i pattern relativi a chiamata a procedura remota
(bloccante e non bloccante), si farà riferimento ad un metodo **M** che
accetta come parametri:

-  **a**, un oggetto contenente a sua volta un array **a1** di interi ed
   una stringa **a2**;

-  **b**, una stringa;

e restituisce una stringa **c** come output.

Le implementazioni degli esempi sono corredate dalla specifica
dell’interfaccia e da uno scambio di messaggi esemplificativo.

Di seguito le indicazioni per le tecnologie accolte dal ModI.

L'AgID assicura l'aggiornamento degli stessi per soddisfare le esigenze 
espresse dalle PA.

.. toctree::
  :maxdepth: 3

  05_pattern-bloccanti/01_block_rest.rst
  05_pattern-bloccanti/02_block_soap.rst

.. forum_italia::
   :topic_id: 21451
   :scope: document
