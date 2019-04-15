Accesso del soggetto fruitore
=============================

[IDAS01] Direct Trust con certificato X.509 su SOAP
---------------------------------------------------

.. _scenario-2:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitrice, o entrambe le parti;

.. _descrizione-2:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un `trust`_ tra fruitore ed erogatore,
che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_, inclusa la modalità
di scambio dei certificati X.509) non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-2:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _regole-di-processamento-2:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore aggiunge al messaggio l’header ``WS-Addressing`` e
   l’elemento ``<wsu:Timestamp>`` composto dagli elementi ``<wsu:Created>`` e
   ``<wsu:Expires>``

3. Il fruitore calcola la firma per gli elementi significativi del
   messaggio, in particolare ``<wsu:Timestamp>`` e ``<wsa:To>`` del blocco
   ``WS-Addressing``. Il digest è firmato usando la chiave privata associata
   al certificato X.509 del fruitore. L’elemento ``<Signature>`` è
   posizionato nell’header ``<Security>`` del messaggio.

4. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   a. ``<wsse:BinarySecurityToken>``

   b. ``<wsse:KeyIdentifier>``

   c. ``<wsse:SecurityTokenReference>``

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6. L’erogatore verifica il contenuto dell’elemento ``<wsu:Timestamp>``
   nell’header del messaggio al fine di verificare la validità
   temporale del messaggio.

7. L’erogatore verifica la corrispondenza tra se stesso e quanto
   definito nell’elemento ``<wsa:To>`` del blocco WS-Addressing.

8.  L’erogatore recupera il certificato X.509 referenziato nell’header
    ``<Security>``.

9.  L’erogatore verifica il certificato secondo i criteri del trust.

10. L’erogatore valida l’elemento <Signature> nell’header ``<Security>``.

11. L’erogatore autentica il fruitore.

12. Se le azioni da 6 a 11 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   ``<Signature>`` rispettivamente ``<DigestMethod>``, ``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` si fa riferimento agli algoritmi indicati
   alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__,

-  Un meccanismo simile può essere utilizzato specularmente per l’erogatore.

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatoe relativo ad un
servizio di ``echo``.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://www.w3.org/2003/05/soap-envelope"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
		<soap:Header>
			<wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"  soap:mustUnderstand="1">
				<wsse:BinarySecurityToken EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" 
				wsu:Id="X509-39011475-65d5-446e-ba38-be84220fd720">MIICqDCCAZCgAwIBAgIEXLSSUTANBgkqhkiG9w0BAQsFADAW...</wsse:BinarySecurityToken>
				<wsu:Timestamp wsu:Id="TS-819df7b7-379d-48f7-8d9c-28c5b5d252f0">
					<wsu:Created>2019-04-15T14:53:34.649Z</wsu:Created>
					<wsu:Expires>2019-04-15T14:58:34.649Z</wsu:Expires>
				</wsu:Timestamp>
				<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="SIG-6e09e972-cbe6-43fc-a10c-38e6dce56dbe">
					<ds:SignedInfo>
						<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
							<ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap"/>
						</ds:CanonicalizationMethod>
						<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
						<ds:Reference URI="#TS-819df7b7-379d-48f7-8d9c-28c5b5d252f0">
							<ds:Transforms>
								<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
									<ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap wsse"/>
								</ds:Transform>
							</ds:Transforms>
							<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
							<ds:DigestValue>K/3Fq1fYjG5PXv8UlKBuT4XBCWudGR5w2M10wPcZ/Yo=</ds:DigestValue>
						</ds:Reference>
						<ds:Reference URI="#id-96f9b013-17e5-489d-8068-52c3f1345c75">
							<ds:Transforms>
								<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
									<ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap"/>
								</ds:Transform>
							</ds:Transforms>
							<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
							<ds:DigestValue>eH3Vlc3l19NbBawDOuFDN11BfmbgGAnl6Z4LpJVM3UM=</ds:DigestValue>
						</ds:Reference>
					</ds:SignedInfo>
					<ds:SignatureValue>jAtZqkfRcFJW+jx9YDv+r2Q8V4IWEWLAZckZlWsmo...</ds:SignatureValue>
					<ds:KeyInfo Id="KI-32484d1e-867e-4465-a96f-52a8668d5a0c">
						<wsse:SecurityTokenReference xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="STR-3cf69cce-c56f-461a-905d-dfc20ab0742c">
							<wsse:Reference URI="#X509-39011475-65d5-446e-ba38-be84220fd720" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>
						</wsse:SecurityTokenReference>
					</ds:KeyInfo>
				</ds:Signature>
			</wsse:Security>
			<Action xmlns="http://www.w3.org/2005/08/addressing">http://profile.security.modi.agid.org/HelloWorld/sayHi</Action>
			<MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:55e6bc57-2286-4b7d-82a9-fdbcf57721b1</MessageID>
			<To xmlns="http://www.w3.org/2005/08/addressing" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="id-96f9b013-17e5-489d-8068-52c3f1345c75">https://api.amministrazioneesempio.it/soap/echo/v1</To>
			<ReplyTo xmlns="http://www.w3.org/2005/08/addressing">
				<Address>http://www.w3.org/2005/08/addressing/anonymous</Address>
			</ReplyTo>
		</soap:Header>
		<soap:Body>
			<ns2:sayHi xmlns:ns2="http://profile.security.modi.agid.org/">
				<arg0>OK !!!!</arg0>
			</ns2:sayHi>
		</soap:Body>
		</soap:Envelope>

Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``).

-  algoritmo per il digest (``DigestMethod``)

Le parti, in base alle proprie esigenze, usano
gli algoritmi indicati in   `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__
, nonché la modalità di inclusione o referenziazione del certificato X.509.

