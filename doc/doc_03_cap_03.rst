Concetti di base
================

**Interazione bloccante vs non bloccante**

Nell'interazione bloccante un fruitore effettua una chiamata al
servente ed attende una risposta prima di continuare l'esecuzione. La
chiamata codifica in modo opportuno la richiesta di servizio, anche
attraverso il passaggio di dati (sia in input alla chiamata che in
output nella risposta).

Nell'interazione non bloccante, invece, il fruitore invia un
messaggio ma non si blocca in attesa di alcuna risposta (se non una
notifica di presa in carico). Il messaggio contiene in modo opportuno
la richiesta ed eventuali dati di input. Talvolta il messaggio,
proprio ad indicare il fatto che codifica la richiesta e le
informazioni necessarie a soddisfarla, viene indicato come documento.
La risposta da parte del servente, nei casi in cui ci sia, può
apparire significativamente più tardi, ove significativamente va
interpretato rispetto al tempo di computazione proprio
dell'interazione [2]_. Anche la risposta del servente viene inviata
tramite un messaggio.

Con abuso di nomenclatura, la comunicazione bloccante talvolta viene
detta *sincrona*, ad indicare che client e servente si sono
sincronizzati (attesa di uno da parte dell'altro); quella non
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
eseguire subroutine "a distanza" su elaboratori remoti, accessibili
attraverso una rete. Essenziale al concetto di RPC è l'idea di
trasparenza: la chiamata di procedura remota deve essere infatti
eseguita in modo il più possibile analogo a quello della chiamata di
procedura locale; i dettagli della comunicazione su rete devono
essere "nascosti" (resi trasparenti) all'utilizzatore del meccanismo.
Se il linguaggio è orientato agli oggetti, l'invocazione della
procedura remote è in realtà l'invocazione di un metodo su un oggetto
remoto, e si parla di Remote Method Invocation - RMI.

RPC/RMI è il meccanismo base con cui realizzare una interazione
bloccante.

------------

**Façade**

È uno schema di organizzazione dei moduli in cui uno, detto appunto
façade, maschera l'accesso ad un insieme di moduli sottostanti, ad
esempio limitando l'accesso a determinate funzionalità tramite un
meccanismo di gestione degli accessi, oppure nascondendo le
complessità nell'organizzazione e gestione dei moduli sottostanti.

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
di rete, l'operazione potrebbe essere eseguita senza che il fruitore
riceva un messaggio di risposta. In questo caso il fruitore può
ritentare la stessa operazione, ma il risultato in questo caso non
deve essere la creazione di una seconda risorsa. L'erogatore
dell'interfaccia di servizio deve invece riconoscere la duplicazione
della richiesta ed evitare comportamenti indesiderati. Questo
comportamento è solitamente ottenuto tramite l'utilizzo di
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
BPEL come Apache ODE), e questo costituisce l'implementazione del
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
quando sia il componente servente (ad esempio l'interfaccia di
servizio) che quello cliente (ad esempio, applicazione Web,
applicazione mobile, un altro servizio composto che utilizza il primo
come componente all'interno della propria orchestrazione, ecc.) sono
nel dominio delle amministrazioni (che probabilmente saranno
differenti, ma non necessariamente). Si parla di
Administration-to-Citizen quando servente e cliente sono uno nel
dominio dell'amministrazione e l'altro su dispositivi del privato
cittadino, mentre Administration-to-Business quando servente e
cliente sono uno nel dominio dell'amministrazione e l'altro di
un'organizzazione privata (azienda, concessionario privato di servizi
pubblici, ecc.). La distinzione è utile non tanto dal punto di vista
funzionale, ma degli aspetti non funzionali, ad esempio legati al
trust, alla reciprocità ed ai livelli di sicurezza che devono essere
instaurati nei vari casi.

------------

**Impedance mismatch**

Derivato dall'*impedance mismatch* dell'elettrotecnica, si
riferisce alle difficoltà concettuali e tecniche che si incontrano
spesso quando due paradigmi differenti, spesso implicati da
altrettante tecnologie, devono coesistere e mapparsi uno sull'altro
durante la progettazione e realizzazione di un sistema.

Il più famoso caso di impedance mismatch è quello
dell'object-to-relational, noto metaforicamente anche come il
Vietnam dell'informatica [4]_, che si verifica quando un sistema di
gestione di database relazionali (RDBMS) è servito da un programma
applicativo (o da più programmi applicativi) scritto in un
linguaggio di programmazione orientato agli oggetti, in particolare
perché gli oggetti o le definizioni di classe devono essere
associati a tabelle di database definite da uno schema relazionale.
Nel ModI ci sono casi di impedance mismatch quando
un'interfaccia di servizio progettata secondo lo stile RPC-like
deve essere realizzata in REST.

.. [1]
   Ad es., se fruitore ed erogatore computano nell'ordine dei secondi,
   la risposta potrebbe arrivare dopo minuti od ore, quindi
   significativamente più tardi.

.. [2]
   Ad es., se fruitore ed erogatore computano nell'ordine dei secondi,
   la risposta potrebbe arrivare dopo minuti od ore, quindi
   significativamente più tardi.

.. [3]
   Cf. http://blogs.tedneward.com/post/the-vietnam-of-computer-science/

.. [4]
   Cf. http://blogs.tedneward.com/post/the-vietnam-of-computer-science/

.. discourse::
   :topic_identifier: 8905

