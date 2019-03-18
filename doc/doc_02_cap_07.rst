Altri approcci e tecnologie di integrazione
=============================================

Nelle precedenti sezioni, sono state introdotte le principali tecnologie di integrazione. Accanto a queste, stanno emergendo altre modalità di integrazione che potrebbero essere proposte in futuro in affiancamento in casi d'uso molto specifici.

Datastore distribuiti
---------------------

L'applicazione di tecnologie per datastore distribuiti è strettamente connessa, in ambito integrazione di sistemi, al mantenimento di database multi-tenant in cui, ad esempio, si richiede data locality per basi di dati di grandi dimensioni. In questo contesto, vanno considerati principalmente i file system ed i database distribuiti.

I file system distribuiti offrono interfacce basate su API per la memorizzazione di file e di oggetti e sono oggigiorno disponibili sia in soluzioni cloud pubbliche sia private. La sicurezza di queste soluzioni è soggetta agli stessi vincoli visti per l'utilizzo di interfacce di servizio nelle sezioni precedenti.

Tra i database distribuiti, grande interesse è stato suscitato da quelli basati su `blockchain <https://it.wikipedia.org/wiki/Blockchain>`_ [93]_. L'obiettivo di una blockchain è il mantenimento di un *libro mastro distribuito* (distributed ledger) mediante una rete peer-to-peer di nodi [94]_. L'obiettivo è quello di avere un datastore capace di certificare transazioni e vincoli contrattuali, in cui il meccanismo di distribuzione certifica la validità degli stessi. In particolare, è possibile appurare la validità di *smart contract* (contratti intelligenti), certificando le precondizioni degli stessi. Il termine contratto spazia dal semplice scambio di denaro, ad es., la piattaforma Bitcoin in cui la
precondizione all'invio di denaro è il possesso del denaro stesso, a contratti complessi dove le precondizioni possono assumere una qualunque forma. L'integrità dei dati memorizzati è certificata da meccanismi basati su chiave pubblica. La maggior parte dei protocolli disponibili per la realizzazione di blockchain sono basati su scambio di messaggi su TCP/TLS o HTTPS.

In Estonia, il modello `X Road <https://e-estonia.com/solutions/security-and-safety/ksi-blockchain>`_ [95]_ (equivalente al ModI) ha promosso l'utilizzo di un ledger distribuito nell'ambito della Pubblica Amministrazione, anche se più a scopo di `marketing <https://techcrunch.com/2018/04/19/do-you-need-a-blockchain/>`_ [96]_ che per l'utilizzo degli aspetti precipui di una blockchain. Quello che è interessante è l'idea di un tracciamento distribuito delle decisioni prese da una Pubblica Amministrazione.

La tecnologia blockchain non è esente da rischi in quanto diversi tipi di attacco sono stati formulati che permettono la modifica dei contenuti e la creazione di ramificazioni della catena di transazioni alla base del `libro mastro <https://www.multichain.com/blog/2017/05/blockchain-immutability-myth/>`_ [97]_.

In conclusione, sebbene si tratti di una tecnologia che sta suscitando interesse, attualmente blockchain non sono considerate abbastanza mature per l'utilizzo nella Pubblica Amministrazione in settori strategici e il
ModI ne sconsiglia al momento l'utilizzo. Inoltre deve ancora essere definito il modo di integrare ed interoperare tra PA utilizzando smart contract come interfacce di servizio, e le tipologie di transazioni che effettivamente hanno bisogno di requisiti tali per cui la blockchain sia la giusta soluzione.

L\'utilizzo di datastore distribuiti potrebbe in futuro affiancare l\'integrazione basata su altre tecnologie più consolidate. Le future linee guida dovranno tenere in considerazione per queste tecnologie:

-   requisiti di latenza e consistenza (ad es., eventual consistency, autoritatività);

-   le modalità di logging e auditing associate alla trasmissione dei dati;

-   le modalità operative di manutenzione;

-   la standardizzazione delle interfacce di accesso.

