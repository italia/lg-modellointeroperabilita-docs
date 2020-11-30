Termini e definizioni
=====================

+-----------------------------------+-----------------------------------+
| **[AgID]**                        | Agenzia per l’Italia Digitale     |
+-----------------------------------+-----------------------------------+
| **[CAD]**                         | Codice Amministrazione Digitale,  |
|                                   | D.lgs. 7 marzo 2005, n. 82        |
+-----------------------------------+-----------------------------------+
| **[PA]**                          | Pubblica Amministrazione          |
+-----------------------------------+-----------------------------------+
| **[UML]**                         | Linguaggio di modellazione        |
|                                   | unificato (Unified Modeling       |
|                                   | Language)                         |
+-----------------------------------+-----------------------------------+
| **[RPC]**                         | Remote procedure call             |
+-----------------------------------+-----------------------------------+
| **[SOAP]**                        | Simple Object Access Protocol     |
+-----------------------------------+-----------------------------------+
| **[REST]**                        | Representational State Transfer   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

4. .. rubric:: 
      Sicurezza di canale e/o identificazione delle organizzazioni
      :name: sicurezza-di-canale-eo-identificazione-delle-organizzazioni

   5. .. rubric:: [ID_AUTH_CHANNEL_01] Direct Trust Transport-Level
         Security
         :name: id_auth_channel_01-direct-trust-transport-level-security

Comunicazione tra fruitore ed erogatore che assicuri, a livello di
canale:

-  confidenzialità;

-  integrità;

-  identificazione dell’erogatore, quale organizzazione;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing.

   1. .. rubric:: Descrizione
         :name: descrizione

Il presente profilo assume l’esistenza di un trust tra fruitore ed
erogatore, che permette il riconoscimento del certificato X.509, o la CA
emittente dell’erogatore, così come previsto dal protocollo Transport
Layer Security.

La sequenza dei messaggi di richiesta/risposta avviene dopo aver
instaurato il canale di trasmissione sicuro.

.. mermaid::
   sequenceDiagram
   activate Fruitore
   activate Erogatore
   Fruitore->>+Erogatore: 1. Request()
   Erogatore-->>Fruitore: 2. Response
   deactivate Erogatore
   deactivate Fruitore

*Figura 1 - Sicurezza di canale e/o Autenticazione dell’erogatore*

Regole di processamento
-----------------------

Il canale sicuro tra erogatore e fruitore viene instaurato utilizzando
il protocollo TLS, secondo le modalità specificate al capitolo 7
Elementi di sicurezza.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta;

2. Il fruitore spedisce sul canale sicuro stabilito il messaggio di
   richiesta; all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce il risultato.

Come indicato in RFC 5246 l’impiego del protocollo TLS garantisce a
livello di canale:

-  l’autenticazione dell’erogatore identificato mediante il certificato
   X.509;

-  la confidenzialità dei dati scambiati;

-  l’integrità dei dati scambiati.

L’impiego del protocollo TLS, mitiga il rischio di:

-  Replay Attack;

-  Spoofing.

   6. .. rubric:: [ID_AUTH_CHANNEL_02] Direct Trust mutual
         Transport-Level Security
         :name: id_auth_channel_02-direct-trust-mutual-transport-level-security

Comunicazione tra fruitore ed erogatore che assicuri a livello di
canale:

-  confidenzialità;

-  integrità;

-  identificazione dell’erogatore e del fruitore, quale organizzazioni;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing.

   3. .. rubric:: Descrizione
         :name: descrizione-1

Il presente profilo assume l’esistenza di un trust tra fruitore (client)
ed erogatore (server), che permette il riconoscimento da entrambe le
parti dei certificati X.509, o le CA emittenti, così come previsto dal
protocollo Transport Layer Security.

La sequenza dei messaggi di richiesta/risposta avviene dopo aver
instaurato il canale di trasmissione sicuro.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
       deactivate Fruitore

