Service Level Agreement – SLA
=============================

L’integrazione può coinvolgere numerose organizzazioni e erogatori
esterni di API. Al fine di accordarsi sulla QoS, gli erogatori e i
fruitori di API utilizzano quelli che vengono definiti Service Level
Agreement (SLA), ovvero accordi sul livello di servizio. Un SLA può
contenere le parti seguenti:

-  Scopo. Le ragioni che hanno portato alla definizione del SLA;

-  Parti. I soggetti interessati dal SLA e i rispettivi ruoli (ad es.,
   l’erogatore dell’interfaccia di servizio e il fruitore);

-  Periodo di validità. L’intervallo di tempo, espresso mediante data,
   ora di inizio, data e ora di fine, per il quale si ritiene valido un
   particolare termine di accordo all’interno degli SLA;

-  Perimetro. Quali sono operazioni interessate dallo specifico SLA;

-  Service Level Objectives (SLO), ovvero obiettivi sul livello di
   servizio. I singoli termini di accordo all’interno di un SLA. Di
   solito, sono definiti utilizzando dei Service Level Indicators (SLI),
   ovvero indicatori sul livello di servizio, che quantificano i singoli
   aspetti di QoS (ad es., la disponibilità);

-  Penalità. Le sanzioni che si applicano nel caso che l’erogatore
   dell’interfaccia di servizio non riesca ad assicurare gli obiettivi
   specificati nel SLA;

-  Esclusioni. Gli aspetti della QoS non coperti dal SLA;

-  Amministrazione. I processi mediante i quali le parti possono
   monitorare la QoS.

Gli SLA possono essere statici o dinamici. Negli SLA dinamici, i SLO
(con associati SLI) variano nel tempo e i periodi di validità
definiscono gli intervalli di validità di questi ultimi (ad es., in
orario lavorativo i SLO possono essere differenti da quelli imposti
durante la notte). La misurazione dei livelli di QoS all’interno di un
SLA richiedono il tracciamento delle operazioni effettuate in un
contesto infrastrutturale multi-dominio (geografico, tecnologico e
applicativo). In uno scenario tipico, ogni interfaccia di servizio può
interagire con molteplici altre API, modificando il suo ruolo da
erogatore a fruitore per alcune interazioni, ognuna governata da un
differente SLA.
