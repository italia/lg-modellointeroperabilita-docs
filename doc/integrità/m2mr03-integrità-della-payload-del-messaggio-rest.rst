4.2. [M2MR03] Integrità della payload del messaggio REST
========================================================

.. _scenario-7:

4.2.1. Scenario
---------------

Comunicazione tra richiedente ed erogatore che assicuri a livello di
messaggio:

-  Integrità della payload del messaggio

Nel caso in cui il certificato per garantire l’integrità è valido anche
per identificare il soggetto richiedente, il presente profilo estende
M2MR01 o M2MR02, e quindi viene assicurato:

-  autenticazione del soggetto richiedente, quale organizzazione o unità
   organizzativa richiedente, o entrambe le parti.

.. _descrizione-7:

4.2.2. Descrizione
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
dell’erogatore includendo il certificato X.509 e la firma della payload
del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida l’integrità della payload del messaggio firmato. Se la verifica e
la validazione sono superate, l’erogatore consuma la richiesta e produce
la relativa risposta.

.. _dettaglio-7:

4.2.3. Dettaglio
----------------

|image0|

.. _flusso-delle-interazioni-7:

4.2.3.1. Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT:

-  include o referenzia il certificato X.509 riconosciuto
   dall’erogatore.

-  include almeno le claim per referenziare:

   -  il digest della payload del messaggio;

   -  l’algoritmo per il calcolo del digest della payload del messaggio.

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma del token JWT e verifica il digest
della payload del messaggio.

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

.. _regole-di-processamento-7:

4.2.4. Regole di processamento
------------------------------

**A: Richiesta**

1. Il richiedente predispone il body del messaggio (ad esempio un
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

   b. la payload del jwt deve contenere almeno i seguenti claim:

      iv. pda [1]_: contenente l’algoritmo di hashing utilizzato per il
          calcolo del digest della payload del messaggio

      v.  mpd [2]_: contenente il digest della payload del messaggio

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

10. Se il certificato è valido anche per identificare il soggetto
    richiedente, l’erogatore autentica lo stesso

11. L’erogatore calcola il digest della payload del messaggio
    utilizzando l’algoritmo indicato nel claim pda.

12. L’erogatore verifica la corrispondenza tra il digest presente nel
    claim mpd contenuto nel payload del token JWT rispetto a quanto
    calcolato al passo precedente.

13. Se le azioni da 6 a 12 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nelle claim alg e pda
   si fa riferimento agli algoritmi indicati sezione “\ `Elenco degli
   algoritmi <#_dm3er5ua5pkp>`__\ ”.

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della risposta da parte dell’erogatore al richiedente.

.. _tracciato-5:

4.2.4.1. Tracciato
~~~~~~~~~~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
richiedente all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

+--------------------------------------------------------+
| POST http://localhost:8080/ws-test/service/hello/echo/ |
|                                                        |
| Accept:text/xml                                        |
|                                                        |
| Authorization: eyJhbGciOiJSUzI1NiIsInR5c.vz8...        |
|                                                        |
| .                                                      |
|                                                        |
| .                                                      |
|                                                        |
| .                                                      |
+--------------------------------------------------------+

Esempio porzione token JWT

+--------------------------------------------------------------------------+
| header                                                                   |
|                                                                          |
| {                                                                        |
|                                                                          |
| "alg": "RS256",                                                          |
|                                                                          |
| "typ": "JWT",                                                            |
|                                                                          |
| "x5c": [                                                                 |
|                                                                          |
| "MIICyzCCAbOgAwIBAgIEC..."                                               |
|                                                                          |
| ]                                                                        |
|                                                                          |
| }                                                                        |
|                                                                          |
| payload                                                                  |
|                                                                          |
| {                                                                        |
|                                                                          |
| "pda":"S256",                                                            |
|                                                                          |
| "mpd":"B89AB4CA23D27F197AAE30F50843F0136900A1A154DCA00CDD8A5B8B4D071500" |
|                                                                          |
| }                                                                        |
+--------------------------------------------------------------------------+

Esempio del body del messaggio

+------------------------+
| {                      |
|                        |
| "testo":"Hello world!" |
|                        |
| }                      |
+------------------------+

Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al certificato X.509 (x5c)

-  algoritmi di firma e digest (alg).

-  algoritmo di hashing per calcolare il digest del body (pda)

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto presente nella sezione “\ `Elenco degli
algoritmi <#_dm3er5ua5pkp>`__\ ”, nonché la modalità di inclusione o
referenziazione del certificato x509.

.. [1]
   Il presente documento ha individuato il claim con sigla “pda” al fine
   di indicare in maniera univoca per la pubblica amministrazione
   italiana il valore dell’algoritmo di hashing utilizzato per il
   calcolo del digest della payload del messaggio.

.. [2]
   Il presente documento ha individuato il claim con sigla “mpd” al fine
   di gestire in maniera univoca per la pubblica amministrazione
   italiana il valore del digest relativo della payload del messaggio,

.. |image0| image:: ./media/image5.png
   :width: 2.47917in
   :height: 1.3125in