*Figura 2 - Sicurezza di canale e/o Autenticazione delle organizzazioni*

.. _regole-di-processamento-1:

Regole di processamento
-----------------------

Il canale sicuro tra erogatore e fruitore viene instaurato in mutua
autenticazione utilizzando il protocollo TLS, secondo le modalità
specificate al capitolo 7 Elementi di sicurezza.

**A: Richiesta**

1. Il fruitore costruisce un messaggio di richiesta.

2. Il fruitore spedisce utilizzando canale sicuro stabilito con il il
   messaggio di richiesta all’interfaccia di servizio dell’erogatore.

**B: Risposta**

3. L’erogatore elabora il messaggio e restituisce il risultato.

Come indicato in RFC 5246 l’impiego del protocollo TLS garantisce a
livello di canale:

-  l’autenticazione di erogatore e fruitore identificati mediante
   certificati X.509;

-  la confidenzialità dei dati scambiati;

-  l’integrità dei dati scambiati.

L’impiego del protocollo TLS, mitiga il rischio di:

-  Replay Attack;

-  Spoofing.

5. .. rubric:: 
      Accesso del soggetto fruitore
      :name: accesso-del-soggetto-fruitore

   7. .. rubric:: [ID_AUTH_SOAP_01] Direct Trust con certificato X.509
         su SOAP
         :name: id_auth_soap_01-direct-trust-con-certificato-x.509-su-soap

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitrice, o entrambe le parti.

   5. .. rubric:: Descrizione
         :name: descrizione-2

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1.

Si assume l’esistenza di un trust tra fruitore ed erogatore, che
permette il riconoscimento da parte dell’erogatore del certificato
X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità di
scambio dei certificati X.509) non condiziona il presente profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. mermaid::

     sequenceDiagram
     
      activate Fruitore
       activate Erogatore
      Fruitore->>+Erogatore: 1. Request()
      Erogatore-->>Fruitore: 2. Response
      deactivate Erogatore
       deactivate Fruitore

*Figura 3 - Accesso del Fruitore*

.. _regole-di-processamento-2:

Regole di processamento
-----------------------

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore aggiunge al messaggio l’header WS-Addressing e l’elemento
   <wsu:Timestamp> composto dagli elementi <wsu:Created> e <wsu:Expires>

3. Il fruitore calcola la firma per gli elementi significativi del
   messaggio, in particolare <wsu:Timestamp> e <wsa:To> del blocco
   WS-Addressing. Il digest è firmato usando la chiave privata associata
   al certificato X.509 del fruitore. L’elemento <Signature> è
   posizionato nell’header <Security> del messaggio.

4. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header <Security>, i seguenti elementi previsti
   nella specifica ws-security:

   a. <wsse:BinarySecurityToken>

   b. <wsse:KeyIdentifier>

   c. <wsse:SecurityTokenReference>

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6.  L’erogatore verifica il contenuto dell’elemento <wsu:Timestamp>
    nell’header del messaggio al fine di verificare la validità
    temporale del messaggio.

7.  L’erogatore verifica la corrispondenza tra se stesso e quanto
    definito nell’elemento <wsa:To> del blocco WS-Addressing.

8.  L’erogatore recupera il certificato X.509 referenziato nell’header
    <Security>.

9.  L’erogatore verifica il certificato secondo i criteri del trust.

10. L’erogatore valida l’elemento <Signature> nell’header <Security>.

11. L’erogatore garantisce l’accesso al fruitore.

12. Se le azioni da 6 a 11 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  In merito agli algoritmi da utilizzare nell’elemento <Signature>
   rispettivamente <DigestMethod>, <SignatureMethod> e
   <CanonicalizationMethod> si fa riferimento agli algoritmi indicati al
   capitolo 7 Elementi di sicurezza,

