Profili di Interazione
=======================

Il *profilo di interazione* definisce le modalità secondo le quali un
fruitore ed un erogatore possono interagire, l’interazione avviene
definendo le interfacce di servizio che comprendono le primitive dei
messaggi scambiati. I *profili di interazione* quali riferimenti
concettuali coniugano, fatto salvo per l’accesso CRUD, message exchange
pattern (MEP) per le tecnologie SOAP e REST proposte dal ModI.
L’attenzione in questa sezione delle linee guida viene rivolta agli
aspetti funzionali rimandando per gli aspetti di sicurezza alla apposita
sezione delle linee guida.

Per i concetti di bloccante e non bloccante si rimanda alla lettura del
capitolo 3 del documento.

Ogni interfaccia di servizio sviluppata nell’ambito della pubblica
amministrazione deve essere corredata da una specifica di interfaccia
che utilizzi un IDL - Interface Description Language standard che il
ModI fissa:

-  per le interfacce di servizio REST, OpenAPI 3.0 e successive

-  per le interfacce di servizio SOAP, WSDL 1.1 e successive

L’endpoint deve indicare in modo esplicito la tecnologia utilizzata
(REST o SOAP) e la versione (versioning su URL).

.. toctree::
  :maxdepth: 3
  :caption: Contenuti

  profili-di-interazione/modalità-di-descrizione-dei-profili.rst
  profili-di-interazione/profilo-bloccante-rpc.rst
  profili-di-interazione/profili-non-bloccanti.rst
  profili-di-interazione/accesso-crud-a-risorse.rst
  profili-di-interazione/robustezza.rst
  profili-di-interazione/passaggio-di-allegati.rst
