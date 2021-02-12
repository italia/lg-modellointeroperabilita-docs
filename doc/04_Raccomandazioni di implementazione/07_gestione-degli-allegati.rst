Gestione degli allegati
=======================

Tra i parametri o i valori di ritorno di una interfaccia di servizio può
esserci la presenza di allegati, dove per allegato si intende un
contenuto binario, o la cui struttura comunque non è definita
direttamente dall’interfaccia di servizio (e.g., un file XML all’interno
di un messaggio di SOAP in cui lo schema che definisce il messaggio SOAP
non specifica anche la struttura dell’XML allegato). In generale, un
allegato può essere passato o ricevuto nelle seguenti forme:

-  Codificato in modo da essere rappresentabile con un set predefinito
   di caratteri. Il caso più comune è quello della codifica Base64.

-  Come URL ad una risorsa esterna o in ogni caso come endpoint di
   accesso ad una risorsa.

-  Nel suo formato binario originale.

Nei primi due casi, l’allegato fa parte del contenuto XML o JSON del
messaggio, mentre nel secondo caso si ricorre a risposte di tipo
multipart.

Ognuna di queste modalità presenta vantaggi e svantaggi. L’utilizzo di
codifiche come Base64 oppure di URL ha il vantaggio di potere inserire
un allegato all’interno del contenuto principale del messaggio. Si noti
come anche nel caso di XML l’utilizzo di formati binari all’interno dei
campi CDATA sia sconsigliato poiché esiste il rischio che il contenuto
binario possa talvolta chiudere il campo CDATA stesso. D’altro canto,
l’utilizzo di codifiche comporta un incremento nella banda richiesta
poiché l’occupazione dei dati non è, in generale, ottimale. L’utilizzo di URL comporta
invece un potenziale rischio potenziale poiché la risorsa collegata può
essere successivamente modificata o rimossa.

In ambito SOAP, la prima proposta di standard per l’invio di allegati
binari è rappresentato da SWA - SOAP with Attachments, a cui il W3C ha
però preferito come standard MTOM - Message Transmission Optimization
Mechanism, che ha il vantaggio di estendere agli allegati i meccanismi
di sicurezza quali WS-Encryption e WS-Signature. MTOM è solitamente
utilizzato insieme a XOP - XML-binary Optimized Packaging quale
meccanismo per fare riferimento agli allegati all’interno del messaggio
Multipart/Related. L’utilizzo di MTOM con XOP è supportato da tutti i
maggiori framework per lo sviluppo di interfacce di servizio SOAP, ma
meccanismi similari, sempre basati su XOP, sono supportati anche dai
maggiori framework per lo sviluppo di interfacce di servizio REST.

L’utilizzo di un approccio o di un altro dipende fortemente dallo
scenario applicativo. Possono essere utilizzate seguenti regole:

-  L’invio di allegati binari corrispondenti a file fa preferire
   solitamente l’invio di dati in formato binario, quindi mediante
   MTOM/XOP.

-  L’utilizzo di Base64 è consigliato per l’invio di allegati di
   dimensioni ridotte quali ad esempio firme digitali o codici di
   controllo.

-  L’utilizzo di URL può essere considerato nel caso in cui gli allegati
   siano di dimensioni tali da rendere il trasferimento via rete
   oneroso, a patto che si possa assicurare la persistenza della risorsa
   (in termini temporali) e che questa non venga modificata (a tal fine
   è possibile utilizzare tecniche ad esempio di hashing). Quest’ultimo
   caso richiede quindi solitamente trust tra fruitore ed erogatore.

.. forum_italia::
   :topic_id: 21497
   :scope: document