-  Un meccanismo simile può essere utilizzato specularmente per
   l’erogatore.

   7. .. rubric:: Esempio
         :name: esempio

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell'erogatore relativo ad un servizio di
echo.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://www.w3.org/2003/05/soap-envelope"
   
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecur
   ity-secext-1.0.xsd"
   
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecuri
   ty-utility-1.0.xsd"
   
   ds="http://www.w3.org/2000/09/xmldsig#"
   
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"

.. code-block:: python

   <?xml version="1.0"?>
   
   <soap:Envelope
   xmlns:soap="http://www.w3.org/2003/05/soap-envelope"\ >
   
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
   wsu:Id="X509-39011475-65d5-446e-ba38-be84220fd720"\ >\ MIICqDCCAZ
   CgAwIBAgIEXLSSUTANBgkqhkiG9w0BAQsFADAW...\ </wsse:BinarySecurityTok
   en>
   
   <wsu:Timestamp
   wsu:Id="TS-819df7b7-379d-48f7-8d9c-28c5b5d252f0"\ >
   
   <wsu:Created>\ 2019-04-15T14:53:34.649Z\ </wsu:Created>
   
   <wsu:Expires>\ 2019-04-15T14:58:34.649Z\ </wsu:Expires>
   
   </wsu:Timestamp>
   
   <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
   Id="SIG-6e09e972-cbe6-43fc-a10c-38e6dce56dbe"\ >
   
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
   URI="#TS-819df7b7-379d-48f7-8d9c-28c5b5d252f0"\ >
   
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
   
   <ds:DigestValue>\ K/3Fq1fYjG5PXv8UlKBuT4XBCWudGR5w2M10wPcZ/Yo=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   <ds:Reference
   URI="#id-96f9b013-17e5-489d-8068-52c3f1345c75"\ >
   
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
   
   <ds:DigestValue>\ eH3Vlc3l19NbBawDOuFDN11BfmbgGAnl6Z4LpJVM3UM=\ *
   *</ds:DigestValue>
   
   </ds:Reference>
   
   </ds:SignedInfo>
   
   <ds:SignatureValue>\ jAtZqkfRcFJW+jx9YDv+r2Q8V4IWEWLAZckZlWsmo...
   \ </ds:SignatureValue>
   
   <ds:KeyInfo Id="KI-32484d1e-867e-4465-a96f-52a8668d5a0c"\ >
   
   <wsse:SecurityTokenReference
   xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-w
   ssecurity-secext-1.0.xsd"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:Id="STR-3cf69cce-c56f-461a-905d-dfc20ab0742c"\ >
   
   <wsse:Reference URI="#X509-39011475-65d5-446e-ba38-be84220fd720"
   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x5
   09-token-profile-1.0#X509v3"\ />
   
   </wsse:SecurityTokenReference>
   
   </ds:KeyInfo>
   
   </ds:Signature>
   
   </wsse:Security>
   
   <Action
   xmlns="http://www.w3.org/2005/08/addressing"\ >\ http://profile.s
   ecurity.modi.agid.org/HelloWorld/sayHi\ </Action>
   
   <MessageID
   xmlns="http://www.w3.org/2005/08/addressing"\ >\ urn:uuid:55e6bc5
   7-2286-4b7d-82a9-fdbcf57721b1\ </MessageID>
   
   <To xmlns="http://www.w3.org/2005/08/addressing"
   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-ws
   security-utility-1.0.xsd"
   wsu:Id="id-96f9b013-17e5-489d-8068-52c3f1345c75"\ >\ https://api.
   amministrazioneesempio.it/soap/echo/v1\ </To>
   
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

-  algoritmi di firma (SignatureMethod)

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

.. image:: ./media/image1.png
  :width: 4.68056in
  :height: 2.40278in

.. mermaid::

     sequenceDiagram
       activate Fruitore
       activate Erogatore
       Fruitore->>+Erogatore: 1. Request()
       Erogatore-->>Fruitore: 2. Response
       deactivate Erogatore
       deactivate Fruitore

.. image:: ./media/image2.png

...   :width: 4.68056in
...   :height: 2.40278in
