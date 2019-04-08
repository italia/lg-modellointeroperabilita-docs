Robustezza
==========

Ai fini di garantire la responsività di una interfaccia di servizio, è
necessario impedire a singoli fruitori di esaurire la capacità di
calcolo dell’erogatore. La tecnica comunemente utilizzata in questi casi
è il rate limiting (anche noto come throttling). Il rate limit fornisce
ad uno specifico fruitore un numero massimo di richieste soddisfacibili
all’interno di uno specifico arco temporale (es. 1000 richieste al
minuto). Un numero di richieste che superi il limite imposto provoca il
rifiuto di ulteriori richieste da parte di uno specifico fruitore per un
intervallo di tempo. Sulle politiche riguardanti il numero massimo di
richieste e la relativa finestra temporale, e quelle riguardanti il
tempo di attesa per nuove richieste (che può essere incrementato in caso
di richieste reiterate, es. con una politica di aumento esponenziale) si
lascia libertà agli implementatori previa un'analisi di carico massimo
sopportabile dall'erogatore.

Segnalare raggiunti limiti di utilizzo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gli erogatori di interfacce di servizio REST DEVONO segnalare eventuali
limiti raggiunti con **HTTP 429 (too many requests)**.

Le API restituiscono in ogni response i valori globali di throttling
tramite i seguenti header:

-  X-RateLimit-Limit: limite massimo di richieste per un endpoint

-  X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo
   reset

-  X-RateLimit-Reset: il numero di secondi che mancano al prossimo reset

In caso di superamento delle quote, le API restituiscono anche l'header:

-  Retry-After: il numero minimo di secondi dopo cui il client è
   invitato a riprovare [1]_

Nel caso di interfacce di servizio SOAP non esistono regole guida
standard per la gestione del rate limit e del throttling. Si suggerisce
l'utilizzo degli stessi header e status code HTTP visti nel caso REST.


I fruitori devono:

-  rispettare gli header di throttling

-  rispettare l'header ​X-RateLimit-Reset sia quando restituisce il
   numero di secondi che mancano al prossimo reset, sia quando ritorna
   il timestamp unix

-  rispettare l'header Retry-After [#Retry-After]_
   sia nella variante che espone il numero di secondi dopo cui
   riprovare, sia nella variante che espone la data in cui riprovare



Segnalare il sovraccarico del sistema o l'indisponibilità del servizio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gli erogatori devono definire ed esporre un piano di continuità
operativa segnalando il sovraccarico del sistema o l'indisponibilità del
servizio con lo status code http​ 503 (service unavailable)​.

In caso di sovraccarico o indisponibilità, l'erogatore deve ritornare
anche l'header:

-  Retry-After​: il numero minimo di secondi dopo cui il client è
   invitato a riprovare

I fruitori devono:

-  rispettare l'header Retry-After [#Retry-After]_
   sia nella variante che espone il numero di secondi dopo cui
   riprovare, sia nella variante che espone la data in cui riprovare


Si propone di seguito una specifica di servizio REST relativa ad un
profilo RPC bloccante arricchito con gli header relativi al rate
limiting. L’utilizzo degli header HTTP in SOAP è fuori dagli obiettivi
di WSDL come Interface Definition Language.

Specifica Servizio
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/openapi.yaml

.. literalinclude:: ../media/robustezza.yaml
   :language: yaml

Di seguito un esempio di chiamata al servizio bloccante con risposta nel
caso in cui i limiti non siano ancora stati raggiunti e nel caso in cui
invece il fruitore debba attendere per presentare nuove richieste.

----

**Endpoint**
https://api.amministrazioneesempio.it/rest/v1/nomeinterfacciaservizio/resources/1234/M

----

1. Request Body

 .. code-block:: http

    POST /rest/v1/nomeinterfacciaservizio/resources/1234/M   HTTP/1.1
    Host: api.amministrazioneesempio.it
    Content-Type: application/json

    {
      "a": {
        "a1s": [1,2],
        "a2": "RGFuJ3MgVG9vbHMgYXJlIGNvb2wh"
      },
      "b": "Stringa di esempio"
    }

----

2. Response 200 Success

 .. code-block:: http

    HTTP/1.1 200 Success
    X-Rate-Limit-Limit: 30
    X-Rate-Limit-Remaining: 11
    X-Rate-Limit-Reset: 44

    {
      "c" : "risultato"
    }

----

2. Response 429 Too Many Requests


.. code-block:: http

   HTTP/1.1 429 Too Many Requests
   Content-Type: application/problem+json
   Retry-After: 60

   {
       "status": 429,
       "title": "Hai superato la quota di richieste."
   }

----



.. [1]
   :RFC:`7231` prevede che l'header Retry-After possa essere utilizzato sia
   in forma di data che di secondi

.. [#Retry-After]
   https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
