Concetti di base
================

**Interazione bloccante vs non bloccante**                            
                                                                      
Nell’interazione bloccante un fruitore effettua una chiamata al       
servente ed attende una risposta prima di continuare l’esecuzione. La 
chiamata codifica in modo opportuno la richiesta di servizio, anche   
attraverso il passaggio di dati (sia in input alla chiamata che in    
output nella risposta).                                               
                                                                      
Nell’interazione non bloccante, invece, il fruitore invia un          
messaggio ma non si blocca in attesa di alcuna risposta (se non una   
notifica di presa in carico). Il messaggio contiene in modo opportuno 
la richiesta ed eventuali dati di input. Talvolta il messaggio,       
proprio ad indicare il fatto che codifica la richiesta e le           
informazioni necessarie a soddisfarla, viene indicato come documento. 
La risposta da parte del servente, nei casi in cui ci sia, può        
apparire significativamente più tardi, ove significativamente va      
interpretato rispetto al tempo di computazione proprio                
dell’interazione [2]_. Anche la risposta del servente viene inviata   
tramite un messaggio.                                                 
                                                                      
Con abuso di nomenclatura, la comunicazione bloccante talvolta viene  
detta *sincrona*, ad indicare che client e servente si sono           
sincronizzati (attesa di uno da parte dell’altro); quella non         
bloccante viene detta *asincrona*, proprio a significare              
l'asincronicità che vi è tra l'invio di un messaggio e la risposta al 
messaggio stesso.                                                     
                                                                      
*Alonso, G., Casati, F., Kuno, H., Machiraju, V. (2004). Web          
Services. Concepts, Architectures and Applications. Springer*         

------------

**Remote Procedure Call**                                             
                                                                      
Una Remote Procedure Call (chiamata a procedura remota, RPC) consiste 
nell'attivazione, da parte di un programma, di una procedura o        
subroutine attivata su un elaboratore diverso da quello sul quale il  
programma viene eseguito. Quindi l'RPC consente a un programma di     
eseguire subroutine “a distanza” su elaboratori remoti, accessibili   
attraverso una rete. Essenziale al concetto di RPC è l'idea di        
trasparenza: la chiamata di procedura remota deve essere infatti      
eseguita in modo il più possibile analogo a quello della chiamata di  
procedura locale; i dettagli della comunicazione su rete devono       
essere “nascosti” (resi trasparenti) all'utilizzatore del meccanismo. 
Se il linguaggio è orientato agli oggetti, l’invocazione della        
procedura remote è in realtà l’invocazione di un metodo su un oggetto 
remoto, e si parla di Remote Method Invocation - RMI.                 
                                                                      
RPC/RMI è il meccanismo base con cui realizzare una interazione       
bloccante.                                                            

------------

**Observer/observable, interfaccia listener e notifica tramite Callback**                                                            
                                                                      
In un framework di programmazione, *observer/observable* è uno schema 
di organizzazione dei moduli in cui un modulo (l’*observable*) offre  
delle funzioni per permettere agli altri (gli *observer*) di          
registrarsi. Gli observer devono offrire un’interfaccia di *callback* 
(anche detta di *listener*) attraverso cui l’observable, quando vuole 
notificare qualcosa, invoca un’opportuna funzione di notifica. In tal 
modo, gli observer hanno dichiarato in fase di registrazione come     
essere “chiamati indietro” (appunto callback) quando succede          
qualcosa, e l’observable può gestire tutti gli observer registrati in 
modo trasparente, senza conoscere i dettagli realizzativi di ogni     
singola callback, in quanto tutti realizzano la stessa interfaccia,   
differenziandosi eventualmente nell’implementazione.                  
                                                                      
In ambito distribuito, il riferimento passato dagli observer in fase  
di registrazione è rappresentato da un endpoint di rete con tutte le  
informazioni necessarie ad invocare su di esso l’interfaccia          
listener/procedure di callback.                                       
                                                                      
Questo meccanismo permette di realizzare interazioni non bloccanti.   
                                                                      
*D'Souza, D. F., Cameron Wills, A. (1999). Objects, components, and   
frameworks with UML: the Catalysis approach. Addison-Wesley Longman   
Publishing Co.*                                                       

------------

**Façade**                                                            
                                                                      
È uno schema di organizzazione dei moduli in cui uno, detto appunto   
façade, maschera l’accesso ad un insieme di moduli sottostanti, ad    
esempio limitando l’accesso a determinate funzionalità tramite un     
meccanismo di gestione degli accessi, oppure nascondendo le           
complessità nell’organizzazione e gestione dei moduli sottostanti.    

------------

**Idempotenza**                                                       
                                                                      
