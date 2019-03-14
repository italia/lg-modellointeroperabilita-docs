3.3. [M2MR01] Direct Trust con certificato X.509 su REST
========================================================

.. _scenario-4:

3.3.1. Scenario
---------------

Comunicazione tra richiedente ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto richiedente, quale organizzazione o unità
   organizzativa richiedente, o entrambe le parti.

.. _descrizione-4:

3.3.2. Descrizione
------------------

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’RFC 7519 [1]

-  JSON Web Signature (JWS) definita dall’RFC 7515 [2]

Si assume l’esistenza di un trust tra richiedente (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il richiedente inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata..

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-4:

3.3.3. Dettaglio
----------------

|image0|

.. _flusso-delle-interazioni-4:

3.3.3.1. Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509 e valida la firma del token JWT.

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

.. _regole-di-processamento-4:

3.3.3.2. Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il richiedente predispone la payload del messaggio (ad esempio un
   oggetto JSON)

2. Il richiedente costruisce il token JWT popolando:

   a. l’header JSON Object Signing and Encryption (JOSE) con almeno:

      i.   la claim alg al fine di definire l’algoritmo utilizzato per
           la signature

      ii.  la claim typ pari a JWT

      iii. in maniera alternativa, per referenziare il certificato
           X.509, una delle seguenti claim:

           1. x5u (X.509 URL)

           2. x5c (X.509 Certificate Chain)

           3. x5t (X.509 Certificate SHA-1 Thumbprint)

           4. x5t#S256 (X.509 Certificate SHA-256 Thumbprint)

   b. la payload del JWT con zero o più claim rappresentative degli
      elementi chiave del messaggio.

3. il richiedente firma il token JWT secondo la specifica JWS adottando
   la JWS Compact Serialization

4. il richiedente posiziona il token JWT firmato nell’header HTTP
   Authorization

5. Il richiedente spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

6.  L’erogatore decodifica il token JWT presente nell’header HTTP
    Authorization

7.  L’erogatore recupera il certificato X.509 referenziato nell’header
    JOSE

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del
    token JWT

10. L’erogatore autentica il richiedente

11. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nella claim alg si fa
   riferimento agli algoritmi indicati alla sezione `Elenco degli
   algoritmi <#elenco-degli-algoritmi>`__. Un meccanismo simile può
   essere utilizzato per autenticare l’erogatore.

.. _tracciato-2:

3.3.3.3. Tracciato
~~~~~~~~~~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
richiedente all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

+-----------------------------------------------------------+
| GET http://localhost:8080/ws-test/service/hello/echo/Ciao |
|                                                           |
| Accept: text/xml                                          |
|                                                           |
| Authorization: eyJhbGciOiJSUzI1NiIsInR5c.vz8...           |
|                                                           |
| .                                                         |
|                                                           |
| .                                                         |
|                                                           |
| .                                                         |
|                                                           |
| .                                                         |
+-----------------------------------------------------------+

Esempio porzione token JWT

+----------------------------+
| header                     |
|                            |
| {                          |
|                            |
| "alg": "RS256",            |
|                            |
| "typ": "JWT",              |
|                            |
| "x5c": [                   |
|                            |
| "MIICyzCCAbOgAwIBAgIEC..." |
|                            |
| ]                          |
|                            |
| }                          |
|                            |
| payload                    |
|                            |
| {}                         |
+----------------------------+

Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al certificato X.509 (x5c)

-  algoritmi di firma e digest (alg).

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione `Elenco degli
algoritmi <#elenco-degli-algoritmi>`__, nonché la modalità di inclusione
o referenziazione del certificato X.509.

.. |image0| image:: ./media/image8.png
   :width: 2.34375in
   :height: 1.28125in