[IDA02] Direct Trust con certificato X.509 su SOAP con con unicità del token/messaggio
---------------------------------------------------------------------------------------

.. _scenario-3:

Scenario
^^^^^^^^

Il seguente profilo estende il profilo M2MS01.

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack 

.. _descrizione-3:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un `trust`_ tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_, inclusa la modalità
di scambio dei certificati X.509, non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509,
valida la firma dei claim ed autentica il fruitore. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-3:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _regole-di-processamento-3:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore aggiunge al messaggio l’header ``WS-Addressing`` e
   l’elemento ``<wsu:Timestamp>`` composto dagli elementi ``<wsu:Created>`` e
   ``<wsu:Expires>``

3. Il fruitore calcola la firma per gli elementi significativi del
   messaggio, in particolare ``<wsu:Timestamp>`` e ``<wsa:To>`` del blocco
   ``WS-Addressing``. Il digest è firmato usando la chiave privata associata
   al certificato X.509 del fruitore. L’elemento ``<Signature>`` è
   posizionato nell’header ``<Security>`` del messaggio.

4. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   a. ``<wsse:BinarySecurityToken>``

   b. ``<wsse:KeyIdentifier>``

   c. ``<wsse:SecurityTokenReference>``

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6. L’erogatore verifica il contenuto dell’elemento ``<wsu:Timestamp>``
   nell’header del messaggio al fine di verificare la validità
   temporale del messaggio anche per mitigare il rischio di replay attack.

7. L’erogatore verifica la corrispondenza tra se stesso e quanto definito
   nell’elemento ``<wsa:To>`` del blocco WS-Addressing.

8.  L’erogatore recupera il certificato X.509 referenziato nell’header ``<Security>``.

9.  L’erogatore verifica il certificato secondo i criteri del trust.

10.  L’erogatore valida l’elemento ``<Signature>`` nell’header ``<Security>``.

11.  L’erogatore autentica il fruitore.

