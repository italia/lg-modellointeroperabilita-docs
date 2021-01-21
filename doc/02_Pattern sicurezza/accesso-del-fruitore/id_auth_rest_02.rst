.. _id_auth_rest_02:

[ID_AUTH_REST_02] Direct Trust con certificato X.509 su REST con unicità del token/messaggio
============================================================================================

Il seguente profilo estende il profilo ID_AUTH_REST_01. Comunicazione
tra fruitore ed erogatore che assicuri a livello di messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti

-  la difesa dalle minacce derivanti dagli attacchi: Replay Attack
   quando il JWT o il messaggio non DEVONO DEVONO essere riprocessati.

Descrizione
-------------

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’:rfc:`7519`

-  JSON Web Signature (JWS) definita dall’:rfc:`7515`

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità di
scambio dei certificati X.509) non condiziona il presente profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio, inclusa la corrispondenza del
destinatario e l’intervallo di validità della firma.

L’erogatore verifica inoltre l’univocità dell’identificativo ricevuto
nel JWT.

Se la verifica e la validazione sono superate, l’erogatore consuma la
richiesta e produce la relativa risposta.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
      activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
      deactivate Fruitore

*Figura 6 - Accesso del Fruitore*

.. _regole-di-processamento-5:

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore predispone il payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il JWT popolando:

   a. il Jose Header con almeno i parameter:

      i.   alg con l’algoritmo di firma, vedi :rfc:`8725`

      ii.  typ uguale a JWT

      iii. una o più delle seguenti opzioni per referenziare il
           certificato X.509:

-  x5u (X.509 URL)

-  x5c (X.509 Certificate Chain)

-  x5t#S256 (X.509 Certificate SHA-256 Thumbprint)

   b. il payload del JWT coi claim rappresentativi degli elementi chiave
      del messaggio, contenente almeno:

      iv.  
      v.   i riferimenti temporali di emissione e scadenza: iat , exp.
           Se il flusso richiede di verificare l’istante di prima
           validità del token, si può usare il claim nbf.

      vi.  il riferimento dell’erogatore in aud;

      vii. un identificativo univoco del token jti. Se utile alla logica
           applicativa l’identificativo può essere anche collegato al
           messaggio.

3. il fruitore firma il token adottando la JWS Compact Serialization

4. il fruitore posiziona il JWT nell’ HTTP header Authorization

5. Il fruitore spedisce il messaggio all’erogatore.

**B: Risposta**

6.  L’erogatore decodifica il JWT presente in HTTP header Authorization
    e valida i claim contenuti nel Jose Header, in particolare verifica:

    c. il contenuto dei claim iat ed exp;

    d. la corrispondenza tra se stesso e il claim aud;

    e. l’univocità del claim jti

7.  L’erogatore recupera il certificato X.509 referenziato nel Jose
    Header

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del JWT

10. L’erogatore garantisce l’accesso al fruitore

11. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  In merito agli algoritmi da utilizzare si fa riferimento al capitolo
   7 Elementi di sicurezza.

-  Un meccanismo simile può essere utilizzato specularmente per
   l’erogatore.

Esempio
-----------

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP.

.. code-block:: http

   GET https://api.erogatore.org/rest/service/v1/hello/echo/Ciao HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

Esempio porzione JWT

.. code-block:: python

   # *header*
   {
	   "alg": "ES256",
	   "typ": "JWT",
	   "x5c": [
		   "MIICyzCCAbOgAwIBAgIEC..."
		   ]
   }
   
   # *payload*
   {
	   "aud": "https://api.erogatore.org/rest/service/v1/hello/echo"
	   "iat": 1516239022,
	   "nbf": 1516239022,
	   "exp": 1516239024,
	   "jti": "065259e8-8696-44d1-84c5-d3ce04c2f40d"
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

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato al capitolo 7 Elementi di sicurezza
nonché la modalità di inclusione o referenziazione del certificato
X.509.


