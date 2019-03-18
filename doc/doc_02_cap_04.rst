REST
====

`REpresentational State Transfer (REST) è uno stile architetturale, proposto da Roy Fielding <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_ [55]_, che consente di accedere e manipolare rappresentazioni testuali di risorse web usando un insieme predefinito di operazioni stateless. Le interfacce di servizio che seguono lo stile architetturale REST sono dette RESTful o semplicemente REST. Con il termine "risorsa web" si intendevano inizialmente documenti e file identificati da una URL sul World Wide Web. Oggi il termine ha un'accezione molto più generica ed astratta, andando ad indicare ogni cosa o entità che possa essere identificata tramite una URI (si noti il passaggio da URL ad URI che indica l'indipendenza dal protocollo di recupero dei dati). Nel caso dell'applicazione di questo stile architetturale ad HTTP, le operazioni stateless a cui si fa riferimento sono GET, POST, PUT, DELETE a cui
corrispondono operazioni di tipo Create-Read-Update-Delete - CRUD sulla risorsa. Questo approccio favorisce l'uniformità delle interfacce di servizio.

Il termine "state transfer" indica che è il client a dovere riportare tutte le informazioni necessarie al soddisfacimento di una richiesta, e il server non memorizza alcun tipo di informazione circa la sessione; quindi le interfacce di servizio sono, per definizione, stateless. Questo tipo di approccio favorisce l'introduzione di meccanismi di caching. In particolare, le risposte del server devono contenere una indicazione sul fatto che le risposte possano essere messe in cache o meno. Opzionalmente, inoltre, è possibile per il server richiedere l'esecuzione di alcune funzionalità al client tramite il passaggio di codice da eseguire (ad es., codice JavaScript da eseguire nel browser).

Talvolta, il termine Resource Oriented Architecture - ROA è usato per denotare l'architettura REST in opposizione alle Service Oriented Architecture - SOA, indicando la predilezione della prima per l'accesso basato su risorsa più che sulla chiamate ad operazioni di tipo RPC. Il dibattito sulla correttezza o meno di implementare operazioni RPC utilizzando REST è molto acceso, ma come dato di fatto numerose iniziative di API commerciali e non, utilizzano interfacce di servizio REST anche per effettuare RPC. Il concetto di REST è inoltre molto spesso legato, anche se non per definizione, alle architetture dette a
microservizi [56]_, caratterizzate da elevata modularità, per via della leggerezza del protocollo.

A differenza delle interfacce di servizio SOAP, per cui una serie di standard è definita e mantenuta da OASIS (cf. stack WS-\*), per le interfacce REST sono disponibili singoli standard e best-practice. 

Per la specifica delle interfacce REST esistono due grandi iniziative: OpenAPI e RAML.
Sebbene simili dal punto di vista dello sviluppatore di interfacce di servizio, la specifica RAML è più indirizzata alla creazione automatica di server e di client per API, mentre OpenAPI (attualmente nella versione OpenAPI v3) contiene elementi più descrittivi per la documentazione e la catalogazione (che invece sono disponibili in RAML come estensioni ad hoc) e si sta imponendo come standard de facto.
Altri standard proposti in passato, quali Web Application Description Language - WADL, hanno avuto scarso successo e nei framework in cui sono stati utilizzati si sta optando per il passaggio ad `OpenAPI v3 <https://www.openapis.org/>`_ [57]_. Per queste ragioni il ModI 2018 impone l’uso di OpenAPI v3.

È possibile assicurare la conversione tra le differenti rappresentazioni delle interfacce REST tramite tool automatici.

Legato al concetto di specifica nel mondo REST è quello di *Hypermedia As The Engine Of Application State - HATEOAS*. Secondo questo approccio, accedendo ad una risorsa, la risposta del server contiene hyperlink ad altre azioni che possono essere eseguite sulla risorsa [58]_. HATEOAS permette di scoprire dinamicamente le operazioni presenti in una interfaccia di servizio e può essere utilizzato come approccio complementare (non sostitutivo) alla specifica.

Indicazioni di utilizzo
-----------------------

