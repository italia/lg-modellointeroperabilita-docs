Termini e definizioni
=====================

+-----------------------------------+-----------------------------------+
| **[AgID]**                        | Agenzia per l’Italia Digitale     |
+-----------------------------------+-----------------------------------+
| **[CAD]**                         | Codice Amministrazione Digitale,  |
|                                   | D.lgs. 7 marzo 2005, n. 82        |
+-----------------------------------+-----------------------------------+
| **[PA]**                          | Pubblica Amministrazione          |
+-----------------------------------+-----------------------------------+
| **[UML]**                         | Linguaggio di modellazione        |
|                                   | unificato (Unified Modeling       |
|                                   | Language)                         |
+-----------------------------------+-----------------------------------+
| **[RPC]**                         | Remote procedure call             |
+-----------------------------------+-----------------------------------+
| **[SOAP]**                        | Simple Object Access Protocol     |
+-----------------------------------+-----------------------------------+
| **[REST]**                        | Representational State Transfer   |
+-----------------------------------+-----------------------------------+

4. .. rubric:: 
      Principi generali
      :name: principi-generali

   6. .. rubric:: Interazione bloccante e non bloccante
         :name: interazione-bloccante-e-non-bloccante

Nell’interazione bloccante un fruitore effettua una chiamata al servente
ed attende una risposta prima di continuare l’esecuzione. La chiamata
codifica in modo opportuno la richiesta di servizio, anche attraverso il
passaggio di dati (sia in input alla chiamata che in output nella
risposta).

Nell’interazione non bloccante, invece, il fruitore invia un messaggio
ma non si blocca in attesa di alcuna risposta (se non una notifica di
presa in carico). Il messaggio contiene in modo opportuno la richiesta
ed eventuali dati di input. Talvolta il messaggio, proprio ad indicare
il fatto che codifica la richiesta e le informazioni necessarie a
soddisfarla, viene indicato come documento. La risposta da parte del
servente, nei casi in cui ci sia, può apparire significativamente più
tardi, ove significativamente va interpretato rispetto al tempo di
computazione proprio dell’interazione. Anche la risposta del servente
viene inviata tramite un messaggio.

Con abuso di nomenclatura, la comunicazione bloccante talvolta viene
detta sincrona, ad indicare che client e servente si sono sincronizzati
(attesa di uno da parte dell’altro); quella non bloccante viene detta
asincrona, proprio a significare l’asincronicità che vi è tra l’invio di
un messaggio e la risposta al messaggio stesso.

*Alonso, G., Casati, F., Kuno, H., Machiraju, V. (2004). Web Services.
Concepts, Architectures and Applications. Springer*
