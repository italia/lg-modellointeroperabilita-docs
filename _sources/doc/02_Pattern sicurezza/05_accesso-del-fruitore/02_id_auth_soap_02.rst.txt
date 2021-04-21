[ID_AUTH_SOAP_02] Direct Trust con certificato X.509 su SOAP con con unicità del token/messaggio
=================================================================================================

Il seguente profilo estende il profilo ID_AUTH_SOAP_01. Comunicazione
tra fruitore ed erogatore che assicuri a livello di messaggio:

-  accesso del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack.

Descrizione
-----------

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
verifica e la validazione sono superate, l’erogatore elabora la
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
   <CanonicalizationMethod> si fa riferimento agli algoritmi indicati 
   nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
   ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

-  Un meccanismo simile può essere utilizzato specularmente per
   l’erogatore.

Esempio
--------

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore relativo ad un servizio di
echo.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"

.. literalinclude:: media/ID_AUTH_SOAP_02_example_request.xml
   :language: xml

Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al security token (BinarySecurityToken)

-  algoritmi di canonizzazione (CanonicalizationMethod)

-  algoritmi di firma (SignatureMethod).

-  algoritmo per il digest (DigestMethod)

Le parti, in base alle proprie esigenze, individuano gli specifici algoritmi 
secondo quanto indicato nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

.. forum_italia::
   :topic_id: 21470
   :scope: document
