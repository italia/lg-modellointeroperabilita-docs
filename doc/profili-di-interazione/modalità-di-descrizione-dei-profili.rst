Modalità di descrizione dei profili
========================================

Nel seguito, per gli esempi proposti per i diversi profili si fa
riferimento ad un’amministrazione denominata ``amministrazioneesempio`` che
offre un’interfaccia di servizio secondo le due diverse tecnologie REST
o SOAP. Inoltre, per quanto riguarda i profili relativi a chiamata a
procedura remota (bloccante e non bloccante), si farà riferimento ad un
metodo ``M`` che accetta come parametri:

-  ``a``, un oggetto contenente a sua volta un array ``a1`` di interi ed una
   stringa ``a2``;

-  ``b``, una stringa.

e restituisce una stringa ``c`` come output. Si suppone in tutti i profili
che l’accesso alle interfacce di servizio sia subordinato all’utilizzo
di meccanismi di autenticazione ed autorizzazione che permettano
all’erogatore di associare una specifica richiesta ad uno specifico
fruitore.

Per ognuno dei profili verrà introdotto:

-  lo scenario di applicazione (sottosezione Scenario), che indica in
   che casi vada utilizzato lo specifico profilo;

-  la descrizione (sottosezione Descrizione) dello scambio di messaggi a
   livello applicativo, indipendentemente quindi dalla tecnologia
   utilizzata;

-  una sezione che riguarda l’utilizzo della tecnologia REST
   (sottosezione REST) per lo specifico profilo, che include una sezione
   con le regole generali da seguire e l’implementazione dell’esempio
   proposto;

-  una sezione che riguarda l’utilizzo della tecnologia SOAP
   (sottosezione SOAP) per lo specifico profilo, che include una sezione
   con le regole generali da seguire e l’implementazione dell’esempio
   proposto.

Le implementazioni degli esempi sono corredate dalla specifica
dell’interfaccia e da uno scambio di messaggi esemplificativo.