L'interfaccia di servizio REST deve utilizzare l\'HTTP verb più adatto all\'operazione come indicato in `RFC 7231 <https://tools.ietf.org/html/rfc7231#section-4.3>`_ [59]_. In particolare i metodi:

-   GET, HEAD, DELETE: non devono avere un payload.

-   GET, HEAD: devono essere \"safe\", cioè devono essere essenzialmente read-only. Il client in questo caso non si aspetta e non richiede un cambiamento dello stato della risorsa.

-   GET, HEAD, PUT, DELETE: devono essere idempotenti, cioè chiamate multiple con richieste identiche si comportano come singole richieste.

-   POST: dovrebbe implementare un meccanismo di idempotenza per evitare di duplicare eventuali entry.

Ove necessario, specialmente ai fini del caching e l'accesso concorrente alle risorse [60]_, occorre fare leva sugli `ETag <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`_ [61]_ (degli identificatori univoci di versione delle risorse). Infine l'utilizzo di eventuali header HTTP non deve sostituire i parametri da passare in una GET.

Sicurezza
---------

Lo standard di riferimento per la firma e la crittografia in ambito JSON/REST è `Javascript Object Signing and Encryption <http://www.etsi.org/deliver/etsi_ts/118100_118199/118103/02.04.01_60/ts_118103v020401p.pdf>`_ [62]_ (di seguito JOSE), menzionato nelle `Linee Guida AgID <http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/cert-pa/linee-guida-sviluppo-sicuro>`_ [63]_ ed in `\"European Telecommunications Standards Institute - Security of the mission critical service\" <http://www.etsi.org/deliver/etsi_ts/133100_133199/133180/14.02.00_60/ts_133180v140200p.pdf>`_ [64]_. JOSE è un framework per la sicurezza comprendente diverse componenti tra cui centrale è il `JSON Web Token <https://tools.ietf.org/html/rfc7519>`_ [65]_ (di seguito JWT). JWT è uno standard per la definizione di token di accesso basato su `JSON Web Signature <https://tools.ietf.org/html/rfc7515>`_ [66]_ (di seguito JWS) e `JSON Web Encryption <https://tools.ietf.org/html/rfc7516>`_ [67]_ (si seguito JWE) di cui eredita ed estende gli header. Il token JWT è passato in REST tramite l'header HTTP
Authorization utilizzando lo schema Bearer [68]_. Il token in OpenID Connect è espresso per esempio direttamente come JWT. 

Per ulteriori dettagli sulla sicurezza, si vedano anche:

-   `OWASP REST Security Cheat-Sheet <https://www.owasp.org/index.php/REST_Security_Cheat_Sheet>`_ [69]_;

-   `OWASP API Security Project <https://www.owasp.org/index.php/OWASP_API_Security_Project>`_ [70]_;

-   `JWS - Security Considerations <https://tools.ietf.org/html/rfc7515#section-10>`_ [71]_.

Uniformità e Naming 
-------------------

In questa sezione introduciamo le best practice da utilizzare per interfacce di servizio REST. In prima istanza, ogni endpoint deve essere univocamente associato alle componenti `Scheme, Authority e Path di un URL <https://tools.ietf.org/html/rfc3986>`_ [72]_.

La componente Authority dell'URL:

-   dovrebbe essere associata al dominio del sito Istituzionale dell'erogatore presente su IndicePA, anche tramite il prefisso \"api\", ad esempio un erogatore con sito istituzionale \"erogatore.gov.it\", potrebbe usare come authority  \"api.erogatore.gov.it\";

-   può essere associata al dominio di un ente che l\'erogatore ha delegato (ad es., una società in-house, un consorzio di comuni).

Per quanto riguarda la componente Path, i nomi utilizzati non devono usare abbreviazioni e acronimi non universalmente riconosciuti [73]_. Inoltre, il Path dovrebbe essere semplice, intuitivo e coerente [74]_.

Il campo Query dovrebbe:

-   essere in snake\_case minuscolo;

-   non essere in camelCase;

-   utilizzare ove possibile dei nomi comuni per le funzionalità di paginazione, ricerca ed embedding/resource-expansion (ad es., limit, offset, q, sort).

