Tecnica
=======

Gli Erogatori rendono disponibili gli e-service individuati nella fase 
organizzativa, assicurando:

- l’attuazione del modello dati definito nella fase semantica;

- la conformità ai pattern e/o profili di interoperabilità individuati 
  dalle presenti Linee Guida.

L’obiettivo della fase tecnica è:

- definire le API quali descrizione di tutte le informazioni che 
  caratterizzano un e-service per una specifica tecnologia;

- stipulare gli accordi di interoperabilità quali contratti tra due 
  soggetti (PA, cittadino o impresa) in cui sono definite le regole per 
  usufruire di un e-service (responsabilità, ruoli organizzativi).

Sono di seguito elencate le regole che erogatori e fruitori DEVONO 
attuare e le raccomandazioni che invece DOVREBBERO seguire.

Gli erogatori DEVONO:

.. list-table:: 
   :widths: 15 40
   :header-rows: 0

   * - (REG_TECNICA_001)
     - Dare seguito all’analisi tecnica dei requisiti che, per ogni 
       e-service, individui le caratteristiche funzionali o non 
       funzionali per:

         * (REG_TECNICA_001.a) Selezionare la porzione del modello dati 
           individuato nella fase semantica.
               
         * (REG_TECNICA_001.b) Individuare le tecnologie tra SOAP o REST.

         * (REG_TECNICA_001.c) Individuare i pattern di interazione.

         * (REG_TECNICA_001.d) Individuare i pattern di sicurezza.

   * - (REG_TECNICA_002) 
     - Implementare le API.

   * - (REG_TECNICA_003) 
     - Esporre ai fruitori una funzione utile a verificare lo stato di 
       funzionamento delle API.
 
|

Gli erogatori POSSONO:

.. list-table:: 
   :widths: 15 40
   :header-rows: 0

   * - (RAC_TECNICA_001)
     - Erogare contemporaneamente gli e-service con API in tecnologia 
       SOAP e REST.

|

Gli erogatori DOVREBBERO:

.. list-table:: 
   :widths: 15 40
   :header-rows: 0

   * - (RAC_TECNICA_002)
     - Adottare architetture capaci di  adeguare l’offerta di e-service 
       all'aumento dei fruitori, in modo da rispondere agli SLA concordati.

|

La fase tecnica si conclude con l’attuazione di quanto disposto in 
"Governance dei servizi" relativamente alla pubblicazione degli e-service 
e della sottoscrizione degli accordi di interoperabilità.

|image0|

*Figura 3 - Relazione tra interfaccia di servizio - e-service –
servizio*

.. |image0| image:: ../media/image3.png
   :width: 4.125in
   :height: 4.19444in

.. forum_italia::
   :topic_id: 21441
   :scope: document
