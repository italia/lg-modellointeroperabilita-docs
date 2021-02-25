[INTEGRITY_SOAP_01] Integrità del payload del messaggio SOAP
==============================================================


Il presente profilo estende ID_AUTH_SOAP_01 o ID_AUTH_SOAP_02,
aggiungendo alla comunicazione tra fruitore ed erogatore a livello di
messaggio:

-  integrità del payload del messaggio.

Descrizione
------------

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
la validazione sono superate, l’erogatore elabora la richiesta e produce
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
   <CanonicalizationMethod> si fa riferimento agli algoritmi indicati 
   nelle Linee Guida sulla sicurezza, emanate dall'Agenzia per l'Italia Digitale 
   ai sensi dell'articolo 71 del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   del payload del messaggio risposta dell’erogatore al fruitore.

Esempio
-------

Di seguito è riportato un tracciato del messaggio inoltrato dal fruitore
all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"

.. literalinclude:: media/INTEGRITY_SOAP_01_example_request.xml
   :language: xm

Il codice rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al security token (BinarySecurityToken)

-  algoritmi di canonizzazione (CanonicalizationMethod)

-  algoritmi di firma (SignatureMethod)

-  algoritmo per il digest (DigestMethod)

Le parti, in base alle proprie esigenze, individuano gli specifici algoritmi
secondo quanto indicato nelle Linee Guida sulla sicurezza,
emanate dall'Agenzia per l'Italia Digitale ai sensi dell'articolo 71
del decreto legislativo 7 marzo 2005, n. 82 (Codice dell'Amministrazione Digitale).

.. forum_italia::
   :topic_id: 21474
   :scope: document
