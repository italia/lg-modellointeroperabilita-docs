Raccomandazioni sul formato dei dati
------------------------------------

[RAC_REST_FORMAT_001] Utilizzo oggetti JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nella tecnologia REST la comunicazione DOVREBBE avvenire tramite oggetti
JSON :rfc:`8259` con il relativo media-type application/json.

È possibile fare eccezione in presenza di specifiche in cui gli oggetti di
comunicazione sono formalizzati in forma diversa da JSON (es. INSPIRE,
HL7).

[RAC_REST_FORMAT_002] Codificare dati strutturati con oggetti JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I dati strutturati in formato JSON :rfc:`8259` DOVREBBERO essere trasferiti
tramite oggetti, in modo da permettere l’estensione retrocompatibile
della response con ulteriori attributi, ad esempio paginazione.

Cioè:

-  il payload di una response contenente una entry ritorna un oggetto

.. code-block:: python

	{
		"given_name": "Paolo",
		"last_name": "Rossi",
		"id": 313
	}

-  il payload di una response contenente più entry ​ritorna un oggetto
   contenente una lista​ e non direttamente una lista.

.. code-block:: python

	{
		"items": [
			{
				"given_name": "Carlo",
				"family_name": "Bianchi",
				"id": 314
			},
			{
				"given_name": "Giuseppe",
				"family_name": "Verdi",
				"id": 315
			}
		]
	}

[RAC_REST_FORMAT_003] Convenzioni di rappresentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DEVONO usarsi le seguenti convenzioni di rappresentazione:

-  I booleani non DEVONO essere null.

-  Gli array vuoti non DEVONO essere null, ma liste vuote, ad es. [].

-  Le enumeration DEVONO essere rappresentate da stringhe non nulle.

[RAC_REST_FORMAT_004] Definire format quando si usano i tipi Number ed Integer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I numeri e gli interi DEVONO indicare la dimensione utilizzando il
parametro format.

La seguente tabella - non esaustiva - elenca un set minimo di formati.

.. list-table:: Set minimo dei formati
   :widths: 15 20 20  
   :header-rows: 1

   * -    TYPE
     -    FORMAT
     -    VALORI AMMESSI

   * -    integer
     -    int32
     -    interi tra -2^31 e 2^31-1

   * -    integer
     -    int64
     -    interi tra -2^63 e 2^63-1

   * -    number
     -    decimal32 / float 
     -    IEEE 754-2008/IS 60559:2011 decimale a 32 bit 

   * -    number
     -    decimal64 / double 
     -    IEEE 754-2008/IS 60559:2011 decimale a 64 bit

   * -    number
     -    decimal128
     -    IEEE 754-2008/IS 60559:2011 decimale a 128 bit 


Le implementazioni DEVONO utilizzare il tipo più adatto.

[RAC_REST_FORMAT_005] Usare link relations registrate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DEVONO usarsi le specifiche indicate in IANA registered link
relations [1]_ per rappresentare link e riferimenti a risorse HTTP
esterne.

.. [1]
   Cfr.
   https://www.iana.org/assignments/link-relations/link-relations.xhtml

.. forum_italia::
   :topic_id: 21493
   :scope: document
