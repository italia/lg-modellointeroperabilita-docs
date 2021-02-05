Roccomandazioni sulla progettazione e naming
--------------------------------------------

[RAC_GEN_NAME_001] Utilizzare i nomi delle proprietà secondo nomenclature standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le proprietà DEVONO utilizzare, ove possibile, la nomenclatura indicata
nelle Linee Guida per la valorizzazione del Patrimonio [1]_ informativo
pubblico e le relative ontologie [2]_.

[RAC_GEN_NAME_002] Nomenclatura delle proprietà
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le proprietà DOVREBBERO avere una nomenclatura consistente.

Scegliere uno dei due stili di seguito e modificarlo in ASCII:

-  snake_case
-  camelCase

Non usare contemporaneamente snake_case e camelCase nella stessa API.

Ad esempio:

SI

.. code-block:: python

   {
     "givenName": "Mario",
     "familyName": "Rossi"
   }

SI

.. code-block:: python

   {
     "given_name": "Mario",
     "family_name": "Rossi"
   }

NO

.. code-block:: python

   {
     "given_name": "Mario",
     "familyName": "Rossi"
   }

SI

.. code-block:: xml

   <givenName>Mario</givenName>
   <familyName>Rossi</familyName>

SI

.. code-block:: xml

   <given_name>Mario</given_name>
   <family_name>Rossi</family_name>

NO

.. code-block:: xml

   <given_name>Mario</given_name>
   <familyName>Rossi</familyName>

[RAC_GEN_NAME_003] Descrittività dei nomi utilizzati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I nomi utilizzati per servizi, path, operation o schemi DEVONO essere
auto-descrittivi e fornire quanta più informazione utile riguardo al
comportamento implementato, evitando però le ridondanze.

Si deve inoltre evitare l’utilizzo di acronimi quando questi non siano
universalmente riconosciuti anche al di fuori del dominio applicativo.

Esempio in un’architettura orientata alle risorse:



   In un servizio per la gestione delle istanze dei cittadini, il nome
   dell'attributo
   
   :code:`gestioneIstanzeCittadinoAbilitatoBoolean`
   
   può essere semplificato in
   
   :code:`cittadinoAbilitato`
   
   se il servizio è limitato alla gestione delle istanze e l'output del
   campo è desumibile dal contesto.

.. [1]
   Cfr.
   https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/index.html

.. [2]
   Cfr. https://github.com/italia/daf-ontologie-vocabolari-controllati

.. forum_italia::
   :topic_id: 21489
   :scope: document
