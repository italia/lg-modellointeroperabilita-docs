Pattern non bloccanti RPC PULL (busy waiting)
=============================================

Questo caso particolare, denominato RPC PULL, è utilizzabile nel caso in
cui il fruitore non abbia a sua volta la possibilità di esporre una
interfaccia di servizio per la ricezione delle risposte. L’erogatore 
fornisce un indirizzo interrogabile per verificare lo stato
di processamento di una richiesta e, alla fine dell’elaborazione della
stessa, il risultato.

Questo scenario prevede due possibili workflow, uno per REST ed uno per
SOAP riportati nelle seguenti figure.

.. mermaid::

   sequenceDiagram

    activate Erogatore
    activate Fruitore
    Fruitore->>Erogatore: 1. Request()
    Erogatore-->>Fruitore: 2. Location
    loop status pending
		Fruitore->>Erogatore: 3. CheckStatus()
		Erogatore-->>Fruitore: 4. Not Ready OR Ready Location
    end
    Fruitore->>Erogatore: 5. RetriveResult()
    Erogatore-->>Fruitore: 6. Result
    deactivate Fruitore
    deactivate Erogatore

*Figura 3 - Interazione non bloccante tramite busy waiting REST*

Il fruitore invia una richiesta (passo (1)) e riceve immediatamente un
acknowledge (passo (2)) insieme ad:

-  un indirizzo dove verificare lo stato del processamento (REST);

-  oppure un CorrelationID (SOAP).

D’ora in poi il fruitore, periodicamente, verifica (passo (3)) lo stato
della richiesta utilizzando:

-  l’url indicato (REST)

-  oppure il CorrelationID (SOAP)

fin quando la risposta alla richiesta sarà pronta (passo (4)).

Gli intervalli di polling possono essere definiti tra le parti.

Quando la risposta è pronta il fruitore può accedere (passi (5) e (6))
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
     Fruitore->>Erogatore: 5. RetriveResult(CorrelationID)
     Erogatore-->>Fruitore: 6. Result
     deactivate Fruitore
     deactivate Erogatore

*Figura 4 - Interazione non bloccante tramite busy waiting SOAP*

.. toctree::
  :maxdepth: 3

  02_nonblock_pull/01_nonblock_pull_rest.rst
  02_nonblock_pull/02_nonblock_pull_soap.rst