Il concetto di idempotenza in matematica è una proprietà delle        
funzioni per la quale applicando molteplici volte una funzione data,  
il risultato ottenuto è uguale a quello derivante dall'applicazione   
della funzione un'unica volta (es. gli operatori di intersezione o    
unione). Applicato alle interfacce di servizio, questo concetto       
indica il fatto che una operazione, se eseguita più volte non         
comporta un risultato diverso sul sistema erogatore. Il caso classico 
è quello in cui si ha una operazione di creazione. Nel caso di errore 
di rete, l’operazione potrebbe essere eseguita senza che il fruitore  
riceva un messaggio di risposta. In questo caso il fruitore può       
ritentare la stessa operazione, ma il risultato in questo caso non    
deve essere la creazione di una seconda risorsa. L’erogatore          
dell’interfaccia di servizio deve invece riconoscere la duplicazione  
della richiesta ed evitare comportamenti indesiderati. Questo         
comportamento è solitamente ottenuto tramite l’utilizzo di            
correlation ID oppure tramite il confronto dati basato su dati che    
fungono da chiave.                                                    

------------

**Orchestrazione e coreografia**                                      
                                                                      
Per orchestrazione si intende un flusso di esecuzione che coinvolge   
diverse chiamate a servizi secondo regole prestabilite (ad es., un    
workflow) al fine di ottenere un servizio composto.                   
                                                                      
La coreografia dei servizi è una forma di specifica della             
composizione dei servizi in cui il protocollo di interazione tra i    
diversi servizi componenti è definito da una prospettiva globale.     
Cioè, in fase di esecuzione della coreografia, ogni partecipante      
esegue la sua parte (cioè il suo *ruolo*) in base al comportamento    
degli altri partecipanti. Il ruolo specifica il comportamento, in     
termini di scambi di messaggi attesi dai partecipanti, che            
riproducono il ruolo appunto in termini di sequenziamento e           
tempistica dei messaggi che possono consumare e produrre. La          
specifica dei messaggi implica anche la descrizione dei dati          
scambiati tra due o più partecipanti.                                 
                                                                      
La differenza tra i due approcci è meglio compresa attraverso il    
loro confronto. Da una parte, nelle coreografie, la logica delle    
interazioni basate sui messaggi tra i partecipanti è specificata da 
una prospettiva globale. Nell'orchestrazione dei servizi, d'altra   
parte, la logica viene specificata dal punto di vista locale di un  
singolo partecipante, chiamato l'orchestratore. Nel linguaggio di   
orchestrazione BPEL, ad esempio, la specifica dell'orchestrazione   
del servizio (ad esempio il file del processo BPEL) può essere      
distribuita sull'infrastruttura (ad esempio un motore di esecuzione 
BPEL come Apache ODE), e questo costituisce l’implementazione del   
servizio composto.      

In un certo senso, le coreografie e le orchestrazioni sono due      
facce della stessa medaglia. Da un lato, i ruoli di una coreografia 
possono essere estratti come orchestrazioni attraverso un processo  
chiamato *proiezione*; attraverso la proiezione, è possibile        
realizzare scheletri, ovvero orchestrazioni di servizi incomplete   
che possono essere utilizzate come linee di base per realizzare i   
servizi web che partecipano alla coreografia di servizio. D'altra   
parte, le orchestrazioni già esistenti possono essere composte in   
coreografie.                                                        
                                                                      
*Chris Peltz (2003): Web Services Orchestration and Choreography.     
IEEE Computer 36(10):46-52*                                          

------------

**Classificazione delle interazioni in A2A, A2C e A2B**               
                                                                       
A2A : Administration-to-Administration                                
                                                                      
A2C : Administration-to-Citizen                                       
                                                                      
A2B : Administration-to-Business                                      
                                                                      
In contesti di digital government, è possibile classificare le        
interazioni tra componenti applicativi in base al soggetto            
organizzativo sotto la cui responsabilità e nel cui dominio viene     
eseguito il componente. Si parla di Administration-to-Administration  
quando sia il componente servente (ad esempio l’interfaccia di        
servizio) che quello cliente (ad esempio, applicazione Web,           
applicazione mobile, un altro servizio composto che utilizza il primo 
come componente all’interno della propria orchestrazione, ecc.) sono  
nel dominio delle amministrazioni (che probabilmente saranno          
differenti, ma non necessariamente). Si parla di                      
Administration-to-Citizen quando servente e cliente sono uno nel      
dominio dell’amministrazione e l’altro su dispositivi del privato     
cittadino, mentre Administration-to-Business quando servente e        
cliente sono uno nel dominio dell’amministrazione e l’altro di        
un’organizzazione privata (azienda, concessionario privato di servizi 
pubblici, ecc.). La distinzione è utile non tanto dal punto di vista  
funzionale, ma degli aspetti non funzionali, ad esempio legati al     
trust, alla reciprocità ed ai livelli di sicurezza che devono essere  
instaurati nei vari casi.                                             
                                                                      
**NOTA:** *in alcuni autori/documenti ed in alcuni contesti si        
utilizza l’acronimo A2A come Application-to-Application (ad indicare  
interazioni puramente tra moduli applicativi, senza utenti umani),    
che invece nel ModI è indicato come M2M (cf. voce relativa). Nel ModI 
A2A è usata sempre e solo ad indicare interazioni                     
Administration-to-Administration.*                                    

------------

**Classificazione delle interazioni in M2M e U2M**
                                                                     
M2M : Machine-to-Machine                                              
                                                                      
U2M : User-to-Machine                                                 
                                                                      