12. Se le azioni da 6 a 11 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   ``<Signature>`` rispettivamente ``<DigestMethod>``, ``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` si fa riferimento agli algoritmi indicati
   alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__,

-  Un meccanismo simile può essere utilizzato per autenticare
   l’erogatore.

.. _tracciato-3:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore relativo ad un
servizio di ``echo``.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

   <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" soap:mustUnderstand="1">
      <wsse:BinarySecurityToken EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" wsu:Id="X509-bf881daf-371a-4d18-9502-d9f92af9a949">MIICqDCCAZCgAwIBAgIEXLSSUTANBgkqhkiG9w0BAQsFADAWMRQwEgYDVQQDDAttb2RpU2VjUHJvZjAeFw0xOTA0MTUxNDE2NDlaFw0yNDA0MTUxNDE2NDlaMBYxFDASBgNVBAMMC21vZGlTZWNQcm9mMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvBJNKBiLS+ZcmwGUku5l2FKeHogeSZejjOOrO2Ag6DGPXo1MtHt2XwgUXmgT+v0IjhZp5XH2XbwSWw2EMWSG3Zz0CJILqWGPg0M/LxaIZAxSdxJpVNWg/profO+xKz0B6QHK+I0yecHg7TtI4es9AuDyR4pKslpcXyMEqJQ7m5N8v2e4WldeHF2SRN/ereEOuewEi15c7akh4TdkGdiwOSif2AXIugHRgdpHjH86iJxFu24IJmBA7C5tytz7mfKollGhI9+2d0902ayVshCV4/pmnX0pDiGayV1C6SDPTbapXKXJrp1+fBHaUkDY+W/2Q9sC4o8pttmcpHeMRxFDkwIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQALwKbIm8S2BpYpHaqMwJLeWBPCaDeT7J+KDj39Ac3YxDb8E/hGM+Hn1mq2ssYqu5JTvuAQ9o8v3UpcIct15RPgOKYfBzxnH1h2vCavpiFCFTc6UoQgPBZGyyNOOKNOxEnXtW7ff1gl2GRLIWXlXDf1fdX7VJVBqWfBvivhIbsDa5LRBCrNsXORx2azUb5QBgMm2UZJxYA3+dFRgYmLSY/RyRLf0o03lwCRhAyrU7ya9IMYgrxgjEos2fHB2IGJJ1Wh+gTQWMP+wJymlC0qyjTHx5pyZOzJGtH5HnaVU7EgtxdBRC9dTlWVpNgmD8nS6Yr/am5cZJZrkIHRyfxqkA2W</wsse:BinarySecurityToken>
      <wsu:Timestamp wsu:Id="TS-09f1357c-beb4-4804-9410-76c5a06e2e48">
        <wsu:Created>2019-04-15T15:02:15.515Z</wsu:Created>
        <wsu:Expires>2019-04-15T15:07:15.515Z</wsu:Expires>
      </wsu:Timestamp>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="SIG-4d949c5b-968b-4fd5-be67-4cd1d1a41ce3">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
            <ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap"/>
          </ds:CanonicalizationMethod>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
          <ds:Reference URI="#TS-09f1357c-beb4-4804-9410-76c5a06e2e48">
            <ds:Transforms>
              <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                <ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap wsse"/>
              </ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>HPYjNXdxIuJIWk1EArE+8PIgyWt5nAD+upwcjOSDB20=</ds:DigestValue>
          </ds:Reference>
          <ds:Reference URI="#id-27c23bc8-0c4f-4d98-b046-6e590ea9661b">
            <ds:Transforms>
              <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                <ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap"/>
              </ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>MJzRD4ZRMsFOxskbnfNV9BnDTCLxuLSnmZ8I4IjaxHw=</ds:DigestValue>
          </ds:Reference>
          <ds:Reference URI="#id-fb4c1fa0-e804-4169-b70e-5b55c5f9d912">
            <ds:Transforms>
              <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                <ec:InclusiveNamespaces xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="soap"/>
              </ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>MIi+ovLTqYu1HqxUtmUnuhVdMmNKOpOX8vn/fKjvQFU=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>SBYs6aikHbfsHHV04ifV/ljVTysxNLRTPU6gsOGJamWGYLMPqOETjBf+NFJhPDVdolQSSHw0SD7uA/RlYkE9amRH1K+hoaUIa/PEhPgC1io/LqZdi3rt+b8uRlk+CXcUKOObgf/N960F/sM6s0ArKQxg/Yx6pqWamXBXo0PH/1FvHSgwdA62s0+Sli96qY0EnJPoyKIrqzskiscLXI1jCe8sesyA+xtJ0qBdFKAn2af48sVStPFv4gizC8+bsCRpQ36ihUIlI8DInJ13EgoKV9/rC4PheExO7HvSNTpBFdQt+Wr9wAb3oHq4urRBdugA6mX2xaJ8/XyZVajivvuVTw==</ds:SignatureValue>
        <ds:KeyInfo Id="KI-dab2ce54-b000-439a-bcc2-9b8249626a1c">
          <wsse:SecurityTokenReference xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="STR-068909fe-1a64-4cf1-bd5a-355a20b0495f">
            <wsse:Reference URI="#X509-bf881daf-371a-4d18-9502-d9f92af9a949" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>
          </wsse:SecurityTokenReference>
        </ds:KeyInfo>
      </ds:Signature>
    </wsse:Security>
    <Action xmlns="http://www.w3.org/2005/08/addressing">http://profile.security.modi.agid.org/HelloWorld/sayHi</Action>
    <MessageID xmlns="http://www.w3.org/2005/08/addressing" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="id-fb4c1fa0-e804-4169-b70e-5b55c5f9d912">urn:uuid:46da4ec1-f962-4f24-8524-48bb74b505d7</MessageID>
    <To xmlns="http://www.w3.org/2005/08/addressing" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="id-27c23bc8-0c4f-4d98-b046-6e590ea9661b">http://localhost:8080/security-profile/echo</To>
    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">
      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>
    </ReplyTo>
  </soap:Header>
  <soap:Body>
    <ns2:sayHi xmlns:ns2="http://profile.security.modi.agid.org/">
      <arg0>OK !!!!</arg0>
    </ns2:sayHi>
  </soap:Body>
</soap:Envelope>


Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``).

-  algoritmo per il digest (``DigestMethod``)

Le parti, in base alle proprie esigenze, usano
gli algoritmi indicati in   `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__
, nonché la modalità di inclusione o referenziazione del certificato X.509.