Esposizione di open data
------------------------

Una modalità di integrazione, importante specialmente negli scenari A2B e A2C, è quella basata sull'esposizione da parte delle PA di *open data*. Gli open data devono essere fruibili, ed essere inseriti ove possibile nel contesto dei Base Register definiti nell\'`EIF <https://joinup.ec.europa.eu/asset/eia/description>`_ [98]_, standardizzando gli schemi e le modalità di fruizione.

Vista la progressiva crescita dei dataset, gli open data dovrebbero essere erogati in modo da ridurre gli impatti infrastrutturali sull\'erogatore.

Come indicato nelle linee guida nazionali per la valorizzazione del `patrimonio informativo pubblico <http://lg-patrimonio-pubblico.readthedocs.io/it/latest/index.html>`_ [99]_ pubblicate da AgID nel 2014, l'obiettivo è quello di mettere a disposizione i dati aperti in formato Linked Open Data - LOD ai fini dell'integrazione, il che prevede l'esposizione di dati in formato W3C RDF e SPARQL (secondo il cosiddetto modello del *Semantic Web*). A tal fine gli SPARQL endpoint costituiscono le interfacce di servizio. Le query in formato SPARQL vengono inviate su endpoint HTTP. Un altro approccio possibile, sempre nel rispetto dei dizionari comuni, è quello di utilizzare un approccio ROA basato su interfacce REST [100]_.

Un'interessante evoluzione dell'approccio REST (di cui eredita molti dei vantaggi, quali ad esempio la leggerezza e l'utilizzo dei verbi HTTP) che può risultare utile nell'esposizione di open data è quello basato su
`GraphQL <https://graphql.org/>`_ [101]_. In particolare, mentre per l'estrazione di dati complessi l'approccio basato su interfacce di servizio REST richiede diverse chiamate, GraphQL introduce un linguaggio che permette l'esecuzione di
interrogazioni complesse sulle risorse.

In tutti i casi presentati, restano valide le indicazioni contenute nelle sezioni precedenti circa la sicurezza nell'esposizione delle interfacce di servizio.


.. discourse::
   :topic_identifier: 3241

	
.. [93] Cf. `https://it.wikipedia.org/wiki/Blockchain <https://it.wikipedia.org/wiki/Blockchain>`_

.. [94] Una rete di calcolatori si definisce peer-to-peer, quando le macchine componenti (i nodi) non sono organizzati gerarchicamente ma svolgono delle funzionalità paritarie.

.. [95] Cf. `https://e-estonia.com/solutions/security-and-safety/ksi-blockchain <https://e-estonia.com/solutions/security-and-safety/ksi-blockchain>`_

.. [96] Cf. `https://techcrunch.com/2018/04/19/do-you-need-a-blockchain/ <https://techcrunch.com/2018/04/19/do-you-need-a-blockchain/>`_

.. [97] Cf. `https://www.multichain.com/blog/2017/05/blockchain-immutability-myth/ <https://www.multichain.com/blog/2017/05/blockchain-immutability-myth/>`_

.. [98] Cf. `https://joinup.ec.europa.eu/asset/eia/description <https://joinup.ec.europa.eu/asset/eia/description>`_

.. [99] Cf. `http://lg-patrimonio-pubblico.readthedocs.io/it/latest/index.html <http://lg-patrimonio-pubblico.readthedocs.io/it/latest/index.html>`_

.. [100] Cf. Massimo Mecella, Francesco Leotta (2017): Migliorare l'accesso agli open data pubblici: tecnologie e approcci, `https://www.agendadigitale.eu/cittadinanza-digitale/pa-tecnologie-e-approcci-per-migliorare-laccesso-ai-dati-aperti/ <https://www.agendadigitale.eu/cittadinanza-digitale/pa-tecnologie-e-approcci-per-migliorare-laccesso-ai-dati-aperti/>`_

.. [101] Cf. `https://graphql.org/ <https://graphql.org/>`_
