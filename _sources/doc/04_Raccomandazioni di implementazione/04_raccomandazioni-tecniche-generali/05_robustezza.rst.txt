Raccomandazioni sulla robustezza 
--------------------------------

Ai fini di garantire la responsività di una API è necessario impedire a
singoli fruitori di esaurire la capacità di calcolo e di banda
dell’erogatore. La tecnica comunemente utilizzata in questi casi è il
rate limiting (anche noto come throttling). Il rate limit fornisce ad
uno specifico fruitore un numero massimo di richieste soddisfacibili
all’interno di uno specifico arco temporale (es. 1000 richieste al
minuto). Un numero di richieste che superi il limite imposto provoca il
rifiuto di ulteriori richieste da parte di uno specifico fruitore per un
intervallo di tempo predeterminato.

Sulle politiche riguardanti il numero massimo di richieste e la relativa
finestra temporale, e quelle riguardanti il tempo di attesa per nuove
richieste (che può essere incrementato in caso di richieste reiterate,
es. con una politica di aumento esponenziale) si lascia libertà agli
implementatori previa un’analisi di carico massimo sopportabile
dall’erogatore.

[RAC_ROBUSTEZZA_001] Segnalare raggiunti limiti di utilizzo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli erogatori di interfacce di servizio REST DEVONO segnalare eventuali
limiti raggiunti con :httpstatus:`429`.

Le API restituiscono in ogni risposta i valori globali di throttling
tramite i seguenti header [1]_:

-  X-RateLimit-Limit: limite massimo di richieste per un endpoint;

-  X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo
   reset;

-  X-RateLimit-Reset: numero di secondi che mancano al prossimo reset.

In caso di superamento delle quote, le API DEVONO restituire anche
l’header:

-  :httpheader:`Retry-After` : numero minimo di secondi dopo cui il client
   è invitato a riprovare [2]_.

Nel caso di SOAP non esistono regole guida standard per la gestione del
rate limit e del throttling. Si POSSONO utilizzare gli stessi header e
status code HTTP visti nel caso REST.

I fruitori DEVONO:

-  rispettare gli header di throttling;

-  rispettare l’header X-RateLimit-Reset quando restituisce il numero di
   secondi che mancano al prossimo reset, ed eventualmente gestire
   l’indicazione in timestamp unix;

-  rispettare l’header :httpheader:`Retry-After` sia nella variante che
   espone il numero di secondi dopo cui riprovare, sia nella variante
   che espone la data in cui riprovare.

[RAC_ROBUSTEZZA_002] Segnalare il sovraccarico del sistema o l’indisponibilità del servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli erogatori DEVONO definire ed esporre un piano di continuità
operativa segnalando il sovraccarico del sistema o l’indisponibilità del
servizio con :httpstatus:`503` Service Unavailable.

In caso di sovraccarico o indisponibilità, l’erogatore DEVE ritornare
anche:

-  :httpheader:`Retry-After` con il numero minimo di secondi dopo cui il
   client è invitato a riprovare.

I fruitori DEVONO:

-  rispettare :httpheader:`Retry-After` sia nella variante che espone il
   numero di secondi dopo cui riprovare, sia nella variante che espone
   la data in cui riprovare.

Per REST si DEVE prevedere nella descrizione delle API l'indicazione
degli header relativi al rate limiting. L’utilizzo degli header HTTP in
SOAP è fuori dagli obiettivi di WSDL come Interface Definition Language.

Esempio di specifica API REST per applicazione del throttling e
segnalazione del sovraccarico o dell’indisponibilità:

.. literalinclude:: media/RAC_ROBUSTEZZA_001_RAC_ROBUSTEZZA_002_example.yaml
   :language: yaml

Di seguito, un esempio di chiamata alle API, con risposta nel caso in
cui i limiti non siano ancora stati raggiunti e nel caso in cui invece
il fruitore debba attendere per presentare nuove richieste.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Host: api.ente.example
   Content-Type: application/json
   
   {
   "a": {
	   "a1": [1, "...", 2],
	   "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
	   },
   "b": "Stringa di esempio"
   }


2. Response 200 con rate limiting

.. code-block:: http

   HTTP/1.1 200 OK
   X-RateLimit-Limit: 30
   X-RateLimit-Remaining: 11
   X-RateLimit-Reset: 44
   
   {"c" :"risultato"}


2. Response 429 Too Many Requests

.. code-block:: http

   HTTP/1.1 429 Too Many Requests
   Content-Type: application/problem+json
   Retry-After: 60
   
   {
   "status": 429,
   "title": "Hai superato la quota di richieste."
   }

2. Response 503 Service Unavailable

.. code-block:: http

   HTTP/1.1 503 Service Unavailable
   Content-Type: application/problem+json
   Retry-After: 3600
   
   {
   "status": 503,
   "title": "Servizio in manutenzione."
   }

[RAC_ROBUSTEZZA_003] Uniformità di Indicatori ed Obiettivi di Servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli SLI pubblicati DEVONO:

-  utilizzare unità di misure referenziate dal Sistema Internazionale
   (ad esempio, secondi o bytes);

-  indicare nel nome identificativo l’eventuale periodo di aggregazione
   con i soli suffissi s (secondi), m (minuti), d (giorni) e y (anni),
   utilizzando al posto dei mesi il numero di giorni;

-  includere la latenza aggiuntiva dovuta ad eventuali componenti
   infrastrutturali e di rete (ad esempio, proxy o gateway).

Gli SLO e gli SLA DOVREBBERO essere in relazione diretta con i valori
associati (ad esempio, indicare il success rate anziché l’error rate),
in modo che a valori più alti corrispondano risultati positivi.

Alcuni esempi di indicatori a cui è possibile associare degli obiettivi
o degli accordi:

-  dimensione massima di ogni richiesta accettata. Le richieste più
   grandi possono essere rifiutate
   
-  latenza al 90º percentile. Utilizzata per calcolare la
   responsività
   
-  percentuale di minuti negli ultimi 30 giorni in cui l’interfaccia
   di servizio è stata disponibile
   
-  valori a 30 giorni del success rate, ovvero il numero di chiamate
   terminate con successo rispetto al numero totale di chiamate
   
-  Application Performance inDEX [3]_, indice su scala percentuale di
   qualità del servizio misurato a 30 giorni
   
-  tempo di risposta medio delle richieste totali (includendo le
   richieste rifiutate a causa del throttling) negli ultimi 30 giorni
   
-  throughput misurato in byte/s

.. [1]
   È in corso il processo di standardizzazione dell’utilizzo degli
   header indicati
   https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/

.. [2]
   Cfr. :rfc:`7231` prevede che l’header :httpheader:`Retry-After` possa
   essere utilizzato sia in forma di data che di secondi

.. [3]
   Cf. https://en.wikipedia.org/wiki/Apdex

.. forum_italia::
   :topic_id: 21491
   :scope: document
