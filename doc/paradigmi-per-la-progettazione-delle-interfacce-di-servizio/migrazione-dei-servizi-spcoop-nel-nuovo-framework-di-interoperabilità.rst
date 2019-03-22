Migrazione dei servizi SPCoop nel nuovo framework di interoperabilità
=====================================================================

Il principio API-first, richiamato nel Piano Triennale per l'informatica
nella Pubblica Amministrazione, richiede la progettazione dei sistemi
con un approccio strutturato partendo dalla definizione delle interfacce
tra le varie componenti. Tutto questo senza dare priorità alle
tecnologie usate per la loro implementazione (nel caso dei servizi le
due tecnologie SOAP/REST). In questa logica per i servizi in produzione
nel contesto del precedente modello di interoperabilità (SPCoop),
sviluppati in tecnologia SOAP e definiti tramite accordi di servizio e
pertanto pienamente aderenti al paradigma API First, non viene richiesta
alcun adeguamento tecnologico. L’unico passo richiesto è quello
dell'eliminazione del nodo di middleware rappresentato dalla *Porta di
dominio* (PdD) orientato alla gestione dell’header Intestazione che
caratterizzava la busta di egov.

L’eliminazione della PdD deve portare l’amministrazione a preservare le
interfacce di servizio attualmente disponibili su tecnologia SOAP, in
coerenza con quanto indicato nelle linee guida per la transizione al
nuovo sistema di interoperabilità [1]_ e nell’allegato del Piano
Triennale.

La possibilità di mantenere i servizi erogati/fruiti con interfacce di
servizio SOAP, permette di preservare gli investimenti fatti dalle
amministrazioni, e quindi orientare i nuovi fondi alla realizzazione di
nuovi servizi.

La scelta della tecnologia tra SOAP e REST non può prescindere da una
analisi funzionale e non-funzionale dei servizi che tenga conto sia
degli impatti degli erogatori, sia e soprattutto dei fruitori. Infatti
si deve evitare che i fruitori eseguino reingegnerizzazioni finalizzate
solo al cambio tecnologico da SOAP a REST, ma, per esigenze specifiche,
l’amministrazione erogatrice può far coesistere per lo stesso servizio
interfacce basate su entrambe le tecnologie (SOAP e REST).

.. [1]
   https://www.agid.gov.it/sites/default/files/repository_files/upload_avvisi/linee_guida_passaggio_nuovo_modello_interoperabilita.pdf