Le risposte in formato `JSON <https://tools.ietf.org/html/rfc7159>`_ [75]_, devono restituire sempre oggetti strutturati con attributi chiave-valore, non semplici liste. Questo permette di estendere facilmente le risposte introducendo in versioni successive ulteriori attributi (ad es., di paginazione).

In caso di errore, le risposte devono usare schemi standard come quello definito nella `RFC 7807 - Problem Details for HTTP APIs - IETF Tools <https://tools.ietf.org/html/rfc7807>`_ [76]_ in particolare utilizzando il content type application/problem+json nella risposta.

Quando le risorse contengono link e riferimenti a risorse esterne, si dovrebbero usare le specifiche indicate in `IANA registered link
relations  <http://www.iana.org/assignments/link-relations/link-relations.xml>`_ [77]_.

Tutti i riferimenti dovrebbero contenere URL comprensivi di schema.

Throttling ed indisponibilità del servizio
------------------------------------------

Nelle API basate su REST, meccanismi di throttling vengono implementati al fine di garantire l’accessibilità delle interfacce di servizio ed evitare in alcuni casi la raccolta non autorizzata (web-harvesting) dei dati. 

Poiché l'RFC 6585 prevede per la gestione del throttling il solo status code 429, nel Modl2018 si richiede di notificare al fruitore lo stato del throttling ed eventuali limiti come segue:

- restituire in ogni risposta valida i valori globali di throttling tramite i seguenti header HTTP:

	- X-RateLimit-Limit: limite massimo di richieste per un endpoint;
	
	- X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo reset;
	
	- X-RateLimit-Reset: il numero di secondi mancanti al momento in cui il limite verrà reimpostato.
	
- utilizzare gli HTTP status code nelle risposte:

	- HTTP 429 (too many requests), insieme ai rate limit di cui al punto precedente, se il rate limit viene superato;
	
	- HTTP 503 (service unavailable) se l'infrastruttura non può erogare le operazioni offerte nei tempi attesi (definiti dalla SLA associata all’interfaccia di servizio).
	
- nei casi 429 e 503 gli erogatori dovrebbero notificare al client dopo quanti secondi ripresentarsi tramite l'header `Retry-After <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-Afte>`_ [78]_ (pratica anche detta “circuit breaker”), anche implementando meccanismi di exponential back-off. L'RFC prevede che questo header possa essere utilizzato sia in forma di data che di secondi, ma il Modl2018 vieta l’utilizzo del formato data poiché se non implementato correttamente potrebbe aggravare lo stato dei sistemi.

I fruitori dell'interfaccia di servizio devono impegnarsi a rispettare le indicazioni provenienti dagli header e dagli status code di cui sopra.

.. discourse::
   :topic_identifier: 3238


.. [55] Cf. `http://www.ics.uci.edu/\~fielding/pubs/dissertation/rest\_arch\_style.htm <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_

.. [56] Cf. Sam Newman (2015): Building Microservices.

.. [57] Cf. `https://www.openapis.org/ <https://www.openapis.org/>`_

