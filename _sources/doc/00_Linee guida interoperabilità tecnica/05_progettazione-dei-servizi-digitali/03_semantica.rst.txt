Semantica
=========

La comunicazione tra soggetti DEVE utilizzare modelli dati condivisi, 
in modo da razionalizzare e uniformare la rappresentazione
dell'informazione quale presupposto per favorire l’interoperabilità tra 
soggetti differenti.

L’adozione di modelli dati condivisi permette ai soggetti che comunicano, 
di partire da una rappresentazione dei dati comune, evitando la 
proliferazione di modelli dati differenti impattano direttamente sulla 
modalità con cui i dati vengono resi persistenti. Ne consegue che 
l'adozione di modelli dati condivisi favorisce il riuso delle strutture 
dati, semplifica le integrazioni e assicura che gli elementi dei dati 
siano compresi nello stesso modo tra le parti tra loro comunicanti.

Il modello dati è un modello astratto che organizza gli elementi dei 
dati e standardizza il modo in cui si relazionano tra loro e con le 
proprietà delle entità del mondo reale [1]_.

La definizione dei modelli dati condivisa deriva le sue entità dalle 
ontologie che rappresentano la specifica formale ed esplicita di 
rappresentazione (concettualizzazione) condivisa di un dominio di 
conoscenza, definita sulla base di requisiti individuati.

I soggetti erogatori di e-service, nell’individuazione delle entità da 
condividere DEVONO:

.. list-table:: 
   :widths: 15 40
   :header-rows: 0

   * - (REG_SEMANTICA_001)
     - Individuare i domini di interesse e in essi determinare le entità 
       da rappresentare in termini di proprietà che li caratterizzano.

   * - (REG_SEMANTICA_002)
     - Verificare la presenza delle entità per dominio tra quelli 
       definiti a livello nazionale da AgID [3]_.

|

Si precisa che successivamente all’attuazione della REG_SEMANTICA_002 
l'erogatore può trovarsi in uno dei seguenti casi:

1. tutte le entità e le relative proprietà trovano copertura;

2. almeno una delle entità non è compresa nelle rappresentazioni;

3. almeno una proprietà di un’entità presente non risulta rappresentata.

Nel caso 1), l'erogatore ha tutti gli elementi per rappresentare il 
proprio modello dati; viceversa, nei casi 2) e 3), la stessa
amministrazione, in accordo con AgID, valutano l’opportunità di 
definire/aggiornare delle entità e/o proprietà a livello nazionale.

.. [1]
   Cf. https://en.wikipedia.org/wiki/Data_model

.. [2]
   Cf. https://github.com/italia/daf-ontologie-vocabolari-controllati

.. [3]
   Cf. https://github.com/italia/daf-ontologie-vocabolari-controllati

.. forum_italia::
   :topic_id: 21440
   :scope: document
