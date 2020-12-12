[ID_AUTH_REST_02] Direct Trust con certificato X.509 su REST con unicità del token/messaggio
============================================================================================

Il seguente profilo estende il profilo ID_AUTH_REST_01. Comunicazione
tra fruitore ed erogatore che assicuri a livello di messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti

-  la difesa dalle minacce derivanti dagli attacchi: Replay Attack
   quando il JWT o il messaggio non DEVONO DEVONO essere riprocessati.

   14. .. rubric:: Descrizione
          :name: descrizione-5

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’RFC 7519

-  JSON Web Signature (JWS) definita dall’RFC 7515

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

      i.   alg con l’algoritmo di firma, vedi RFC 8725

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

   16. .. rubric:: Esempio
          :name: esempio-3

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP.

.. code-block:: http

   GET https://api.erogatore.org/rest/service/v1/hello/echo/Ciao
   HTTP/1.1
   
   Accept: application/json
   
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

Esempio porzione JWT

.. code-block:: python

   *# header*
   
   {
   
   "alg": "ES256",
   
   "typ": "JWT",
   
   "x5c": [
   
   "MIICyzCCAbOgAwIBAgIEC..."
   
   ]
   
   }
   
   *# payload*
   
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
   token, RFC 7519 non assegna a questo claim nessun ruolo specifico
   nella validazione, a differenza di nbf;

-  il destinatario del JWT, che DEVE sempre essere validato;

-  contenuto della certificate chain X.509 (x5c)

-  algoritmi di firma e digest (alg).

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato al capitolo 7 Elementi di sicurezza
nonché la modalità di inclusione o referenziazione del certificato
X.509.

6. .. rubric:: 
      Integrità
      :name: integrità

   11. .. rubric:: [INTEGRITY_SOAP_01] Integrità del payload del
          messaggio SOAP
          :name: integrity_soap_01-integrità-del-payload-del-messaggio-soap

Il presente profilo estende ID_AUTH_SOAP_01 o ID_AUTH_SOAP_02,
aggiungendo alla comunicazione tra fruitore ed erogatore a livello di
messaggio:

-  integrità del payload del messaggio.

   17. .. rubric:: Descrizione
          :name: descrizione-6

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1.

Si assume l’esistenza di un trust tra fruitore ed erogatore, che
permette il riconoscimento da parte dell’erogatore del certificato
X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e la
firma del payload del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida l’integrità del payload del messaggio firmato. Se la verifica e
la validazione sono superate, l’erogatore consuma la richiesta e produce
la relativa risposta.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
       deactivate Fruitore

*Figura 7 - Integrità del payload del messaggio*

.. _regole-di-processamento-6:

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore calcola la firma del payload del messaggio usando l’XML
   Signature. Il digest è firmato usando la chiave privata associata al
   certificato X.509 del fruitore. L’elemento <Signature> è posizionato
   nell’header <Security> del messaggio.

3. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header <Security>, i seguenti elementi previsti
   nella specifica ws-security:

   a. <wsse:BinarySecurityToken>

   b. <wsse:KeyIdentifier>

   c. <wsse:SecurityTokenReference>

4. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

5. L’erogatore recupera il certificato X.509 referenziato nell’header
   <Security>.

6. L’erogatore verifica il certificato secondo i criteri del trust.

7. L’erogatore valida la firma verificando l’elemento <Signature>
   nell’header <Security>.

8. Se il certificato è valido anche per identificare il soggetto
   fruitore, l’erogatore autentica lo stesso

9. Se le azioni da 5 a 8 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   <Signature> rispettivamente <DigestMethod> , <SignatureMethod> e
   <CanonicalizationMethod> si fa riferimento agli algoritmi indicati al
   capitolo 7 Elementi di sicurezza.

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   del payload del messaggio risposta dell’erogatore al fruitore.

   19. .. rubric:: Esempio
          :name: esempio-4

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecur
   ity-secext-1.0.xsd"
   
   ds="http://www.w3.org/2000/09/xmldsig#"
   
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"

.. code-block:: python

   <soap:Envelope>
   
   <soap:Header>
   
   <wsse:Security soap:mustUnderstand="1"\ >
   
   <wsse:BinarySecurityToken
   EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss
   -soap-message-security-1.0#Base64Binary"
   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x5
   09-token-profile-1.0#X509v3"
   wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"\ >\ MIICyzCCAb
   OgAwIBAgIECxY+9TAhkiG9w...
   
   </wsse:BinarySecurityToken>
   
   <ds:Signature
   Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90"\ >
   
   <ds:SignedInfo>
   
   <ds:CanonicalizationMethod
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces PrefixList="soap" />
   
   </ds:CanonicalizationMethod>
   
   <ds:SignatureMethod
   Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
   
   <ds:Reference
   URI="#bd-567d101-aed1-789e-81cb-5ae1c5dbef1a"\ >
   <ds:Transforms>
   
   <ds:Transform
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces PrefixList="soap" />
   
   </ds:Transform>
   
   </ds:Transforms>
   
   <ds:DigestMethod
   Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
   
   <ds:DigestValue>\ 0cJNCJ1W8Agu66fGTXlPRyy0EUNUQ9OViFlm8qf8Ysw=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   </ds:SignedInfo>
   
   <ds:SignatureValue>\ AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...\ </
   ds:SignatureValue>
   
   <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8"\ >
   
   <wsse:SecurityTokenReference
   wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3"\ >
   
   <wsse:Reference URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"
   ValueType="http://docs.oasis-open.org/
   wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"\ />
   </wsse:SecurityTokenReference>
   
   </ds:KeyInfo>
   
   </ds:Signature>
   
   </wsse:Security>
   
   </soap:Header>
   
   <soap:Body
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:id="bd-567d101-aed1-789e-81cb-5ae1c5dbef1a"\ >
   
   <ns2:sayHi
   xmlns:ns2="http://example.profile.security.modi.agid.gov.it/"\ >
   
   <arg0>\ Hello World!\ </arg0>
   
   </ns2:sayHi>
   
   </soap:Body>
   
   </soap:Envelope>

Il codice rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al security token (BinarySecurityToken)

-  algoritmi di canonizzazione (CanonicalizationMethod)

-  algoritmi di firma (SignatureMethod)

-  algoritmo per il digest (DigestMethod)

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato al capitolo 7 Elementi di sicurezza
nonché la modalità di inclusione o referenziazione del certificato
X.509.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
       deactivate Fruitore

.. image:: ./media/image2.png
   :width: 4.68056in
   :height: 2.40278in