In contesti di interoperabilità tra pubbliche amministrazioni,        
cittadini ed imprese, è utile classificare le interazioni tra sistemi 
informativi differenti come:                                          
                                                                      
-  Machine-to-Machine, quando i due sistemi informativi interagiscono 
   (scambiando dati) a livello applicativo, e l’identificazione del   
   client verso il fornitore di interfacce di servizio è demandato ad 
   un identity provider operante all’interno del dominio applicativo  
   dal quale il client opera.                                         
                                                                      
-  User-to-Machine, quando i sistemi informativi interagiscono,       
   sempre attraverso la mediazione di un utente umano, ad esempio il  
   cittadino oppure un funzionario di una pubblica amministrazione, e 
   l’identificazione del client verso il fornitore è demandata ad un  
   identity provider differente rispetto al dominio del client.       
                                                                      
A scopo esemplificativo, si considerino i seguenti casi:              
                                                                      
1. cittadino che utilizza una Web/mobile app per fruire dei servizi   
   di una pubblica amministrazione. Si è nel caso U2M, in quanto i    
   moduli applicativi (app client ed interfaccia di servizio)         
   interoperano, ma tale interazione è operata con l’utente che ha    
   fornito le proprie credenziali e queste sono utilizzate da un      
   identity provider differente dal suo dominio (ad es., un identity  
   provider commerciale oppure la stessa pubblica amministrazione     
   servente) per creare il contesto di sicurezza;                     
                                                                      
2. operatore di una pubblica amministrazione A che interopera,        
   attraverso un’applicazione, con un’interfaccia di servizio presso  
   la pubblica amministrazione B. In questo caso, il sistema          
   informativo della pubblica amministrazione A riconosce il proprio  
   operatore, e quando il modulo applicativo si presenta presso la    
   pubblica amministrazione B lo fa con il contesto di sicurezza      
   dell’amministrazione A, in modo trasparente rispetto allo          
   specifico operatore ed alla sua identità; siamo quindi nel caso    
   M2M;                                                               
                                                                      
3. modulo software di una amministrazione A che in modalità *batch*   
   ed *unattended* utilizza un’interfaccia di servizio                
   dell’amministrazione B. Di nuovo il caso è M2M.                    
                                                                      
La differenza U2M e M2M è significativa in termini di quale soggetto  
ha il carico di riconoscere le identità del client e fornire l’AA -   
authentication ed authorization. In particolare nei 3 esempi          
precedente                                                            
                                                                      
-  caso 1, U2M - la gestione delle identità è demandata all’identity  
   provider (nel caso che sia terzo/commerciale) ma la pubblica       
   amministrazione servente ha il compito di censire tutte le         
   identità e per ognuna fornire l’AA; oppure è la pubblica           
   amministrazione stessa gestisce le identità. In ogni caso le       
   spetta l’onere di gestire l’AA di ogni singola identità.           
                                                                      
-  casi 2 e 3, M2M - la pubblica amministrazione B servente riconosce 
   ed AA un solo soggetto, la pubblica amministrazione A, ed è questa 
   che invece ha l’onere di riconoscere le identità e dare loro l’AA  
   per interoperare con B.                                            
                                                                      
Quindi emerge come la discriminante sia da parte dell’amministrazione 
fornitrice di interfacce di servizio, se è in suo carico di gestire   
ed AA le identità o meno.                                             

------------

**Impedance mismatch**                                                
                                                                      
Derivato dall’\ *impedance mismatch* dell’elettrotecnica, si          
riferisce alle difficoltà concettuali e tecniche che si incontrano    
spesso quando due paradigmi differenti, spesso implicati da           
altrettante tecnologie, devono coesistere e mapparsi uno sull’altro   
durante la progettazione e realizzazione di un sistema.               
                                                                      
Il più famoso caso di impedance mismatch è quello                   
dell’object-to-relational, noto metaforicamente anche come il       
Vietnam dell’informatica [4]_, che si verifica quando un sistema di 
gestione di database relazionali (RDBMS) è servito da un programma  
applicativo (o da più programmi applicativi) scritto in un          
linguaggio di programmazione orientato agli oggetti, in particolare 
perché gli oggetti o le definizioni di classe devono essere         
associati a tabelle di database definite da uno schema relazionale. 
Nel ModI ci sono casi di impedance mismatch quando             
un’interfaccia di servizio progettata secondo lo stile RPC-like     
deve essere realizzata in REST.                                     

.. [1]
   Ad es., se fruitore ed erogatore computano nell’ordine dei secondi,
   la risposta potrebbe arrivare dopo minuti od ore, quindi
   significativamente più tardi.

.. [2]
   Ad es., se fruitore ed erogatore computano nell’ordine dei secondi,
   la risposta potrebbe arrivare dopo minuti od ore, quindi
   significativamente più tardi.

.. [3]
   Cf. http://blogs.tedneward.com/post/the-vietnam-of-computer-science/

.. [4]
   Cf. http://blogs.tedneward.com/post/the-vietnam-of-computer-science/
   
.. discourse::
   :topic_identifier: XXXX
   
