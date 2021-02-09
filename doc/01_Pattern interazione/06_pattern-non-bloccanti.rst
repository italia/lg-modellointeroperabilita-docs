Pattern non bloccanti
=====================

I pattern di interazione non bloccanti di tipo RPC-like sono quelli in cui un
fruitore invia una richiesta e questa viene solo presa in carico
immediatamente, mentre il suo soddisfacimento può avvenire in maniera
differita. Gli approcci non bloccanti vengono utilizzati nei casi in cui
i tempi per l’erogazione di una risposta da parte del fruitore sono
lunghi perché

-  la richiesta è onerosa in termini temporali;

-  il fruitore non può farsi immediatamente carico dell’erogazione del
   servizio.

Al fine di collegare le richieste con le risposte si farà uso, sia nelle
implementazioni SOAP che in quelle REST, di meta-informazioni specifiche
(quali il CorrelationID e l’endpoint per le callback). Queste sono
estranee solitamente alla business logic del servizio, ma è necessario
definirle a livello di API ai fini dell’interoperabilità. A tal fine
verranno definiti header (HTTP nel caso REST ed envelope nel caso SOAP)
utili a contenere queste informazioni. In alcuni casi, una API viene
creata al fine di automatizzare o semplificare un servizio già offerto
dalla pubblica amministrazione. In una moltitudine di casi questi
servizi sono asincroni (non bloccanti) per natura, e consistono di
richieste a cui vengono allegati degli identificativi (es. numeri di
protocollo) che accompagnano la richiesta. In questi casi, il
CorrelationID può essere sostituito da questi identificativi già
previsti dal servizio.

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
  :caption: Indice dei contenuti

  06_pattern-non-bloccanti/01_nonblock_push.rst
  06_pattern-non-bloccanti/02_nonblock_pull.rst

.. forum_italia::
   :topic_id: 21454
   :scope: document
