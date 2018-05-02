4 REST
======

REpresentational State Transfer (REST) è uno stile architetturale, proposto originariamente da Fielding [55]_, che consente di accedere e manipolare rappresentazioni testuali di risorse web usando un insieme predefinito di operazioni stateless. Le interfacce di servizio che seguono lo stile architetturale REST sono chiamate interfacce di servizio RESTful o semplicemente REST. Con il termine "risorsa web" si intendevano inizialmente documenti e file identificati da una URL sul World Wide Web. Oggi il termine ha un'accezione molto più generica ed astratta, andando ad indicare ogni cosa o entità che possa essere identificata tramite una URI (si noti il passaggio da URL ad URI che indica l'indipendenza dal protocollo di recupero dei dati). Nel caso dell'applicazione di questo stile architetturale ad HTTP, le operazioni stateless a cui si fa riferimento sono GET, POST, PUT, DELETE a cui
corrispondono operazioni di tipo Create-Read-Update-Delete - CRUD sulla risorsa. Questo approccio favorisce l'uniformità delle interfacce di servizio.

Il termine "state transfer" all'interno dell'acronimo REST indica che è il client a dovere riportare tutte le informazioni necessarie al soddisfacimento di una richiesta, e il server non memorizza alcun tipo di informazione circa la sessione; quindi le interfacce di servizio sono, per definizione, stateless. Questo tipo di approccio favorisce inoltre l'introduzione di meccanismi di caching. In particolare, le risposte del server devono contenere una indicazione sul fatto che le risposte possano essere messe in cache o meno. Opzionalmente, inoltre, è possibile per il server richiedere l'esecuzione di alcune funzionalità al client tramite il passaggio di codice da eseguire (ad es., codice JavaScript da eseguire nel browser).

Talvolta, il termine Resource Oriented Architecture - ROA è usato per denotare l'architettura REST in opposizione alle Service Oriented Architecture - SOA, indicando la predilezione della prima per l'accesso basato su risorsa più che sulla chiamate ad operazioni di tipo RPC. Il dibattito sulla correttezza o meno di implementare operazioni RPC utilizzando REST è molto acceso, ma come dato di fatto numerose iniziative di API commerciali e non, utilizzano interfacce di servizio REST anche per effettuare RPC. Il concetto di REST è inoltre molto spesso legato, anche se non per definizione, alle architetture dette a
microservizi [56]_, caratterizzate da elevata modularità, per via della leggerezza del protocollo.

A differenza delle interfacce di servizio SOAP, per cui una serie di standard è definita e mantenuta da OASIS (cf. stack WS-\*), per le interfacce di servizio REST sono disponibili solamente singoli standard e best-practice. Per la specifica delle interfacce REST esistono due grandi iniziative: OpenAPI e RAML. Sebbene simili dal punto di vista dello sviluppatore di interfacce di servizio, la specifica RAML è più indirizzata alla creazione automatica di server e di client per API, mentre OpenAPI (attualmente nella versione OpenAPI v3 [57]_) contiene elementi più descrittivi per la documentazione e la catalogazione (che invece sono disponibili in RAML come estensioni ad-hoc) e si sta imponendo come standard de-facto. Per queste ragioni il ModI 2018 impone l'uso di OpenAPI v3.

Altri standard proposti in passato, quali Web Application Description Language - WADL, hanno avuto scarso successo e nei framework in cui sono stati utilizzati si sta optando per il passaggio ad OpenAPI v3.

Legato al concetto di specifica nel mondo REST è quello di *Hypermedia As The Engine Of Application State - HATEOAS*. Secondo questo approccio, accedendo ad una risorsa, la risposta del server contiene hyperlink ad
altre azioni che possono essere eseguite sulla risorsa [58]_. HATEOAS permette in questa maniera di scoprire dinamicamente le operazioni presenti in una interfaccia di servizio e quindi può essere utilizzato come approccio complementare (non sostitutivo) alla specifica.

4.1 Indicazioni di utilizzo
---------------------------

L'interfaccia di servizio REST deve utilizzare l\'HTTP verb più adatto all\'operazione come indicato in RFC 7231 [59]_. In particolare i metodi:

-   GET, HEAD, DELETE: non devono avere un payload.

-   GET, HEAD: devono essere \"safe\", cioè devono essere essenzialmente read-only. Il client in questo caso non si aspetta e non richiede un cambiamento dello stato della risorsa.

-   GET, HEAD, PUT, DELETE: devono essere idempotenti, cioè chiamate multiple con richieste identiche si comportano come singole richieste.

