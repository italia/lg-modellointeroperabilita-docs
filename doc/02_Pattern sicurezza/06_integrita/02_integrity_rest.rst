[INTEGRITY_REST_01] Integrità del payload messaggio REST
========================================================

Il presente profilo estende ID_AUTH_REST_01 o ID_AUTH_REST_02,
aggiungendo alla comunicazione tra fruitore ed erogatore a livello di
messaggio:

-  integrità del payload del messaggio

Si adottano le indicazione riportate in :rfc:`7231`. Considereremo sempre
richieste e risposte complete, con i metodi standard definiti in RFC
7231#section-4.

Questo scenario non copre quindi Range Requests :rfc:`7233` o HTTP method
PATCH che trasmette una rappresentazione parziale.

Descrizione
-----------

Il presente profilo propone l’utilizzo di:

-  semantica HTTP :rfc:`7231`;

-  Digest HTTP header :rfc:`3230` per l’integrità della rappresentazione
   della risorsa;

-  JSON Web Token (JWT) definita dall’ :rfc:`7519`;

-  JSON Web Signature (JWS) definita dall’ :rfc:`7515`.

Si assume l’esistenza di un trust tra fruitore ed erogatore, che
permette il riconoscimento da parte dell’erogatore del certificato
X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

.. mermaid::

  sequenceDiagram

    activate Fruitore
	activate Erogatore
    Fruitore->>+Erogatore: 1. Request()
	Erogatore-->>Fruitore: 2. Response
    deactivate Erogatore
    deactivate Fruitore


*Figura 8 - Integrità del payload del messaggio*

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore predispone il body del messaggio (ad esempio un oggetto
   JSON)

2. Il fruitore calcola il valore del Digest header dei representation
   data secondo le indicazioni in :rfc:`3230`

3. Il fruitore individua l’elenco degli HTTP Header da firmare, incluso
   Digest e se presenti :httpheader:`Content-Type` e HTTP header
   Content-Encoding

4. Il fruitore crea la struttura o la stringa da firmare in modo che
   includa gli http header da proteggere, i riferimenti temporali di
   validità della firma e degli estremi della comunicazione, ovvero:

   a. il JOSE Header con almeno i parameter:

      i.   alg con l’algoritmo di firma, vedi :rfc:`8725`

      ii.  typ uguale a JWT

      iii. una o più delle seguenti opzioni per referenziare il
           certificato X.509:

           -  x5u (X.509 URL)

           -  x5c (X.509 Certificate Chain)

           -  x5t#S256 (X.509 Certificate SHA-256 Thumbprint)

   b. i seguenti claim obbligatori:

      iv. i riferimenti temporali di emissione e scadenza: iat , exp. Se
          il flusso richiede di verificare l’istante di prima validità
          del token, si può usare il claim nbf.

      v.  il riferimento dell’erogatore in aud;

   c. i seguenti claim, secondo la logica del servizio:

      vi.   sub: oggetto (principal see :rfc:`3744#section-2`) dei claim
            contenuti nel jwt

      vii.  iss: identificativo del mittente

      viii. jti: identificativo del JWT, per evitare replay attack

   d. il claim signed_headers con gli header http da proteggere ed i
      rispettivi valori, ovvero:

      ix. Digest

      x.  Content-Type

      xi. Content-Encoding

5. il fruitore firma il token adottando la JWS Compact Serialization

6. il fruitore posiziona il JWS nell’header Agid-JWT-Signature

7. Il fruitore spedisce il messaggio all’erogatore.

**B: Risultato**

8.  L’erogatore decodifica il JWS presente in Agid-JWT-Signature header
    e valida i claim contenuti nel Jose Header, in particolare verifica:

    e. il contenuto dei claim iat ed exp;

    f. la corrispondenza tra se stesso e il claim aud;

    g. l’univocità del claim jti se presente.

9.  L’erogatore recupera il certificato X.509 referenziato nel JOSE
    Header

10. L’erogatore verifica il certificato secondo i criteri del trust

11. L’erogatore valida la firma verificando l’elemento Signature del JWS

12. L’erogatore verifica la corrispondenza tra i valori degli header
    passati nel messaggio e quelli presenti nel claim signed-header,
    Content-Type e Content-Encoding se presenti devono essere sempre
    firmati, come indicato nel punto A3

13. L’erogatore quindi verifica la corrispondenza tra Digest ed il
    payload body ricevuto

14. Se le azioni da 8 a 13 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per gli algoritmi da utilizzare in alg e Digest si vedano
   le Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
   ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della risposta da parte dell’erogatore al fruitore. In questo caso si
   ricorda che Digest fa riferimento al checksum del payload body della
   selected representation. Per una richiesta con :httpmethod:`HEAD` il
   server DEVE ritornare il checksum dell’ipotetico payload body
   ritornato dalla corrispondente richiesta con :httpmethod:`GET`.

Esempio
-------

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore.

Richiesta HTTP con Digest e representation metadata

.. code-block:: http

   POST https://api.erogatore.org/rest/service/v1/hello/echo/ HTTP/1.1
   Accept: application/json
   Agid-JWT-Signature: eyJhbGciOiJSUzI1NiIsInR5c.vz8...
   Digest: SHA-256=cFfTOCesrWTLVzxn8fmHl4AcrUs40Lv5D275FmAZ96E=
   Content-Type: application/json
   
   {"testo": "Ciao mondo"}

Porzione JWS con campi protetti dalla firma

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
     "signed_headers": [
       {"digest": "SHA-256=cFfTOCesrWTLVzxn8fmHl4AcrUs40Lv5D275FmAZ96E="},
       {"content-type": "application/json"}
     ],
   }

Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

-  include tutti gli elementi del JWS utilizzati in ID_AUTH_REST_02

-  mette in minuscolo i nomi degli header firmati

-  utilizza il claim custom signed_headers contenente una lista di json
   objects per supportare la firma di più header ed eventualmente
   verificare il loro ordinamento

Le parti, in base alle proprie esigenze, individuano gli specifici algoritmi
secondo quanto indicato nelle Linee Guida sulla sicurezza,
emanate dall'Agenzia per l'Italia Digitale ai sensi dell'articolo 71
del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

.. forum_italia::
   :topic_id: 21475
   :scope: document
