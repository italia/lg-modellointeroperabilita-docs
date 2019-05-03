Integrità
=========

[IDAS03] Integrità della payload del messaggio SOAP
---------------------------------------------------

.. _integrita-scenario-6:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  Integrità della payload del messaggio.

Nel caso in cui il certificato per garantire l’integrità è valido anche
per identificare il soggetto fruitore, il presente profilo estende
**IDAS01** o **IDAS02**, e quindi viene assicurato:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

.. _integrita-descrizione-6:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un `trust`_ tra fruitore ed erogatore,
che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_ non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e la
firma della payload del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida l'integrità della payload del messaggio firmato. Se la verifica e
la validazione sono superate, l’erogatore consuma la richiesta e produce
la relativa risposta.

.. _integrita-dettaglio-6:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Integrità della payload del messaggio
   :alt: Integrità della payload del messaggio

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F


Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore calcola la firma della payload del messaggio usando
   l’XML Signature. Il digest è firmato usando la chiave privata
   associata al certificato X.509 del fruitore. L’elemento
   ``<Signature>`` è posizionato nell’header ``<Security>`` del messaggio.

3. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   d. ``<wsse:BinarySecurityToken>``

   e. ``<wsse:KeyIdentifier>``

   f. ``<wsse:SecurityTokenReference>``

4. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

5. L’erogatore recupera il certificato X.509 referenziato nell’header
   ``<Security>``.

6. L’erogatore verifica il certificato secondo i criteri del trust.

7. L’erogatore valida la firma verificando l’elemento <Signature>
   nell’header ``<Security>``.

8. Se il certificato è valido anche per identificare il soggetto
   fruitore, l’erogatore autentica lo stesso

9. Se le azioni da 5 a 8 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   <Signature> rispettivamente ``<DigestMethod>``,``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` si fa riferimento agli algoritmi indicati
   alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della payload del del messaggio risposta dell’erogatore al
   fruitore.

.._integrita-tracciato-4:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

  soap="http://schemas.xmlsoap.org/soap/envelope/"
  wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
  ds="http://www.w3.org/2000/09/xmldsig#"
  ec="http://www.w3.org/2001/10/xml-exc-c14n#"
  "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

   <soap:Envelope>
     <soap:Header>
       <wsse:Security soap:mustUnderstand="1">
         <wsse:BinarySecurityToken EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"    wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIBAgIECxY+9TAhkiG9w...
         </wsse:BinarySecurityToken>
         <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">
           <ds:SignedInfo>
             <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
               <ec:InclusiveNamespaces PrefixList="soap" />
             </ds:CanonicalizationMethod>
             <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
               <ds:Reference URI="#bd-567d101-aed1-789e-81cb-5ae1c5dbef1a"> <ds:Transforms>
                 <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                   <ec:InclusiveNamespaces PrefixList="soap" />
                 </ds:Transform>
               </ds:Transforms>
               <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
               <ds:DigestValue>0cJNCJ1W8Agu66fGTXlPRyy0EUNUQ9OViFlm8qf8Ysw=</ds:DigestValue>
             </ds:Reference>
           </ds:SignedInfo>
           <ds:SignatureValue>AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...</ds:SignatureValue>
           <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8">
             <wsse:SecurityTokenReference wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3">
              <wsse:Reference URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7" ValueType="http://docs.oasis-open.org/   wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>          </wsse:SecurityTokenReference>
           </ds:KeyInfo>
         </ds:Signature>
       </wsse:Security>
        </soap:Header>
     <soap:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"    wsu:id="bd-567d101-aed1-789e-81cb-5ae1c5dbef1a">
       <ns2:sayHi xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">
         <arg0>Hello World!</arg0>
       </ns2:sayHi>
     </soap:Body>
   </soap:Envelope>

Il codice rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``)

-  algoritmo per il digest (``DigestMethod``)

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi`_
nonché la modalità di inclusione o referenziazione del certificato X.509.

[IDAR03] Integrità della payload messaggio REST
---------------------------------------------------

.. _integrita-scenario-7:

Scenario
^^^^^^^^

Il presente profilo estende IDAR01 o IDAR02, aggiungendo alla comunicazione tra fruitore ed erogatore
a livello di messaggio:

-  Integrità della payload del messaggio.

Si adottano le indicazione riportate in :rfc:`7231`. 

