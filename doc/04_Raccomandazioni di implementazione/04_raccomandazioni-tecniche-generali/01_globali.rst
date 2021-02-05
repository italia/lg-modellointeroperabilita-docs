Raccomandazioni globali
-----------------------

[RAC_GEN_001] Descrizione delle API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le API DEVONO essere rappresentate mediante un Interface Description
Language standard (IDL). Nello specifico:

-  per REST, OpenAPI 3.0 e successive;

-  per SOAP, WSDL 1.1 e successive.

[RAC_GEN_002] Endpoint delle API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il numero di versione NON DEVE essere presente all’interno del nome
della API.

Si DOVREBBE indicare il numero di versione e la tecnologia nell’endpoint
delle API.

Esempio:

.. code-block:: python

   https://<dominioOrganizzativo>/[rest|soap]/<DominioApplicativo>/v<major>[.<minor>[.<patch>]]/<NomeAPI>

dove:

-  ​<dominioOrganizzativo> indica l'organizzazione che espone il
   servizio;

-  [rest|soap] indica la tecnologia della API;

-  <DominioApplicativo> indica il settore all’interno
   dell’organizzazione;

-  v<major>[.<minor>[.<patch>]] indica il numero di versione in coerenza
   con Semantic Versioning 2.0.0 [1]_;

-  <NomeAPI> è il nome della specifica API.

[RAC_GEN_003] Codifica di default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si DOVREBBE utilizzare UTF-8 come codifica di default per i dati.

[RAC_GEN_004] Non passare credenziali o dati riservati nell’URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eventuali dati riservati o credenziali e token di autenticazione NON
DEVONO essere passati nei query parameters o comunque nell’URL.

.. [1]
   Cfr. https://semver.org/

.. forum_italia::
   :topic_id: 21487
   :scope: document
