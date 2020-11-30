[ID_AUTH_SOAP_02] Direct Trust con certificato X.509 su SOAP con con unicità del token/messaggio
================================================================================================

Il seguente profilo estende il profilo ID_AUTH_SOAP_01. Comunicazione
tra fruitore ed erogatore che assicuri a livello di messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack.

   8. .. rubric:: Descrizione
         :name: descrizione-3

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1].

Si assume l’esistenza di un trust tra fruitore ed erogatore, che
permette il riconoscimento da parte dell’erogatore del certificato
X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità di
scambio dei certificati X.509, non condiziona il presente profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509,
valida la firma dei claim ed garantisce l’accesso al fruitore. Se la
verifica e la validazione sono superate, l’erogatore consuma la
richiesta e produce la relativa risposta.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
       deactivate Fruitore

*Figura 4 - Accesso del Fruitore*

.. _regole-di-processamento-3:

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore aggiunge al messaggio l’header WS-Addressing e l’elemento
   <wsu:Timestamp> composto dagli elementi <wsu:Created> e <wsu:Expires>

3. Il fruitore calcola la firma per gli elementi significativi del
   messaggio, in particolare <wsa:To> e <wsa:MessageID> del blocco
   WS-Addressing e <wsu:Timestamp>. Il digest è firmato usando la chiave
   privata associata al certificato X.509 del fruitore. L’elemento
   <Signature> è posizionato nell’header <Security> del messaggio.

4. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header <Security>, i seguenti elementi previsti
   nella specifica ws-security:

   a. <wsse:BinarySecurityToken>

   b. <wsse:KeyIdentifier>

   c. <wsse:SecurityTokenReference>

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

1. L’erogatore verifica il contenuto dell’elemento <wsu:Timestamp>
   nell’header del messaggio al fine di verificare la validità temporale
   del messaggio.

2. L’erogatore verifica la corrispondenza tra se stesso e quanto
   definito nell’elemento <wsa:To> del blocco WS-Addressing.

3. L’erogatore verifica l’univocità del <wsa:MessageID> del blocco
   WS-Addressing

4. L’erogatore recupera il certificato X.509 referenziato nell’header
   <Security>.

5. L’erogatore verifica il certificato secondo i criteri del trust.

6. L’erogatore valida l’elemento <Signature> nell’header <Security>.

7. L’erogatore garantisce l’accesso al fruitore.

8. Se le azioni da 6 a 12 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato.

Note:

-  In merito agli algoritmi da utilizzare nell’elemento <Signature>
   rispettivamente <DigestMethod>, <SignatureMethod> e
   <CanonicalizationMethod> si fa riferimento agli algoritmi indicati al
   capitolo 7 Elementi di sicurezza,

-  Un meccanismo simile può essere utilizzato specularmente per
   l’erogatore.

   10. .. rubric:: Esempio
          :name: esempio-1

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore relativo ad un servizio di
echo.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecur
   ity-secext-1.0.xsd"
   
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecuri
   ty-utility-1.0.xsd"
   
   ds="http://www.w3.org/2000/09/xmldsig#"
   
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"

