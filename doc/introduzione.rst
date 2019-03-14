Introduzione
============

Il presente documento descrive i *profili* individuati da AgID che la
Pubblica Amministrazione DOVREBBE utilizzare per soddisfare le proprie
necessità espresse attraverso requisiti funzionali e non funzionali.

I profili:

-  definiscono a livello di specifica tecnologica uno “strumento
   condiviso” utile a favorire l’interoperabilità tra le pubbliche
   amministrazione, cittadini ed imprese.

-  forniscono un comune linguaggio per richiedenti ed erogatori utile a
   trattare le necessità e le caratteristiche delle *interfacce di
   servizio*.

-  offrono agli sviluppatori le modalità tecniche supportate da standard
   tecnologici documentati, revisionati e testati per esporre i *servizi
   digitali* fornendo indicazioni in risposta alle necessità.

I profili affrontano il tema della sicurezza su due livelli differenti:

-  **Canale**: definisce le modalità di trasporto dei messaggi tra i
   confini dei *domini* delle entità coinvolte.

-  **Messaggio**: definisce le modalità di comunicazione dei messaggi
   tra componenti interne dei *domini* delle entità coinvolte.

Ogni profilo è strutturato come segue:

-  **Scenario:** definizione dei requisiti funzionali e non funzionali
   soddisfatti dall’implementazione del profilo.

-  **Descrizione:** rappresentazione in linguaggio naturale del profilo
   con relativi precondizioni e obiettivi.

-  **Dettaglio:**

   -  **Flusso delle interazioni:** descrizione delle interazioni tra le
      2 part alle interfacce.

   -  **Regole di processamento:** elenco dei passi da eseguire per
      implementare il profilo.

   -  **Tracciato:** ove presente, fornisce un esempio dei messaggi
      prodotti nell’interazione.

Le Pubbliche Amministrazioni, a seguito dell’\ **analisi dei requisiti**
realizzata internamente, per individuare le proprie esigenze funzionali
e non funzionali, DOVREBBE:

1. individuare tra i *profili di interazione* quelli che soddisfano le
   proprie esigenze;

2. individuare tra i *profili di sicurezza* quelli che soddisfano le
   proprie esigenze;

3. implementare le *interfacce di servizio* attraverso la combinazione
   dei *profili di interazione* e di *profili di sicurezza*.

L’individuazione dei *profili* DEVE ricoprire **solamente** i requisiti
necessari, inoltre la scelta dei profili da implementare risulta
necessaria ove l’ente erogatore del servizio non disponga già di
tecnologie che garantiscano i requisiti richiesti.

.. toctree::
  :maxdepth: 3
  :caption: Indice dei contenuti

  introduzione/trust.rst
  introduzione/modalità-di-combinazione-dei-profili.rst
