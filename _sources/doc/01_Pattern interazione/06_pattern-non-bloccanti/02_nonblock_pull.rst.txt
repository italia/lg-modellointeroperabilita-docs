Pattern non bloccanti RPC PULL (busy waiting)
=============================================

Questo caso particolare, denominato RPC PULL, è utilizzabile nel caso in
cui il fruitore non abbia a sua volta la possibilità di esporre una
interfaccia di servizio per la ricezione delle risposte.
L’erogatore fornisce un URL per verificare lo stato
di processamento di una richiesta e, alla fine dell’elaborazione della
stessa, il risultato.

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

.. toctree::
  :maxdepth: 3

  02_nonblock_pull/01_nonblock_pull_rest.rst
  02_nonblock_pull/02_nonblock_pull_soap.rst

.. forum_italia::
   :topic_id: 21458
   :scope: document