-   POST: dovrebbe implementare un meccanismo di idempotenza per evitare di duplicare eventuali entry.

Ove necessario, specialmente ai fini del caching, occorre fare leva sugli ETag [60]_ (degli identificatori univoci di versione delle risorse). Infine l'utilizzo di eventuali header HTTP non deve sostituire i parametri da passare in una GET.

4.2 Sicurezza
-------------

Lo standard di riferimento per la firma e la crittografia in ambito JSON/REST è Javascript Object Signing and Encryption [61]_ (di seguito JOSE), menzionato nelle Linee Guida AgID [62]_ ed in \"European Telecommunications Standards Institute - Security of the mission critical service\" [63]_. JOSE è un framework per la sicurezza comprendente diverse componenti tra cui centrale è il JSON Web Token [64]_ (di seguito JWT). JWT è uno standard per la definizione di token di accesso basato su JSON Web Signature [65]_ (di seguito JWS)) e JSON Web Encryption [66]_ (si seguito JWE) di cui eredita ed estende gli header. Il token JWT è passato in REST tramite l'header HTTP
Authorization utilizzando lo schema Bearer [67]_. Il token in OpenID Connect è espresso per esempio direttamente come JWT. 

Per ulteriori dettagli sulla sicurezza, si vedano anche:

-   OWASP REST Security Cheat-Sheet  [68]_;

-   OWASP API Security Project  [69]_;

-   JWS - Security Considerations  [70]_.

4.3 Uniformità e Naming 
------------------------

In questa sezione introduciamo le best practice da utilizzare per interfacce di servizio REST. In prima istanza, ogni endpoint deve essere univocamente associato alle componenti Scheme, Authority e Path di un URL [71]_.

La componente Authority dell'URL:

-   dovrebbe essere associata al dominio del sito Istituzionale dell'erogatore presente su IndicePA, anche tramite il prefisso \"api\";

-   può essere associata al dominio di un ente che l\'erogatore ha delegato (ad es., una società in-house, un consorzio di comuni).

Per quanto riguarda la componente Path, i nomi utilizzati non devono usare abbreviazioni e acronimi non universalmente riconosciuti [72]_. 

Inoltre, il Path dovrebbe essere semplice, intuitivo e coerente [73]_.

Per quanto riguarda il campo Query dovrebbe:

-   essere in snake\_case minuscolo;

-   non essere in camelCase;

-   utilizzare ove possibile dei nomi comuni per le funzionalità di paginazione, ricerca ed embedding/resource-expansion (ad es., limit, offset, q, sort).

Le response in formato JSON [74]_, dovrebbero tornare sempre oggetti, non liste. Questo permette di estendere le response introducendo successivamente ulteriori attributi (ad es., di paginazione).

In caso di errore, le response dovrebbero usare schemi standard come quello definito nella RFC 7807 - Problem Details for HTTP APIs - IETF Tools [75]_ in particolare utilizzando il content type application/problem+json nella response.

Quando le risorse contengono link e riferimenti a risorse esterne, si dovrebbero usare le specifiche indicate in IANA registered link
relations [76]_.

Tutti i riferimenti dovrebbero contenere URL comprensivi di schema.

4.4 Throttling ed indisponibilità del servizio
----------------------------------------------

Di sovente, nelle API basate su REST, meccanismi di throttling vengono implementati al fine di garantire l'accessibilità delle interfacce di servizio ed evitare in alcuni casi dump dei dati. Sebbene non esistano standard a riguardo, al fine di rendere noto al fruitore dell'interfaccia di servizio lo stato del throttling ed eventuali limiti si possono utilizzare le seguenti indicazioni:

-   ritornare in ogni response valida i valori globali di throttling tramite i seguenti header HTTP:

    -   X-RateLimit-Limit: limite massimo di richieste per un endpoint;

    -   X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo reset;

    -   X-RateLimit-Reset: il timestamp UTC che indica il momento in cui il limite verrà reimpostato o il numero di secondi mancanti.

-   utilizzare gli HTTP status code nelle risposte:

    -   HTTP 429 (too many requests), insieme ad i rate limit di cui al punto precedente, se il rate limit viene superato;

    -   HTTP 503 (service unavailable) se l\'infrastruttura non può erogare le operazioni offerte nei tempi attesi (definiti dalla SLA associata all'interfaccia di servizio). In questo caso si può utilizzare l\'header Retry-After [77]_ con codice HTTP 503 (pratica anche detta "circuit breaker") per suggerire al client dopo quanto tempo ripresentarsi, anche implementando meccanismi di exponential back-off. Questo header può essere utilizzato sia in forma di data che di secondi, ma l'utilizzo di questi ultimi è suggerito [78]_.

