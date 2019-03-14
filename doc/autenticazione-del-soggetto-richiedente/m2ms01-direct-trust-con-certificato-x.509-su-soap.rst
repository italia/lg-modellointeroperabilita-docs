3.1. [M2MS01] Direct Trust con certificato X.509 su SOAP
========================================================

.. _scenario-2:

3.1.1. Scenario
---------------

Comunicazione tra richiedente ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto richiedente, quale organizzazione o unità
   organizzativa richiedente, o entrambe le parti;

.. _descrizione-2:

3.1.2. Descrizione
------------------

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 [4].

Si assume l’esistenza di un trust tra richiedente (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il richiedente inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-2:

3.1.3. Dettaglio
----------------

|image0|

.. _flusso-delle-interazioni-2:

3.1.3.1. Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il richiedente invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

Al messaggio è aggiunta la firma di una porzione significativa dello
stesso.

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509 e valida la firma..

L’erogatore predispone il messaggio di risposta e lo inoltra al
richiedente.

.. _regole-di-processamento-2:

3.1.3.2. Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il richiedente costruisce un messaggio SOAP per il servizio.

2. Il richiedente calcola la firma per gli elementi significativi del
   messaggio usando l’XML Signature. Il digest è firmato usando la
   chiave privata associata al certificato X.509 del richiedente.
   L’elemento <Signature> è posizionato nell’header <Security> del
   messaggio.

3. Il richiedente referenzia il certificato X.509 usando in maniera
   alternativa, nell’header <Security>, i seguenti elementi previsti
   nella specifica ws-security:

   a. <wsse:BinarySecurityToken>

   b. <wsse:KeyIdentifier>

   c. <wsse:SecurityTokenReference>

4. Il richiedente spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

5. L’erogatore recupera il certificato X.509 referenziato nell’header
   <Security>.

6. L’erogatore verifica il certificato secondo i criteri del trust.

7. L’erogatore valida la firma verificando l’elemento <Signature>
   nell’header <Security>.

8. L’erogatore autentica il richiedente.

9. Se le azioni da 5 a 8 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   <Signature> rispettivamente <DigestMethod>,<SignatureMethod> e
   <CanonicalizationMethod> si fa riferimento alla sezione `Elenco degli
   algoritmi <#elenco-degli-algoritmi>`__ .

-  Un meccanismo simile può essere utilizzato per autenticare
   l’’erogatore.

3.1.3.3. Tracciato
~~~~~~~~~~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
richiedente all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

-  soap="http://schemas.xmlsoap.org/soap/envelope/"

-  wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"

-  wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

-  ds="http://www.w3.org/2000/09/xmldsig#"

-  ec="http://www.w3.org/2001/10/xml-exc-c14n#"

-  http://www.w3.org/2005/08/addressing

+-----------------------------------------------------------------------+
| | <soap:Envelope>                                                     |
| | <soap:Header>                                                       |
| | <wsse:Security soap:mustUnderstand="1">                             |
| | <wsse:BinarySecurityToken                                           |
|   EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-w |
| ss-soap-message-security-1.0#Base64Binary"                            |
|   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss- |
| x509-token-profile-1.0#X509v3"                                        |
| | wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIB |
| AgIECxY+9TAhkiG9w...                                                  |
| | </wsse:BinarySecurityToken>                                         |
| | <wsu:Timestamp wsu:Id="TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">    |
| | <wsu:Created>2018-10-04T10:17:28.061Z</wsu:Created>                 |
| | <wsu:Expires>2018-10-04T10:22:28.061Z</wsu:Expires>                 |
| | </wsu:Timestamp>                                                    |
| | <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">        |
| | <ds:SignedInfo>                                                     |
| | <ds:CanonicalizationMethod                                          |
|   Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">                |
| | <ec:InclusiveNamespaces PrefixList="soap" />                        |
| | </ds:CanonicalizationMethod>                                        |
| | <ds:SignatureMethod                                                 |
|                                                                       |
| | Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />    |
| | <ds:Reference URI="#TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">       |
| | <ds:Transforms>                                                     |
| | <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">  |
| | <ec:InclusiveNamespaces PrefixList="soap wsse" />                   |
| | </ds:Transform>                                                     |
| | </ds:Transforms>                                                    |
| | <ds:DigestMethod                                                    |
|   Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />              |
| | <ds:DigestValue>NWPKndUk42jwIJOpDGXACq7QbyBUg1UfJFSEylsCxQw=</ds:Di |
| gestValue>                                                            |
| | </ds:Reference>                                                     |
| | </ds:SignedInfo>                                                    |
| | <ds:SignatureValue>AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...</ds:Signa |
| tureValue>                                                            |
| | <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8">           |
| | <wsse:SecurityTokenReference                                        |
|   wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3">                  |
| | <wsse:Reference                                                     |
|                                                                       |
| | URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"                    |
|   ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss- |
| x509-token-profile-1.0#X509v3"/>                                      |
|   </wsse:SecurityTokenReference>                                      |
| | </ds:KeyInfo>                                                       |
| | </ds:Signature>                                                     |
| | </wsse:Security>                                                    |
| | </soap:Header>                                                      |
| | <soap:Body>                                                         |
| | <ns2:sayHi                                                          |
|   xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">      |
| | <arg0>Hello World!</arg0>                                           |
| | </ns2:sayHi>                                                        |
| | </soap:Body>                                                        |
| | </soap:Envelope>                                                    |
+-----------------------------------------------------------------------+

Il codice rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al security token (BinarySecurityToken)

-  algoritmi di canonizzazione (CanonicalizationMethod)

-  algoritmi di firma (SignatureMethod)

-  algoritmo per il digest (DigestMethod)

-  l’inclusione dell’elemento Timestamp quale porzione significativa del
   messaggio e la relativa firma.

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione `Elenco degli
algoritmi <#elenco-degli-algoritmi>`__, nonché la modalità di inclusione
o referenziazione del certificato x509.

.. |image0| image:: ./media/image9.png
   :width: 2.34375in
   :height: 1.28125in
