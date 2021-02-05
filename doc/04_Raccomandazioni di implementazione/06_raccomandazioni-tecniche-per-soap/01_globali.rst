Raccomandazioni globali
-----------------------

[RAC_SOAP_001] Le API SOAP DEVONO rispettare il WS-I Basic Profile versione 2.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo profilo è definito dal WS-I (Web Services Interoperability
Organization), ora confluito in OASIS. Questa specifica è implementata
dai framework più diffusi.

[RAC_SOAP_002] Utilizzo di camelCase e PascalCase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per i nomi dei servizi si DOVREBBE utilizzare PascalCase.

Per le operazioni implementate e gli argomenti si DOVREBBE utilizzare il
camelCase.

[RAC_SOAP_003] Unicità dei namespace e utilizzo di pattern fissi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All’interno del WSDL DOVREBBE essere presente un namespace unico.

[RAC_SOAP_004] Esporre lo stato del servizio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'API DEVE includere un metodo \`echo\` per restituire lo stato della
stessa.

ESEMPIO: Esposizione stato del servizio

.. literalinclude:: media/RAC_SOAP_002_example.xml
   :language: xml

.. forum_italia::
   :topic_id: 21496
   :scope: document