.. code-block:: python

   <?xml version="1.0"?>
   
   <soap:Envelope
   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"\ >
   
   <soap:Header>
   
   <wsse:Security
   xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-w
   ssecurity-secext-1.0.xsd"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   soap:mustUnderstand="1"\ >
   
   <wsse:BinarySecurityToken
   EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss
   -soap-message-security-1.0#Base64Binary"
   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x5
   09-token-profile-1.0#X509v3"
   wsu:Id="X509-bf881daf-371a-4d18-9502-d9f92af9a949"\ >\ MIICqDCCAZ
   CgAwIBAgIEXLSSUTANBgkqhkiG9w0BAQsFADAWMRQwEgYDVQQDDAttb2RpU2VjUHJvZjA
   eFw0xOTA0MTUxNDE2NDlaFw0yNDA0MTUxNDE2NDlaMBYxFDASBgNVBAMMC21vZGlTZWNQ
   cm9mMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvBJNKBiLS+ZcmwGUku5l2
   FKeHogeSZejjOOrO2Ag6DGPXo1MtHt2XwgUXmgT+v0IjhZp5XH2XbwSWw2EMWSG3Zz0CJ
   ILqWGPg0M/LxaIZAxSdxJpVNWg/profO+xKz0B6QHK+I0yecHg7TtI4es9AuDyR4pKslp
   cXyMEqJQ7m5N8v2e4WldeHF2SRN/ereEOuewEi15c7akh4TdkGdiwOSif2AXIugHRgdpH
   jH86iJxFu24IJmBA7C5tytz7mfKollGhI9+2d0902ayVshCV4/pmnX0pDiGayV1C6SDPT
   bapXKXJrp1+fBHaUkDY+W/2Q9sC4o8pttmcpHeMRxFDkwIDAQABMA0GCSqGSIb3DQEBCw
   UAA4IBAQALwKbIm8S2BpYpHaqMwJLeWBPCaDeT7J+KDj39Ac3YxDb8E/hGM+Hn1mq2ssY
   qu5JTvuAQ9o8v3UpcIct15RPgOKYfBzxnH1h2vCavpiFCFTc6UoQgPBZGyyNOOKNOxEnX
   tW7ff1gl2GRLIWXlXDf1fdX7VJVBqWfBvivhIbsDa5LRBCrNsXORx2azUb5QBgMm2UZJx
   YA3+dFRgYmLSY/RyRLf0o03lwCRhAyrU7ya9IMYgrxgjEos2fHB2IGJJ1Wh+gTQWMP+wJ
   ymlC0qyjTHx5pyZOzJGtH5HnaVU7EgtxdBRC9dTlWVpNgmD8nS6Yr/am5cZJZrkIHRyfx
   qkA2W\ </wsse:BinarySecurityToken>
   
   <wsu:Timestamp
   wsu:Id="TS-09f1357c-beb4-4804-9410-76c5a06e2e48"\ >
   
   <wsu:Created>\ 2019-04-15T15:02:15.515Z\ </wsu:Created>
   
   <wsu:Expires>\ 2019-04-15T15:07:15.515Z\ </wsu:Expires>
   
   </wsu:Timestamp>
   
   <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
   Id="SIG-4d949c5b-968b-4fd5-be67-4cd1d1a41ce3"\ >
   
   <ds:SignedInfo>
   
   <ds:CanonicalizationMethod
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces
   xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   PrefixList="soap"\ />
   
   </ds:CanonicalizationMethod>
   
   <ds:SignatureMethod
   Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"\ />
   
   <ds:Reference
   URI="#TS-09f1357c-beb4-4804-9410-76c5a06e2e48"\ >
   
   <ds:Transforms>
   
   <ds:Transform
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces
   xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap
   wsse"\ />
   
   </ds:Transform>
   
   </ds:Transforms>
   
   <ds:DigestMethod
   Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"\ />
   
   <ds:DigestValue>\ HPYjNXdxIuJIWk1EArE+8PIgyWt5nAD+upwcjOSDB20=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   <ds:Reference
   URI="#id-27c23bc8-0c4f-4d98-b046-6e590ea9661b"\ >
   
   <ds:Transforms>
   
   <ds:Transform
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces
   xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   PrefixList="soap"\ />
   
   </ds:Transform>
   
   </ds:Transforms>
   
   <ds:DigestMethod
   Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"\ />
   
   <ds:DigestValue>\ MJzRD4ZRMsFOxskbnfNV9BnDTCLxuLSnmZ8I4IjaxHw=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   <ds:Reference
   URI="#id-fb4c1fa0-e804-4169-b70e-5b55c5f9d912"\ >
   
   <ds:Transforms>
   
   <ds:Transform
   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"\ >
   
   <ec:InclusiveNamespaces
   xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   PrefixList="soap"\ />
   
   </ds:Transform>
   
   </ds:Transforms>
   
   <ds:DigestMethod
   Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"\ />
   
   <ds:DigestValue>\ MIi+ovLTqYu1HqxUtmUnuhVdMmNKOpOX8vn/fKjvQFU=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   </ds:SignedInfo>
   
   <ds:SignatureValue>\ SBYs6aikHbfsHHV04ifV/ljVTysxNLRTPU6gsOGJamWG
   YLMPqOETjBf+NFJhPDVdolQSSHw0SD7uA/RlYkE9amRH1K+hoaUIa/PEhPgC1io/LqZdi
   3rt+b8uRlk+CXcUKOObgf/N960F/sM6s0ArKQxg/Yx6pqWamXBXo0PH/1FvHSgwdA62s0
   +Sli96qY0EnJPoyKIrqzskiscLXI1jCe8sesyA+xtJ0qBdFKAn2af48sVStPFv4gizC8+
   bsCRpQ36ihUIlI8DInJ13EgoKV9/rC4PheExO7HvSNTpBFdQt+Wr9wAb3oHq4urRBdugA
   6mX2xaJ8/XyZVajivvuVTw==\ </ds:SignatureValue>
   
   <ds:KeyInfo Id="KI-dab2ce54-b000-439a-bcc2-9b8249626a1c"\ >
   
   <wsse:SecurityTokenReference
   xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-w
   ssecurity-secext-1.0.xsd"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:Id="STR-068909fe-1a64-4cf1-bd5a-355a20b0495f"\ >
   
   <wsse:Reference URI="#X509-bf881daf-371a-4d18-9502-d9f92af9a949"
   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x5
   09-token-profile-1.0#X509v3"\ />
   
   </wsse:SecurityTokenReference>
   
   </ds:KeyInfo>
   
   </ds:Signature>
   
   </wsse:Security>
   
   <Action
   xmlns="http://www.w3.org/2005/08/addressing"\ >\ http://profile.s
   ecurity.modi.agid.org/HelloWorld/sayHi\ </Action>
   
   <MessageID xmlns="http://www.w3.org/2005/08/addressing"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:Id="id-fb4c1fa0-e804-4169-b70e-5b55c5f9d912"\ >\ urn:uuid:46d
   a4ec1-f962-4f24-8524-48bb74b505d7\ </MessageID>
   
   <To xmlns="http://www.w3.org/2005/08/addressing"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:Id="id-27c23bc8-0c4f-4d98-b046-6e590ea9661b"\ >\ http://local
   host:8080/security-profile/echo\ </To>
   
   <ReplyTo xmlns="http://www.w3.org/2005/08/addressing"\ >
   
   <Address>\ http://www.w3.org/2005/08/addressing/anonymous\ </Ad
   dress>
   
   </ReplyTo>
   
   </soap:Header>
   
   <soap:Body>
   
   <ns2:sayHi
   xmlns:ns2="http://profile.security.modi.agid.org/"\ >
   
   <arg0>\ OK\ </arg0>
   
   </ns2:sayHi>
   
   </soap:Body>
   
   </soap:Envelope>

Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al security token (BinarySecurityToken)

-  algoritmi di canonizzazione (CanonicalizationMethod)

-  algoritmi di firma (SignatureMethod).

-  algoritmo per il digest (DigestMethod)

Le parti, in base alle proprie esigenze, usano gli algoritmi indicati al
capitolo 7 Elementi di sicurezza, nonché la modalità di inclusione o
referenziazione del certificato X.509.

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