I fruitori dell'interfaccia di servizio devono impegnarsi a rispettare le indicazioni provenienti dagli header ed dagli status code di cui sopra.


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

.. [60] Cf. `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`_

.. [61] Cf. `http://www.etsi.org/deliver/etsi\_ts/118100\_118199/118103/02.04.01\_60/ts\_118103v020401p.pdf <http://www.etsi.org/deliver/etsi_ts/118100_118199/118103/02.04.01_60/ts_118103v020401p.pdf>`_

.. [62] Cf. `http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/cert-pa/linee-guida-sviluppo-sicuro <http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/cert-pa/linee-guida-sviluppo-sicuro>`_

.. [63] Cf. `http://www.etsi.org/deliver/etsi\_ts/133100\_133199/133180/14.02.00\_60/ts\_133180v140200p.pdf <http://www.etsi.org/deliver/etsi_ts/133100_133199/133180/14.02.00_60/ts_133180v140200p.pdf>`_

.. [64] Cf. `https://tools.ietf.org/html/rfc7519 <https://tools.ietf.org/html/rfc7519>`_

.. [65] Cf. `https://tools.ietf.org/html/rfc7515 <https://tools.ietf.org/html/rfc7515>`_

.. [66] Cf. `https://tools.ietf.org/html/rfc7516 <https://tools.ietf.org/html/rfc7516>`_

.. [67] Lo schema Bearer, inizialmente introdotto nella specifica OAuth2 ma poi utilizzato in altri contesti, ha la forma "Authorization:
    Bearer \<token\>" dove il token JWT è codificato in base64.

.. [68] Cf. `https://www.owasp.org/index.php/REST\_Security\_Cheat\_Sheet <https://www.owasp.org/index.php/REST_Security_Cheat_Sheet>`_

.. [69] Cf. `https://www.owasp.org/index.php/OWASP\_API\_Security\_Project <https://www.owasp.org/index.php/OWASP_API_Security_Project>`_

.. [70] Cf. `https://tools.ietf.org/html/rfc7515\#section-10 <https://tools.ietf.org/html/rfc7515#section-10>`_

.. [71] Cf. `https://tools.ietf.org/html/rfc3986 <https://tools.ietf.org/html/rfc3986>`_

.. [72] Cf. `https://linee-guida-cataloghi-dati-profilo-dcat-ap-it.readthedocs.io/it/latest/catalogo\_elementi\_obbligatori.html\#titolo-dct-title <https://linee-guida-cataloghi-dati-profilo-dcat-ap-it.readthedocs.io/it/latest/catalogo_elementi_obbligatori.html#titolo-dct-title>`_
    Ad esempio, 
	(i) sono ammesse stringhe come \"id\", \"args\" o \"stdin\" ed abbreviazioni come \"tcp\" ed \"udp\"; 
	(ii) stringhe come \"codice fiscale\" andrebbero espresse per esteso con \"codice\_fiscale\" o \"tax\_code\", e non con \"cod\_fiscale\", \"cod\_fisc\" o \"cf\".

.. [73] Alcune indicazioni in questo senso:

    - usare parole minuscole separate da trattino "-";

    - usare nomi al plurale per le risorse e al singolare per l\'accesso alla singola risorsa;

    - ispirarsi alle convenzioni utilizzate a livello europeo (ad es., Core Vocabularies/Dizionari Controllati, Direttiva Europea INSPIRE 2007/2/CE);

    - non contenere verbi (ad es., api.example.com/ospedale/prenota/);

    - uniformarsi a quello di altre interfacce di servizio a livello Europeo quando ciò vada nella direzione dell\'interoperabilità e della semplicità.

    In generale inoltre, tutte le stringhe in inglese, dovrebbero utilizzare la dizione US per evitare ambiguità come ad es., \"color\" vs \"colour\", \"flavor\" vs \"flavour\").

.. [74] Cf. `https://tools.ietf.org/html/rfc7159 <https://tools.ietf.org/html/rfc7159>`_

.. [75] Cf. `https://tools.ietf.org/html/rfc7807 <https://tools.ietf.org/html/rfc7807>`_

.. [76] Cf. `http://www.iana.org/assignments/link-relations/link-relations.xml <http://www.iana.org/assignments/link-relations/link-relations.xml>`_

.. [77] Cf. `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After>`_

.. [78] Cf. `http://www.nurkiewicz.com/2015/02/retry-after-http-header-in-practice.html <http://www.nurkiewicz.com/2015/02/retry-after-http-header-in-practice.html>`_