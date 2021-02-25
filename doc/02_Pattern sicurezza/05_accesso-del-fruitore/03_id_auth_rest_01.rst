[ID_AUTH_REST_01] Direct Trust con certificato X.509 su REST
============================================================

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

Descrizione
-----------

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’:rfc:`7519`

-  JSON Web Signature (JWS) definita dall’:rfc:`7515`

Si assume l’esistenza di un trust tra fruitore ed erogatore, che
permette il riconoscimento da parte dell’erogatore del certificato
X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità di
scambio dei certificati X.509, non condiziona il presente profilo.

Il fruitore inoltra un messaggio all’erogatore includendo o
referenziando il certificato X.509 e una porzione significativa del
messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio, inclusa la corrispondenza del
destinatario e l’intervallo di validità della firma. Se la verifica e la
validazione sono superate, l’erogatore elabora la richiesta e produce la
relativa risposta.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
      activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
      deactivate Fruitore

*Figura 5 - Accesso del Fruitore*

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore predispone il payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il JWT popolando:

   a. il JOSE Header con almeno i parameter:

      i.   alg con l’algoritmo di firma, vedi :rfc:`8725`

      ii.  typ uguale a JWT

      iii. una o più delle seguenti opzioni per referenziare il
           certificato X.509:

-  x5u (X.509 URL)

-  x5c (X.509 Certificate Chain)

-  x5t#S256 (X.509 Certificate SHA-256 Thumbprint)

   b. il payload del JWT coi claim rappresentativi degli elementi chiave
      del messaggio, contenente almeno:

      iv. i riferimenti temporali di emissione e scadenza: iat , exp. Se
          il flusso richiede di verificare l’istante di prima validità
          del token, si può usare il claim nbf.

      v.  il riferimento dell’erogatore in aud

3. il fruitore firma il token adottando la JWS Compact Serialization

4. il fruitore posiziona il JWT nell’ :httpheader:`Authorization`

5. Il fruitore spedisce il messaggio all’erogatore

**B: Risposta**

6.  L’erogatore decodifica il JWT presente in :httpheader:`Authorization`
    e valida i claim contenuti nel JOSE Header, in particolare verifica:

7.  il contenuto dei claim iat ed exp;

8.  la corrispondenza tra se stesso e il claim aud;

9.  L’erogatore recupera il certificato X.509 referenziato nel JOSE
    Header

10. L’erogatore verifica il certificato secondo i criteri del trust

11. L’erogatore valida la firma verificando l’elemento Signature del JWT

12. L’erogatore garantisce l’accesso al fruitore

13. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato

Note:

-  Gli algoritmi da utilizzare in alg sono indicati
   nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
   ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

-  Un meccanismo simile può essere utilizzato specularmente per
   l’erogatore.

-  Per prevenire il rischio di user-enumeration, i messaggi di errore di
   autenticazione non DEVONO fornire informazioni sull’esistenza o meno
   dell’utenza.

Esempio
-----------

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’erogatore.

Esempio porzione messaggio HTTP.

.. code-block:: http

   GET https://api.erogatore.org/rest/service/v1/hello/echo/Ciao HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

Esempio porzione JWT

.. code-block:: python

   # header
   
   {
   "alg": "ES256",
   "typ": "JWT",
   "x5c": [
   "MIICyzCCAbOgAwIBAgIEC..."
   ]
   }
   
   # *payload*
   {
   "iat": 1554382877,
   "nbf": 1554382877,
   "exp": 1554382879,
   "aud": "https://api.erogatore.org/rest/service/v1/hello/echo"
   }

Gli elementi presenti nel tracciato rispettano le seguenti scelte
implementative e includono:

-  l’intervallo temporale di validità, in modo che il JWT possa essere
   usato solo tra gli istanti nbf ed exp;

-  indica l’istante iat di emissione del JWT. Se le parti possono
   accordarsi nel considerarlo come l’istante iniziale di validità del
   token, :rfc:`7519` non assegna a questo claim nessun ruolo specifico
   nella validazione, a differenza di nbf;

-  il destinatario del JWT, che DEVE sempre essere validato;

-  contenuto della certificate chain X.509 (x5c)

-  algoritmi di firma e digest (alg).

Le parti, in base alle proprie esigenze, individuano gli specifici algoritmi 
secondo quanto indicato nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

.. forum_italia::
   :topic_id: 21471
   :scope: document
