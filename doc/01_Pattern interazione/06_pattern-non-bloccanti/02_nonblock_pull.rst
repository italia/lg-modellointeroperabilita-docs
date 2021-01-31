Pattern non bloccanti RPC PULL (busy waiting)
=============================================

Questo pattern è simile al precedente, di cui eredita le motivazioni, ma
in questo caso:

- l’erogatore fornisce un URL dove verificare lo stato
  di processamento di una richiesta;
- il fruitore non fornisce un indirizzo di callback.

Questo scenario prevede due possibili workflow, uno per REST ed uno per
SOAP riportati nelle seguenti figure.

.. mermaid::

   sequenceDiagram
    participant E as Erogatore
    participant F as Fruitore
    activate E
    activate F

    F->>E: 1. Request()
    E-->>F: 2. Status URL (Location)

    loop status pending
		F->>E: 3. Check status URL

        alt pending
		 E-->>F: 4a. Status pending
        else Ready
		 E-->>F: 4b. Result URL (Location)
        end
    end

    F->>E: 5. Retrieve Result URL
    E-->>F: 6. Result

    deactivate F
    deactivate E

*Figura 3 - Interazione non bloccante tramite busy waiting REST*

Il fruitore invia una richiesta (passo 1.) e riceve immediatamente un
acknowledge (passo 2.) insieme ad:

-  un URL dove verificare lo stato del processamento (REST);
-  oppure un CorrelationID (SOAP).

D’ora in poi il fruitore, periodicamente, verifica (passo 3.) lo stato
dell'operazione utilizzando:

-  l’URL indicato (REST)
-  oppure il CorrelationID (SOAP)

fin quando il risultato dell'operazione sarà pronto (passo 4b.).

Gli intervalli di polling possono essere definiti tra le parti.

Quando la risposta è pronta il fruitore può accedere (passi 5. e 6.)
al risultato del processamento

.. mermaid::

   sequenceDiagram
     
     activate Erogatore
     activate Fruitore
     Fruitore->>Erogatore: 1. Request()
     Erogatore-->>Fruitore: 2. CorrelationID
     loop status pending
		 Fruitore->>Erogatore: 3. CheckStatus(CorrelationID)
		 Erogatore-->>Fruitore: 4. CurrentStatus
     end
     Fruitore->>Erogatore: 5. RetrieveResult(CorrelationID)
     Erogatore-->>Fruitore: 6. Result
     deactivate Fruitore
     deactivate Erogatore

*Figura 4 - Interazione non bloccante tramite busy waiting SOAP*

[NONBLOCK_PULL_REST] Not Blocking Pull REST
-------------------------------------------

Quando il profilo viene implementato con tecnologia REST,
DEVONO essere rispettate le seguenti regole:

-  La specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   codici di stato HTTP restituiti con relativo schema della risposta,
   oltre che ad eventuali header HTTP restituiti;

-  La specifica dell’interfaccia DEVE dichiarare gli schemi delle
   richieste insieme ad eventuali header HTTP richiesti;

-  Al passo (1), il fruitore DEVE utilizzare il verbo HTTP POST;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta, un URL per interrogare lo stato di
   processamento utilizzando :httpheader:`Location`, il codice HTTP di
   stato DEVE essere :httpstatus:`202` a meno che non si
   verifichino errori;

-  Al passo (3), il fruitore DEVE utilizzare il percorso di cui al passo
   (2) per richiedere lo stato della risorsa; il verbo HTTP utilizzato
   deve essere GET;

-  Al passo (4) l’erogatore indica, sulla base dello stato del
   processamento, che l'operazione:
   * 4a. non è completata (:httpstatus:`200`)
   * 4b. che la risorsa finale è pronta (:httpstatus:`303`) all’URL indicato nell’ :httpheader:`Location`;

-  Al passo (5), il fruitore DEVE recuperare la risorsa con una richiesta :httpmethod:`GET`
   all'URL indicato in (4b.);

-  Al passo (6) l’erogatore risponde con la rappresentazione della
   risorsa, il codice HTTP restituito è :httpstatus:`200`.


Regole di processamento
------------------------------------------------------------

Al termine del processamento delle richieste, l’erogatore deve fare uso
dei codici di stato HTTP rispettando la semantica. In particolare, al
ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica e semantica dei dati in
   ingresso

