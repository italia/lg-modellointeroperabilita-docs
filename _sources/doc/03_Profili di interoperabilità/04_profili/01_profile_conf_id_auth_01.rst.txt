[PROFILE_CONF_ID_AUTH_01] Profilo per confidenzialità ed autenticazione del fruitore
-------------------------------------------------------------------------------------

Dare seguito ad uno scambio tra fruitore ed erogatore che garantisca:

-  la confidenzialità a livello di canale

-  l’autenticazione del fruitore

Il fruitore potrebbe non coincidere con l’unità organizzativa fruitore,
ma comunque appartenere alla stessa.

Questo profilo è indipendente dal pattern di interazione implementato ed
utilizza i seguenti pattern di sicurezza:

-  ID_AUTH_CHANNEL_01

-  ID_AUTH_SOAP_01 o ID_AUTH_REST_01

Si assume l’esistenza di un trust tra fruitore ed erogatore che
stabilisce:

-  riconoscimento da parte dell’erogatore dei certificati X.509, o la CA
   emittente, relative al fruitore

-  riconoscimento da parte del fruitore del certificato X.509, o la CA
   emittente, relative al soggetto erogatore

Il meccanismo con cui è stabilito il trust non condiziona quanto
descritto di seguito.

Flusso delle interazioni
^^^^^^^^^^^^^^^^^^^^^^^^^

**A: Richiesta**

Il messaggio di richiesta viene predisposto utilizzando il pattern
[ID_AUTH_SOAP_01] nel caso di utilizzo di SOAP o [ID_AUTH_REST_01] nel
caso di utilizzo di REST, per garantire:

-  l’identità del fruitore.

Il fruitore invia il messaggio di richiesta all’interfaccia di servizio
dell’erogatore.

Il messaggio viene trasmesso su un canale sicuro utilizzando il profilo
ID_AUTH_CHANNEL_01 per garantire:

-  la confidenzialità a livello di canale.

**B: Risposta**

L’erogatore da seguito a quanto previsto nel pattern ID_AUTH_SOAP_01 nel
caso di utilizzo di SOAP o ID_AUTH_REST_01 nel caso di utilizzo di REST.

.. forum_italia::
   :topic_id: 21481
   :scope: document
