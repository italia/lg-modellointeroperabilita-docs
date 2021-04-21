Raccomandazioni sul logging
---------------------------

[RAC_GEN_LOG_01] Informazioni di Logging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I log file DEVONO contenere:

-  l’istante della comunicazione in formato UTC (:rfc:`3339`) e con i
   separatori Z e T in maiuscolo. La specifica è fondamentale per
   l’interoperabilità dei sistemi di logging e auditing, evitando
   problemi di transizione all’ora legale e la complessità nella
   gestione di fusi orari nell’ottica dell’interoperabilità con altre PA
   europee;

-  l’URI che identifica l’erogatore e l’operazione richiesta;

-  la tipologia di chiamata (ad esempio, metodo HTTP per i protocolli
   basati su HTTP);

-  esito della chiamata (ad es., stato della response HTTP se
   disponibile, SOAP fault nel caso di web service SOAP);

-  ove applicabile, l’Indirizzo IP del client;

-  ove applicabile, identificativo del consumatore o altro soggetto
   operante la richiesta comunicato dal fruitore. È cura del fruitore
   procedere alla codifica e all’anonimizzazione, ove necessario;

-  ove applicabile, un identificativo univoco della richiesta, utile a
   eventuali correlazioni.

.. forum_italia::
   :topic_id: 21490
   :scope: document