-  DEVE, in caso di dati errati, restituire :httpstatus:`400`
   fornendo nel body di risposta dettagli circa l’errore;

-  DOVREBBE, in caso di representation semanticamente non corretta,
   ritornare :httpstatus:`422`;

-  DEVE, se qualcuno degli ID nel path o nel body non esiste, restituire
   :httpstatus:`404`, indicando nel body di risposta quale degli
   ID è mancante;

-  PUÒ, se ipotizza che la richiesta sia malevola, ritornare HTTP status
   400 Bad Request o :httpstatus:`404`;

-  DEVE, in caso di errori non dipendenti dalla richiesta, restituire
   HTTP status 5xx rispettando la semantica degli stessi;

-  DEVE, ricevuta la richiesta, restituire :httpstatus:`202`.

-  In caso di ricezione corretta della risposta, il fruitore DEVE
   restituire :httpstatus:`200`, riempiendo il body di risposta con il
   risultato dell’operazione.

-  In caso di errore al momento di ricezione della risposta da parte del
   fruitore, è possibile definire meccanismi specifici per la
   ritrasmissione della risposta o della richiesta.

NB: I messaggi di errore devono essere utili al client ma NON DEVONO
rivelare dettagli tecnici e/o informazioni riservate.

.. _esempio-4:

Esempio
~~~~~~~

Specifica Servizio Server

https://api.ente.example/rest/nome-api/v1/openapi.yaml

.. literalinclude:: file-d0f6ac6f34fbe9304da62adbeaeb90f398f5ce55818391790b6141dea87bd75a.yaml
   :language: yaml

Il fruitore richiede la risorsa **M**,
e l’erogatore risponde dichiarando di aver preso in carico la richiesta.

Endpoint https://api.ente.example/rest/nome-api/v1/resources/1234/M

1. Request:

.. code-block:: http

   POST /rest/nome-api/v1/resources/1234/M HTTP/1.1
   Host: api.ente.example
   Content-Type: application/json

   {
     "a": {
        "a1": [1, "…", 2],
        "a2": "Stringa di esempio"
     },
     "b": "Stringa di esempio"
   }


2. Response

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 202 Accepted
   Content-Type: application/json
   Location: /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d
   
   {
     "status": "accepted",
     "message": "Preso carico della richiesta",
     "id": "8131edc0-29ed-4d6e-ba43-cce978c7ea8d"
   }

Quindi il fruitore verifica lo stato dell’esecuzione di **M** (3).
L’erogatore ritorna un payload diverso a seconda dei casi:
- processamento ancora in atto (4a)
- e di processamento avvenuto (4b).

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d

3. Request

.. code-block:: http

   GET /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d HTTP/1.1
   Host: api.ente.example


4a. Response (:httpstatus:`200`)

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 200 OK
   Host: api.ente.example
   Content-Type: application/json

   {
     "status": "processing",
     "message": "Richiesta in fase di processamento"
   }

4b. Response (:httpstatus:`303`)

.. code-block:: http
   :emphasize-lines: 1

   HTTP/1.1 303 See Other
   Content-Type: application/json
   Location: /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result
   
   {
     "status": "done",
     "message": "Processamento completo"
   }

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

Endpoint

https://api.ente.example/rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result

5. Request:

.. code-block:: http

   GET /rest/nome-api/v1/resources/1234/M/8131edc0-29ed-4d6e-ba43-cce978c7ea8d/result HTTP/1.1
   Host: api.ente.example


6. Response:

.. code-block:: http

   HTTP/1.1 200 OK
   Host: api.ente.example
   Content-Type: application/json

   {"c": "OK"}


[NONBLOCK_PULL_SOAP] Not Blocking Pull SOAP
-------------------------------------------

Nel caso in cui il profilo venga implementato con tecnologia SOAP,
DEVONO essere rispettate le seguenti regole:

-  L’interfaccia di servizio dell’erogatore fornisce tre metodi
   differenti al fine di inoltrare una richiesta, controllare lo stato
   ed ottenerne il risultato;

-  La specifica dell’interfaccia dell’erogatore DEVE indicare l’header
   SOAP :code:`X-Correlation-ID`;

-  Al passo (2), l’erogatore DEVE fornire insieme all’acknowledgement
   della richiesta nel body, un CorrelationID riportato nel header
   custom SOAP :code:`X-Correlation-ID`;