.. [58] Si supponga ad esempio una operazione HTTP GET http://api.domain.com/management/departments che restituisce informazioni circa i reparti. Il singolo reparto può contenere link relativi ad altre operazioni come quella per ottenere gli impiegati del reparto:\
    {\
    \"departmentId\": 10,\
    \"departmentName\": \"Administration\",\
    \"links\": \[\
    {\"href\":
    \"[[http://api.domain.com/management/departments/10/employees]{.underline}](http://api.domain.com/management/departments/10/employees)\",\
    \"rel\": \"employees\", \"type\" : \"GET\" }\
    \]\
    }

.. [59] Cf. `https://tools.ietf.org/html/rfc7231\#section-4.3 <https://tools.ietf.org/html/rfc7231#section-4.3>`_

.. [60] C.f. `https://en.wikipedia.org/wiki/Optimistic_concurrency_contro <https://en.wikipedia.org/wiki/Optimistic_concurrency_contro>`_

.. [61] Cf. `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`_

.. [62] Cf. `http://www.etsi.org/deliver/etsi\_ts/118100\_118199/118103/02.04.01\_60/ts\_118103v020401p.pdf <http://www.etsi.org/deliver/etsi_ts/118100_118199/118103/02.04.01_60/ts_118103v020401p.pdf>`_

.. [63] Cf. `http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/cert-pa/linee-guida-sviluppo-sicuro <http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/cert-pa/linee-guida-sviluppo-sicuro>`_

.. [64] Cf. `http://www.etsi.org/deliver/etsi\_ts/133100\_133199/133180/14.02.00\_60/ts\_133180v140200p.pdf <http://www.etsi.org/deliver/etsi_ts/133100_133199/133180/14.02.00_60/ts_133180v140200p.pdf>`_

.. [65] Cf. `https://tools.ietf.org/html/rfc7519 <https://tools.ietf.org/html/rfc7519>`_

.. [66] Cf. `https://tools.ietf.org/html/rfc7515 <https://tools.ietf.org/html/rfc7515>`_

.. [67] Cf. `https://tools.ietf.org/html/rfc7516 <https://tools.ietf.org/html/rfc7516>`_

.. [68] Lo schema Bearer, inizialmente introdotto nella specifica OAuth2 ma poi utilizzato in altri contesti, ha la forma "Authorization:
    Bearer \<token\>" dove il token JWT è codificato in base64.

.. [69] Cf. `https://www.owasp.org/index.php/REST\_Security\_Cheat\_Sheet <https://www.owasp.org/index.php/REST_Security_Cheat_Sheet>`_

.. [70] Cf. `https://www.owasp.org/index.php/OWASP\_API\_Security\_Project <https://www.owasp.org/index.php/OWASP_API_Security_Project>`_

.. [71] Cf. `https://tools.ietf.org/html/rfc7515\#section-10 <https://tools.ietf.org/html/rfc7515#section-10>`_

.. [72] Cf. `https://tools.ietf.org/html/rfc3986 <https://tools.ietf.org/html/rfc3986>`_

.. [73] Cf. `https://linee-guida-cataloghi-dati-profilo-dcat-ap-it.readthedocs.io/it/latest/catalogo\_elementi\_obbligatori.html\#titolo-dct-title <https://linee-guida-cataloghi-dati-profilo-dcat-ap-it.readthedocs.io/it/latest/catalogo_elementi_obbligatori.html#titolo-dct-title>`_ Ad esempio,
	
	- sono ammesse stringhe come \"id\", \"args\" o \"stdin\" ed abbreviazioni come \"tcp\" ed \"udp\"; 
	
	- stringhe come \"codice fiscale\" andrebbero espresse per esteso con \"codice\_fiscale\" o \"tax\_code\", e non con \"cod\_fiscale\", \"cod\_fisc\" o \"cf\".

.. [74] Alcune indicazioni in questo senso:

	- usare parole minuscole separate da trattino "-";

	- usare nomi al plurale per le risorse e al singolare per l\'accesso alla singola risorsa;

	- ispirarsi alle convenzioni utilizzate a livello europeo (ad es., Core Vocabularies/Dizionari Controllati, Direttiva Europea INSPIRE 2007/2/CE);

	- non contenere verbi (ad es., api.example.com/ospedale/prenota/);

	- uniformarsi a quello di altre interfacce di servizio a livello Europeo quando ciò vada nella direzione dell\'interoperabilità e della semplicità.

	- In generale tutte le stringhe in inglese dovrebbero utilizzare la dizione US per evitare ambiguità (come ad es., \"color\" vs \"colour\", \"flavor\" vs \"flavour\").

.. [75] Cf. `https://tools.ietf.org/html/rfc7159 <https://tools.ietf.org/html/rfc7159>`_

.. [76] Cf. `https://tools.ietf.org/html/rfc7807 <https://tools.ietf.org/html/rfc7807>`_

.. [77] Cf. `http://www.iana.org/assignments/link-relations/link-relations.xml <http://www.iana.org/assignments/link-relations/link-relations.xml>`_

.. [78] Cf. `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After>`_
