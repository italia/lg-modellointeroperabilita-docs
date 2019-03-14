3.4. [M2MR02] Direct Trust con certificato X.509 su REST con threat mitigation
==============================================================================

.. _scenario-5:

3.4.1. Scenario
---------------

Il seguente profilo estende il profilo M2MR01.

Comunicazione tra richiedente ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto richiedente, quale organizzazione o unità
   organizzativa richiedente, o entrambe le parti

-  la difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

.. _descrizione-5:

3.4.2. Descrizione
------------------

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’RFC 7519 `[1] <#bibliografia>`__

-  JSON Web Signature (JWS) definita dall’RFC 7515
   `[2] <#bibliografia>`__

Si assume l’esistenza di un trust tra richiedente (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il richiedente inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509,
valida la firma dei claim ed autentica il fruitore. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-5:

3.4.3. Dettaglio
----------------

|image0|

.. _flusso-delle-interazioni-5:

3.4.3.1. Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT:

-  include o referenzia il certificato X.509 riconosciuto
   dall’erogatore,

-  include almeno i seguenti claim:

   -  il riferimento dell’erogatore

   -  un riferimento temporale univoco per messaggio

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma del token JWT e le claim ricevute.

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

.. _regole-di-processamento-5:

3.4.3.2. Regole di processamento
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

   b. la payload del JWT con le claim rappresentative degli elementi
      significativi del messaggio, quali almeno:

      iv. iat: contenente il riferimento temporale univoco per messaggio

      v.  aud: contenente il riferimento dell’erogatore

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
    JOSE.

8.  L’erogatore verifica il certificato secondo i criteri del trust.

9.  L’erogatore valida la firma verificando l’elemento Signature del
    token JWT

10. L’erogatore verifica il contenuto della claim iat contenuta nella
    payload del JWT al fine di verificare la validità temporale del
    messaggio anche per mitigare il rischio di replay attack.

11. L’erogatore verifica la corrispondenza tra se stesso e quanto
    definito nella claim aud contenuta nella payload del JWT.

12. L’erogatore autentica il richiedente.

13. Se le azioni da 6 a 12 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nella claim alg si fa
   riferimento agli algoritmi indicati alla sezione `Elenco degli
   algoritmi <#elenco-degli-algoritmi>`__.

-  Un meccanismo simile può essere utilizzato per autenticare
   l’erogatore.

.. _tracciato-3:

3.4.3.3. Tracciato
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
+-----------------------------------------------------------+

Esempio porzione token JWT

+----------------------------------------------------------+
| header                                                   |
|                                                          |
| {                                                        |
|                                                          |
| "alg": "RS256",                                          |
|                                                          |
| "typ": "JWT",                                            |
|                                                          |
| "x5c": [                                                 |
|                                                          |
| "MIICyzCCAbOgAwIBAgIEC..."                               |
|                                                          |
| ]                                                        |
|                                                          |
| }                                                        |
|                                                          |
| payload                                                  |
|                                                          |
| {                                                        |
|                                                          |
| “iat”:”1516239022”,                                      |
|                                                          |
| “aud”:”http://localhost:8080/ws-test/service/hello/echo” |
|                                                          |
| }                                                        |
+----------------------------------------------------------+

Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al certificato X.509 (x5c)

-  algoritmi di firma e digest (alg).

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione `Elenco degli
algoritmi <#elenco-degli-algoritmi>`__, nonché la modalità di inclusione
o referenziazione del certificato x509.

.. |image0| image:: ./media/image1.png
   :width: 2.47917in
   :height: 1.3125in