Considereremo sempre richieste e risposte complete,
con i metodi standard definiti in :rfc:`7231#section-4`.

Questo scenario non copre quindi `Range Requests` :rfc:`7233`
o  :httpmethod:`PATCH` che trasmette una rappresentazione
parziale.


.. _integrita-descrizione-7:

Descrizione
^^^^^^^^^^^

Il presente profilo propone l’utilizzo di:

- semantica HTTP :RFC:`7231`;

- ``Digest`` HTTP header :RFC:`3230` per l'integrità della rappresentazione della risorsa;

- JSON Web Token (JWT) definita dall’ :RFC:`7519`;

- JSON Web Signature (JWS) definita dall’ :RFC:`7515`.

Si assume l’esistenza di un `trust`_ tra fruitore ed erogatore,
che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_ non condiziona il presente
profilo.

.. _integrita-dettaglio-7:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Integrità del messaggio
   :alt: Integrità del messaggio

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>F: Calcola il Digest del messaggio
      F->>F: Crea la struttura da firmare
      F->>F: Firma la struttura
      F->>E: Richiesta
      activate E
      E->>E: Verifica claim JWT
      E->>E: Verifica firma JWT
      E->>E: Verifica header
      E->>E: Verifica digest
      E-->>F: Risposta
      deactivate E
      deactivate F

.. _regole-di-processamento-7:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

**A: Richiesta**

1. Il fruitore predispone il body del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore calcola il valore del ``Digest`` header dei `representation data`_ secondo
   le indicazioni in :RFC:`3230`

3. Il fruitore individua l'elenco degli HTTP Header da firmare, inclusi ``Digest``,
   :httpheader:`Content-Type` e :httpheader:`Content-Encoding`

