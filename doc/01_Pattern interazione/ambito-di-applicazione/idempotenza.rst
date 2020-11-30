Idempotenza
===========

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
