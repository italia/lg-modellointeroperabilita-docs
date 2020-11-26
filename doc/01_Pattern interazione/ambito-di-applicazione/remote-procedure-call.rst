Remote Procedure Call
=====================

Una Remote Procedure Call (chiamata a procedura remota, RPC) consiste
nell’attivazione, da parte di un programma, di una procedura o
subroutine attivata su un elaboratore diverso da quello sul quale il
programma viene eseguito. Quindi l’RPC consente a un programma di
eseguire subroutine «a distanza» su elaboratori remoti, accessibili
attraverso una rete. Essenziale al concetto di RPC è l’idea di
trasparenza: la chiamata di procedura remota deve essere infatti
eseguita in modo il più possibile analogo a quello della chiamata di
procedura locale; i dettagli della comunicazione su rete devono essere
«nascosti» (resi trasparenti) all’utilizzatore del meccanismo. Se il
linguaggio è orientato agli oggetti, l’invocazione della procedura
remote è in realtà l’invocazione di un metodo su un oggetto remoto, e si
parla di Remote Method Invocation - RMI.

RPC/RMI è il meccanismo base con cui realizzare una interazione
bloccante.