4. Il fruitore crea la struttura o la stringa da firmare in modo che includa gli http header da proteggere,
   i riferimenti temporali di validità della firma e degli estremi della comunicazione, ovvero:

   a. il `Jose Header`_  con almeno i ``parameter``:

      -  `alg`_ con l’algoritmo di firma
      -  `typ`_ uguale a ``JWT``

      - una o più delle seguenti opzioni per referenziare il certificato X.509:

           * `x5u`_ (X.509 URL)
           * `x5c`_ (X.509 Certificate Chain)
           * `x5t#256`_ (X.509 Certificate SHA-256 Thumbprint)

   b. i seguenti claim obbligatori:

      * i riferimenti temporali di emissione e scadenza: `iat`_ , `exp`_.
        Se il flusso richiede di verificare l'istante di prima validità del token, si può
        usare il claim `nbf`_.
      * il riferimento dell'erogatore in `aud`_;


   c. i seguenti claim, secondo la logica del servizio:

      - `sub`_: oggetto (`principal` see :rfc:`3744#section-2`) dei claim contenuti nel jwt
      - `iss`_: identificativo del mittente
      - `jti`_: identificativo del JWT, per evitare replay attack

   d. il claim ``signed_headers`` [#signed_headers_claim]_ con gli header http da proteggere ed i rispettivi valori, ovvero:
   
      - ``digest``
      - ``content-type``
      - ``content-encoding``
      
3. il fruitore firma il token adottando la `JWS Compact Serialization`_

4. il fruitore posiziona il ``JWT`` nell’ ``Authorization`` header

5. Il fruitore spedisce il messaggio all’erogatore.

**B: Risultato**

6.  L’erogatore decodifica il  ``JWT`` presente in ``Authorization`` header e valida
    i claim contenuti nel `Jose Header`_, in particolare verifica:

    - il contenuto dei claim `iat`_ ed `exp`_;
    - la corrispondenza tra se stesso e il claim `aud`_;
    - l'univocità del claim `jti`_

7.  L’erogatore recupera il certificato X.509 referenziato nel `Jose Header`_

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del ``JWT``

10. L'erogatore verifica la corrispondenza tra i valori degli header
    passati nel messaggio e quelli presenti nel claim ``signed-header``

11. L'erogatore quindi verifica la corrispondenza tra ``Digest`` ed il payload body ricevuto

12. Se le azioni da 6 a 11 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per gli algoritmi da utilizzare in `alg`_ e ``Digest``
   si veda `Elenco degli algoritmi`_

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della risposta da parte dell’erogatore al fruitore.
   In questo caso si ricorda che ``Digest`` fa\' riferimento al checksum del
   payload body della `selected representation`_. Per una richiesta con :httpmethod:`HEAD`
   il server deve ritornare il checksum dell'ipotetico payload body ritornato dalla
   corrispondente richiesta con :httpmethod:`GET` [#cite_selected_representation]_.

.. _integrita-tracciato-5:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

.. code-block:: http
   :caption: Richiesta HTTP con `Digest` e representation metadata

   POST https://api.erogatore.org/service/v1/hello/echo/ HTTP/1.1
   Accept: application/json
   Agid-JWT-Signature: eyJhbGciOiJSUzI1NiIsInR5c.vz8...
   Digest: SHA-256=cFfTOCesrWTLVzxn8fmHl4AcrUs40Lv5D275FmAZ96E=
   Content-Type: application/json
   Content-Encoding: identity


   {"testo": "Ciao mondo"}


.. code-block:: python
   :caption: Porzione JWT con campi protetti dalla firma

   # header
   {
     "alg": "ES256",
     "typ": "JWT",
     "x5c": [
       "MIICyzCCAbOgAwIBAgIEC..."
     ]
   }
   # payload
   {
     "aud": "https://api.erogatore.org/service/v1/hello/echo"
     "iat": 1516239022,
     "nbf": 1516239022,
     "exp": 1516239024,
     "signed_headers": [
         {"digest": "SHA-256=cFfTOCesrWTLVzxn8fmHl4AcrUs40Lv5D275FmAZ96E="},
         {"content-type": "application/json"},
         {"content-encoding": "identity"},
     ],
   }


Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

- include tutti gli elementi del ``JWT`` utilizzati in **IDAR02**

- mette in ``minuscolo`` i nomi degli header firmati

- utilizza il claim custom ``signed_headers`` contenente una lista di json objects
  per supportare la firma di più header ed eventualmente verificare il loro ordinamento

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi`_
nonché la modalità di inclusione o referenziazione del certificato X.509.


.. [#signed_headers_claim]
   Il presente documento ha individuato il claim "signed_headers"
   per contenere l'elenco degli header firmati.

.. [#cite_selected_representation] Per coerenza con :rfc:`7231#section-3.1` "In a response to a
   HEAD request, the representation header fields describe the
   representation data that would have been enclosed in the payload body
   if the same request had been a GET."

.. discourse::
   :topic_identifier: 8908


.. _`Elenco degli algoritmi`: elenco-degli-algoritmi.html

.. _`trust`: ../doc_04_cap_00.html


.. _`HTTP/1.1 Semantics and Content`: https://tools.ietf.org/html/rfc7231
.. _`selected representation`: https://tools.ietf.org/html/rfc7231#section-3
.. _`representation metadata`: https://tools.ietf.org/html/rfc7231#section-3.1
.. _`representation data`: https://tools.ietf.org/html/rfc7231#section-3.2


.. _`JWS Compact Serialization`: https://tools.ietf.org/html/rfc7515#section-7.1
.. _`Jose Header`: https://tools.ietf.org/html/rfc7515#section-4

.. _`alg`: https://tools.ietf.org/html/rfc7515#section-4.1.1
.. _`jku`: https://tools.ietf.org/html/rfc7515#section-4.1.2
.. _`jwk`: https://tools.ietf.org/html/rfc7515#section-4.1.3
.. _`kid`: https://tools.ietf.org/html/rfc7515#section-4.1.4
.. _`x5u`: https://tools.ietf.org/html/rfc7515#section-4.1.5
.. _`x5c`: https://tools.ietf.org/html/rfc7515#section-4.1.6
.. _`x5t#256`: https://tools.ietf.org/html/rfc7515#section-4.1.8


.. _`iss`: https://tools.ietf.org/html/rfc7519#section-4.1.1
.. _`sub`: https://tools.ietf.org/html/rfc7519#section-4.1.2
.. _`aud`: https://tools.ietf.org/html/rfc7519#section-4.1.3
.. _`exp`: https://tools.ietf.org/html/rfc7519#section-4.1.4
.. _`nbf`: https://tools.ietf.org/html/rfc7519#section-4.1.5
.. _`iat`: https://tools.ietf.org/html/rfc7519#section-4.1.6
.. _`jti`: https://tools.ietf.org/html/rfc7519#section-4.1.7

.. _`typ`: https://tools.ietf.org/html/rfc7519#section-5.1
.. _`cty`: https://tools.ietf.org/html/rfc7519#section-5.2