-  Al passo (3), il fruitore DEVE utilizzare il CorrelationID ottenuto
   al passo (2) per richiedere lo stato di processamento di una
   specifica richiesta;

-  Al passo (4) l’erogatore, quando il processamento non si è ancora
   concluso fornisce informazioni circa lo stato della lavorazione della
   richiesta, quando invece il processamento si è concluso risponde
   indicando in maniera esplicita il completamento;

-  Al passo (5), il fruitore utilizza il CorrelationID di cui al passo
   (2) al fine di richiedere il risultato della richiesta;

-  Al passo (6), l’erogatore fornisce il risultato del processamento.

Regole di processamento
------------------------------------------------------------

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire :httpstatus:`500`
   fornendo dettagli circa l’errore utilizzando il meccanismo della SOAP
   fault;

-  Se l’erogatore ipotizza che la richiesta sia malevola PUÒ ritornare
   :httpstatus:`400` o :httpstatus:`404`;

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice :httpstatus:`500` indicando il motivo dell’errore nella SOAP
   fault;

-  In caso di successo restituire :httpstatus:`200`, riempiendo il body
   di risposta con il risultato dell’operazione.

Esempio
------------------------------------------------------------

Specifica Servizio Server

https://api.ente.example/soap/nome-api/v1?wsdl

.. literalinclude:: file-74d9e6cd7ef59e44c9956803ae35d556311b1872778a13ff214cce1062b8873f.xml
   :language: xml

Di seguito un esempio di chiamata ad **M** in cui l’erogatore risponde
di avere preso in carico la richiesta.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method MRequest

1. Request Body

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Body>
		<m:MRequest>
		  <M>
			<o_id>1234</o_id>
			<a>
			  <a1s>1</a1s>
			  <a2>prova</a2>
			</a>
			<b>prova</b>
		  </M>
		</m:MRequest>
	  </soap:Body>
	</soap:Envelope>


2. Response Body (HTTP status code 200 OK)

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Header>
		<m:X-Correlation-ID>
	c8e191a8-f34f-41ed-82ea-68e096466707
	</m:X-Correlation-ID>
	  </soap:Header>
	  <soap:Body>
		<m:MRequestResponse>
		  <return>
			<status> accepted </status>
			<message> Preso carico della richiesta </message>
		  </return>
		</m:MRequestResponse>
	  </soap:Body>
	</soap:Envelope>


Di seguito un esempio di chiamata con cui il fruitore verifica
l’esecuzione di M nei casi di processamento ancora in atto e di
processamento avvenuto (4).

Endpoint

https://api.ente.example/soap/nome-api/v1

Method MProcessingStatus

3. Request Body status

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Header>
		<m:X-Correlation-ID>c8e191a8-f34f-41ed-82ea-68e096466707</m:X-Correlation-ID>
	  </soap:Header>
	  <soap:Body>
		<m:MProcessingStatus/>
	  </soap:Body>
	</soap:Envelope>

4. Response Body (HTTP status code 200 OK) status in attesa

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Body>
		<m:MProcessingStatusResponse>
		  <return>
			<status>processing</status>
			<message>Richiesta in fase di processamento</message>
		  </return>
		</m:MProcessingStatusResponse>
	  </soap:Body>
	</soap:Envelope>


4. Response Body (HTTP status code 200 OK) status completata

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Body>
		<m:MProcessingStatusResponse>
		  <return>
			<status>done</status>
			<message> Richiesta completata </message>
		  </return>
		</m:MProcessingStatusResponse>
	  </soap:Body>
	</soap:Envelope>

Di seguito un esempio di chiamata con cui il fruitore richiede l’esito
della sua richiesta.

Endpoint

`https://api.ente.example/soap/nome-api/v1 <https://api.amministrazioneesempio.it/soap/nomeinterfacciaservizio/v1>`__

Method MProcessingStatus

5. Request Body result

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Header>
		<m:X-Correlation-ID>c8e191a8-f34f-41ed-82ea-68e096466707</m:X-Correlation-ID>
	  </soap:Header>
	  <soap:Body>
		<m:MResponse/>
	  </soap:Body>
	</soap:Envelope>

4. Response Body (HTTP status code 200 OK) result

.. code-block:: xml

	<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://ente.example/nome-api">
	  <soap:Body>
		<m:MResponseResponse>
		  <return>
			<c>OK</c>
		  </return>
		</m:MResponseResponse>
	  </soap:Body>
	</soap:Envelope>

