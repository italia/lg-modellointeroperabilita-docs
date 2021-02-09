Introduzione
============

I pattern di sicurezza definiscono le modalità per assicurare che le
interazioni tra fruitore ed erogatore siano realizzate nel rispetto
delle specifiche esigenze di sicurezza determinate dalla natura delle
transazioni realizzate e dalle prescrizioni normative che riguardano le stesse.

I pattern di sicurezza si applicano ai pattern di interazione indicati
nel Documento Operativo - Pattern di interazione, e sono scelti
dall'erogatore in funzione alle specifiche esigenze applicative in
relazione alla natura dei fruitori.

Il Documento operativo descrive i pattern di sicurezza individuati da
AgID che gli erogatori DEVONO utilizzare per soddisfare le necessità
individuate dai requisiti funzionali e non funzionali delle specifiche
interazioni con i propri fruitori.

Data la variabilità nel tempo delle esigenze delle amministrazioni e
delle tecnologie abilitanti, nonché considerata la natura incrementale
del ModI, l’elenco dei pattern di sicurezza non è da intendersi
esaustivo. Nel caso in cui un’amministrazione abbia esigenze non
ricoperte nei seguenti profili DEVE informare AGID, nei modi indicati
nel capitolo 7 "Pattern e profili di interoperabilità" delle Linee di
indirizzo sull’interoperabilità tecnica delle Pubbliche Amministrazioni.

I pattern di sicurezza individuati coprono gli aspetti di comunicazione
"sicura" tra i domini delle singole parti. Le parti mantengono la loro
autonomia negli aspetti organizzativi e di sicurezza interni al proprio
dominio.

I pattern di sicurezza

-  definiscono a livello di specifica tecnologica uno «strumento
   condiviso» utile a favorire l’interoperabilità tra erogatori e
   fruitori.

-  forniscono un comune linguaggio per fruitori ed erogatori utile a
   trattare le necessità e le caratteristiche delle interfacce di
   servizio.

-  offrono agli sviluppatori le modalità tecniche supportate da standard
   tecnologici documentati, revisionati e testati per esporre i servizi
   digitali.

I pattern di sicurezza affrontano il tema della sicurezza su due livelli
differenti:

-  Canale: definisce le modalità di trasporto dei messaggi tra i confini
   dei domini delle entità coinvolte.

-  Messaggio: definisce le modalità di comunicazione dei messaggi tra
   componenti interne dei domini delle entità coinvolte.

Ogni pattern di sicurezza è strutturato come segue:

-  Descrizione: rappresentazione in linguaggio naturale del profilo con
   relativi precondizioni e obiettivi.

-  Regole di processamento: elenco dei passi da eseguire per
   implementare il profilo.

-  Tracciato: ove presente, fornisce un esempio dei messaggi prodotti
   nell’interazione.

Gli erogatori, ove necessario in accordo con i fruitori, a seguito
dell’analisi dei requisiti realizzata, per individuare le proprie
esigenze funzionali e non funzionali, DOVREBBERO:

-  individuare tra i pattern di interazione (vedi Documento operativo -
   Pattern di interazione) quelli che soddisfano le proprie esigenze;

-  individuare tra i pattern di sicurezza quelli che soddisfano le
   proprie esigenze;

-  implementare le interfacce di servizio attraverso la combinazione dei
   pattern di interazione e di pattern di sicurezza.

L’individuazione dei pattern di sicurezza DEVE ricoprire solamente i
requisiti necessari.

Il *Trust* è uno dei mezzi più importanti per gestire le problematiche di
sicurezza nello scambio di informazione in rete per consentire
l’interoperabilità tra i sistemi. Esso si basa sul reciproco
riconoscimento delle entità interagenti e sulla fiducia nei rispettivi
comportamenti.

Nel presente Documento operativo, per *direct trust* si intende la
relazione di fiducia tra fruitore ed erogatore, stabilita in modalità
diretta, attraverso accordi che si basano sulla condivisione del
reciproco modus operandi.

Si rimanda alle Linee Guida sulla sicurezza, emanate dall'Agenzia per 
l'Italia Digitale ai sensi dell'articolo 71 del decreto legislativo 7 
marzo 2005, n. 82 (Codice dell'Amministrazione Digitale), in merito 
agli algoritmi utilizzabili per la corretta implementazione dei pattern 
di sicurezza.

.. forum_italia::
   :topic_id: 21462
   :scope: document
