Principi generali
=================

Interazione bloccante e non bloccante
-------------------------------------

Nell’*interazione bloccante* un fruitore effettua una chiamata al servente
ed attende una risposta prima di continuare l’esecuzione. La chiamata
codifica in modo opportuno la richiesta di servizio, anche attraverso il
passaggio di dati (sia in input alla chiamata che in output nella
risposta).

Nell’*interazione non bloccante*, invece, il fruitore invia un messaggio,
ma non si blocca in attesa di alcuna risposta (se non una notifica di
presa in carico). Il messaggio contiene in modo opportuno la richiesta
ed eventuali dati di input. Talvolta il messaggio, proprio ad indicare
il fatto che codifica la richiesta e le informazioni necessarie a
soddisfarla, viene indicato come documento. La risposta da parte del
servente, nei casi in cui ci sia, può apparire significativamente più
tardi, ove "significativamente" va interpretato rispetto al tempo di
computazione proprio dell’interazione. Anche la risposta del servente
viene inviata tramite un messaggio.

Con abuso di nomenclatura, la comunicazione bloccante talvolta viene
detta sincrona, ad indicare che client e servente si sono sincronizzati
(attesa di uno da parte dell’altro); quella non bloccante viene detta
asincrona, proprio a significare l’asincronicità che vi è tra l’invio di
un messaggio e la risposta al messaggio stesso.

*Alonso, G., Casati, F., Kuno, H., Machiraju, V. (2004). Web Services.
Concepts, Architectures and Applications. Springer*

Remote Procedure Call
---------------------

Una Remote Procedure Call (chiamata a procedura remota, RPC) consiste
nell’attivazione, da parte di un programma, di una procedura o
subroutine attivata su un elaboratore potenzialmente diverso da quello sul quale il
programma viene eseguito. Quindi l’RPC consente a un programma di
eseguire subroutine «a distanza» su elaboratori remoti, accessibili
attraverso una rete. Essenziale al concetto di RPC è l’idea di
trasparenza: la chiamata di procedura remota deve essere infatti
eseguita in modo il più possibile analogo a quello della chiamata di
procedura locale; i dettagli della comunicazione su rete devono essere
«nascosti» (resi trasparenti) all’utilizzatore del meccanismo.
I problemi di comunicazione possono essere gestiti anch'essi in modo trasparente,
oppure generare errori o eccezioni.
Se il linguaggio è orientato agli oggetti, l’invocazione della procedura
remote è in realtà l’invocazione di un metodo su un oggetto remoto, e si
parla di Remote Method Invocation - RMI.

RPC/RMI è il meccanismo base con cui realizzare una interazione
bloccante.

Idempotenza
-----------

Il concetto di idempotenza in matematica è una proprietà delle funzioni
per la quale applicando molteplici volte una funzione data, il risultato
ottenuto è uguale a quello derivante dall’applicazione della funzione
un’unica volta (es. gli operatori di intersezione o unione). Applicato
alle interfacce di servizio, questo concetto indica il fatto che una
operazione, se eseguita più volte non comporta un risultato diverso sul
sistema erogatore. Il caso classico è quello in cui si ha una operazione
di creazione. Nel caso di errore di rete, l’operazione potrebbe essere
eseguita senza che il fruitore riceva un messaggio di risposta. In
questo caso il fruitore può ritentare la stessa operazione, ma il
risultato in questo caso non deve essere la creazione di una seconda
risorsa. L’erogatore dell’interfaccia di servizio deve invece
riconoscere la duplicazione della richiesta ed evitare comportamenti
indesiderati. Questo comportamento è solitamente ottenuto tramite
l’utilizzo di CorrelationID oppure tramite il confronto dati basato su
dati che fungono da chiave.

.. forum_italia::
   :topic_id: 21450
   :scope: document
