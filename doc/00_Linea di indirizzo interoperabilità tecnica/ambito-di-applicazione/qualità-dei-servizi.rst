Qualità dei servizi
===================

Il concetto di qualità di servizio, anche comunemente chiamata Quality
of Service (QoS), fa riferimento alla descrizione non funzionale di una
API, cioè alla capacità di quest’ultima di soddisfare le aspettative dei
fruitori. Assicurare la QoS nell’ambito Internet ai fini
dell’interoperabilità è una sfida critica a causa della natura dinamica
e impredicibile del contesto applicativo. Cambiamenti negli schemi di
traffico, la presenza di transazioni critiche, gli effetti dei problemi
di rete, le performance dei protocolli e degli standard di rete
richiedono una definizione precisa della QoS offerta da una interfaccia
di servizio.

Gli elementi chiave a supporto della QoS possono essere riassunti come
segue:

-  Disponibilità. La probabilità che una interfaccia di servizio sia
   disponibile e funzionante in un istante casuale. Associato al
   concetto di disponibilità è quello di Time-To-Repair (TTR), cioè il
   tempo necessario a ripristinare una interfaccia di servizio una volta
   che questa diventa indisponibile. La disponibilità di una interfaccia
   di servizio dovrebbe potere essere verificata tramite l’esposizione
   di un’altra interfaccia di servizio di monitoraggio, dedicata e a
   basso impatto (quindi a elevata disponibilità);

-  Accessibilità. Misura la capacità di una interfaccia di servizio di
   essere contattabile da un elevato numero di richieste;

-  Prestazioni. Le prestazioni vengono misurate solitamente rispetto a
   due valori: il throughput e la latenza. Il throughput rappresenta il
   numero di richieste soddisfatte in un dato intervallo. La latenza
   rappresenta la quantità di tempo che passa tra l’invio di una
   richiesta e la ricezione di una risposta. Un’interfaccia di servizio
   con buone prestazioni ha un elevato throughput e una bassa latenza;

-  Affidabilità. Rappresenta la capacità di una interfaccia di servizio
   di funzionare correttamente e consistentemente, fornendo la stessa
   QoS a dispetto di malfunzionamenti di diversa natura. Di solito è
   espressa in termini di fallimenti in un dato lasso di tempo;

-  Scalabilità. L’abilità di servire in modo consistente, efficiente e
   performante le richieste all'aumentare o al diminuire del loro
   numero. È strettamente connessa al concetto di accessibilità;

-  Sicurezza. La sicurezza implica aspetti quali confidenzialità,
   integrità, autorizzazione e autenticazione;

-  Transazionalità. Ci sono alcuni casi (ad es., API stateful) in cui è
   necessario assicurare l’esecuzione transazionale di una operazione.
   La capacità di una operazione di rispettare questa proprietà è parte
   della QoS.

Gli erogatori di e-service devono prendere tutte le iniziative
necessarie a mantenere i requisiti di QoS richiesti dal caso d’uso.
Questo include anche l’utilizzo di buone pratiche, ad esempio, per
assicurare prestazioni e scalabilità, il risparmio della banda è una
condizione fondamentale.