[M2MR01] Direct Trust con certificato X.509 su REST
---------------------------------------------------

.. _scenario-4:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

.. _descrizione-4:

Descrizione
^^^^^^^^^^^

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’ :RFC:`7519`

-  JSON Web Signature (JWS) definita dall’ :RFC:`7515`

Si assume l’esistenza di un `trust`_ tra fruitore ed erogatore,
che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_, inclusa la modalità
di scambio dei certificati X.509, non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’erogatore
includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio, inclusa la corrispondenza
del destinatario e l'intervallo di validità della firma.

Se la verifica e la validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-4:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-4:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore genera un JWT signed contenente i riferimenti temporali
ed il destinatario del messaggio.

Il fruitore invia il messaggio di richiesta all’erogatore.

Il JWT include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

**B: Risposta**

L’erogatore, ricevuto il messaggio, verifica il
certificato X.509 e valida la firma del JWT e il contenuto dei claim standard.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-4:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore predispone la payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il JWT popolando:

   a. il `Jose Header`_  con almeno i ``parameter``:

      -   `alg`_ con l’algoritmo di firma
      -  `typ`_ uguale a ``JWT``

      - una o più delle seguenti opzioni per referenziare il certificato X.509:

           * `x5u`_ (X.509 URL)
           * `x5c`_ (X.509 Certificate Chain)
           * `x5t#256`_ (X.509 Certificate SHA-256 Thumbprint)

   b. la payload del JWT coi claim rappresentativi degli
      elementi chiave del messaggio, contenente almeno:

      * i riferimenti temporali di emissione e scadenza: `iat`_ , `exp`_.
        Se il flusso richiede di verificare l'istante di prima validità del token, si può
        usare il claim `nbf`_.

      * il riferimento dell'erogatore in `aud`_

3. il fruitore firma il token adottando la `JWS Compact Serialization`_

4. il fruitore posiziona il ``JWT`` signed nell’ :httpheader:`Authorization`

5. Il fruitore spedisce il messaggio all'erogatore

**B: Risposta**

6.  L’erogatore decodifica il  ``JWT`` presente in :httpheader:`Authorization` e valida
    i claim contenuti nel `Jose Header`_, in particolare verifica:

    - il contenuto dei claim `iat`_ ed `exp`_;
    - la corrispondenza tra se stesso e il claim `aud`_;

7.  L’erogatore recupera il certificato X.509 referenziato nel `Jose Header`_

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del ``JWT``

10. L’erogatore autentica il fruitore

11. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato

Note:

-  Gli algoritmi da utilizzare in `alg`_ sono indicati in  `Elenco degli algoritmi`_

-  Un meccanismo simile può essere utilizzato per autenticare l’erogatore.

.. _tracciato-2:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’erogatore.

Esempio porzione messaggio HTTP

.. code-block:: http

   GET http://api.erogatore.org/ws-test/service/hello/echo/Ciao  HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

   .
   .
   .


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
   # payload
   {
    "iat": 1554382877,
    "nbf": 1554382877,
    "exp": 1554382879,
    "aud": "https://api.erogatore.org/ws-test/service/hello/echo"
   }

Gli elementi presenti nel tracciato rispettano le seguenti scelte implementative e includono:


-  l'intervallo temporale di validità, in modo che il JWT
   possa essere usato solo tra gli istanti `nbf`_ ed `exp`_;

-  indica l'istante `iat`_ di emissione del JWT. Se le parti possono accordarsi nel considerarlo
   come l'istante iniziale di validità del token, :rfc:`7519` non assegna a questo claim
   nessun ruolo specifico nella validazione, a differenza di `nbf`_;

-  il destinatario del JWT, che deve sempre essere validato;

-  contenuto della certificate chain X.509 (`x5c`_)

