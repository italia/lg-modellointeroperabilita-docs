Raccomandazioni tecniche per SOAP
=================================

In questo capitolo si raccolgono delle indicazioni per la tecnologia
SOAP, al fine di favorire l’interoperabilità.

[RAC_SOAP_001] Le API SOAP DEVONO rispettare il WS-I Basic Profile versione 2.0
-------------------------------------------------------------------------------

Questo profilo è definito dal WS-I (Web Services Interoperability
Organization), ora confluito in OASIS. Questa specifica è implementata
dai framework più diffusi.

[RAC_SOAP_002] Utilizzo di camelCase e PascalCase
-------------------------------------------------

Per i nomi dei servizi si DOVREBBE utilizzare PascalCase.

Per le operazioni implementate e gli argomenti si DOVREBBE utilizzare il
camelCase.

[RAC_SOAP_003] Unicità dei namespace e utilizzo di pattern fissi
----------------------------------------------------------------

All’interno del WSDL DOVREBBE essere presente un namespace unico.

[RAC_SOAP_004] Esporre lo stato del servizio
--------------------------------------------

L'API DEVE includere un metodo \`echo\` per restituire lo stato della
stessa.

ESEMPIO: Esposizione stato del servizio

.. literalinclude:: file-379e37e7cb90b316fbcdbbe766a7969473e9c737c1f614365773255fe7da7640.xml
   :language: xml