-  algoritmi di firma e digest (`alg`_).

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi`_
nonché la modalità di inclusione o referenziazione del certificato X.509.

[M2MR02] Direct Trust con certificato X.509 su REST con unicità del token/messaggio
-----------------------------------------------------------------------------------

.. _scenario-5:

Scenario
^^^^^^^^

Il seguente profilo estende il profilo M2MR01.

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti

-  la difesa dalle minacce derivanti dagli attacchi: Replay Attack
   quando il JWT o il messaggio non devono essere riprocessati

.. _descrizione-5:

Descrizione
^^^^^^^^^^^

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’:RFC:`7519`

-  JSON Web Signature (JWS) definita dall’:RFC:`7515`

Si assume l’esistenza di un `trust`_ tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il `trust`_, inclusa la modalità
di scambio dei certificati X.509) non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio, inclusa la corrispondenza
del destinatario e l'intervallo di validità della firma.

L'erogatore verifica inoltre l'univocità dell'identificativo ricevuto
nel JWT.

Se la verifica e la validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-5:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-5:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore genera un JWS contenente almeno:

  - i riferimenti temporali ed il destinatario del messaggio;
  - un identificativo univoco del token o del messaggio.

Il JWT include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

Il fruitore invia il messaggio di richiesta all’erogatore.

**B: Risposta**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma del JWT e le claim ricevute.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-5:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore predispone la payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il JWT popolando:

   a. il `Jose Header`_  con almeno i ``parameter``:

      -  `alg`_ con l’algoritmo di firma
      -  `typ`_ uguale a ``JWT``

      - una o più delle seguenti opzioni per referenziare il certificato X.509:

           * `x5u`_ (X.509 URL)
           * `x5c`_ (X.509 Certificate Chain)
           * `x5t#256`_ (X.509 Certificate SHA-256 Thumbprint)

   b. la payload del JWT coi claim rappresentativi degli
      elementi chiave del messaggio, contenente almeno:

      * i riferimenti temporali di emissione e scadenza: `iat`_ , `exp`_.
        Se il flusso richiede di verificare l'istante di prima validità del token, si può
        usare il claim `nbf`_.
      * il riferimento dell'erogatore in `aud`_;
      * un identificativo univoco del token `jti`_. Se utile alla logica applicativa
        l'identificativo può essere anche collegato al messaggio.

3. il fruitore firma il token adottando la `JWS Compact Serialization`_

4. il fruitore posiziona il ``JWS`` nell’ :httpheader:`Authorization`

5. Il fruitore spedisce il messaggio all'erogatore

**B: Risposta**

6.  L’erogatore decodifica il  ``JWT`` presente in :httpheader:`Authorization` e valida
    i claim contenuti nel `Jose Header`_, in particolare verifica:

    - il contenuto dei claim `iat`_ ed `exp`_;
    - la corrispondenza tra se stesso e il claim `aud`_;
    - l'univocità del claim `jti`_

7.  L’erogatore recupera il certificato X.509 referenziato nel `Jose Header`_

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del ``JWT``

10. L’erogatore autentica il fruitore

11. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato

Note:

-  Per quanto riguarda gli algoritmi da utilizzare si fa
   riferimento ad  `Elenco degli algoritmi`_.

-  Un meccanismo simile può essere utilizzato per autenticare
   l’erogatore.

.. _tracciato-5:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

.. code-block:: http

   GET http://localhost:8080/ws-test/service/hello/echo/Ciao  HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

   .
   .

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
   # payload
   {
     "aud": "http://localhost:8080/ws-test/service/hello/echo"
     "iat": 1516239022,
     "nbf": 1516239022,
     "exp": 1516239024,
     "jti": "065259e8-8696-44d1-84c5-d3ce04c2f40d"
   }


Gli elementi presenti nel tracciato rispettano le seguenti scelte implementative e includono:


-  l'intervallo temporale di validità, in modo che il JWT
   possa essere usato solo tra gli istanti `nbf`_ ed `exp`_;

-  indica l'istante `iat`_ di emissione del JWT. Se le parti possono accordarsi nel considerarlo
   come l'istante iniziale di validità del token, :rfc:`7519` non assegna a questo claim
   nessun ruolo specifico nella validazione, a differenza di `nbf`_;

-  il destinatario del JWT, che deve sempre essere validato;

-  contenuto della certificate chain X.509 (`x5c`_)

-  algoritmi di firma e digest (`alg`_).

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi`_
nonché la modalità di inclusione o referenziazione del certificato X.509.



.. _`Elenco degli algoritmi`: elenco-degli-algoritmi.html

.. _`trust`: ../doc_04_cap_00.html

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


.. discourse::
   :topic_identifier: 8907
