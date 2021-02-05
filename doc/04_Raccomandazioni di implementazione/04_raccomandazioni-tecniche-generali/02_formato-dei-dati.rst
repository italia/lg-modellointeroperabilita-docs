Roccomandazioni sul formato dei dati
------------------------------------

[RAC_GEN_FORMAT_001] Utilizzare Content-Type semanticamente coerenti
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando si ritornano dati binari, immagini o documenti (eg. pdf, png, …)
si DEVONO utilizzare i rispettivi Content-Type.
Nel protocollo HTTP, l’:httpheader:`Content-Type` indica il media-type di una risorsa.

[RAC_GEN_FORMAT_002] Evitare Content-Type personalizzati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si DOVREBBE evitare l’uso di media-type personalizzati come da
:rfc:`6838#section-3.4` (eg. application/x.custom.name+xml,
application/x.custom.name+json) ed utilizzare nomi standard come:

-  application/xml
-  application/soap+xml
-  application/json​
-  application/problem+json​
-  application/jose+json

L'elenco dei media-type è reperibile sul `sito IANA <https://www.iana.org/assignments/media-types/media-types.xhtml>`_.


[RAC_GEN_FORMAT_003] Formati standard per Data ed Ora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le date DEVONO essere conformi:

-  alla sintassi "full-date" indicata in :rfc:`3339`, ad esempio 2015-05-28
   se si indica una data;

-  alla sintassi "date-time" indicata in :rfc:`3339`, ad esempio
   2015-05-28T14:07:17Z o nel formato UNIX Timestamp definito in "The
   Open Group Base Specifications Issue 7, Rationale: Base Definitions,
   section A.4 General Concepts" se si indica un momento esatto nel
   tempo.

:rfc:`3339` permette di indicare una timezone prefissando la data con la
distanza da UTC:

-  2015-05-28T14:07:17+01:00

-  2015-05-28T14:07:17-05:00

Quando la data è specificata in UTC occorre utilizzare sempre il
suffisso Z (Zulu time zone):

-  2015-05-28T14:07:17Z

Ove non dettagliato nelle specifiche, le date negli header HTTP DEVONO
essere conformi:

-  o al formato UNIX Timestamp;

-  o alla sintassi HTTP-date definito in :rfc:`7231`, eg. "Sun, 06 Nov 1994 08:49:37 GMT".

[RAC_GEN_FORMAT_004] Tempi di durata e intervalli
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I tempi di durata e gli intervalli DEVONO essere espresse in secondi o
usare lo standard ISO 8601.

Di seguito alcuni esempi di durata in formato ISO 8601.

I tempi di durata sono prefissati da «P»; giorni e ore sono separati da
«T».

Esempi:

-  P1Y2M3D - 1 anno, 2 mesi e 3 giorni

-  PT1H4M5S - 1 ora, 4 minuti e 5 secondi

-  P1M - 1 mese

-  PT1M - 1 minuto

-  P1Y2M10DT2H30M - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

[RAC_GEN_FORMAT_005] Lingue e monete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si DEVONO utilizzare per le codifiche standard indicate nelle Linee
Guida per la Valorizzazione del Patrimonio Informativo Nazionale [1]_,
inclusi:

-  ISO 3166-1-alpha2 country (due lettere)

-  ISO 639-1 language code

-  ISO 639-1 per le varianti dei linguaggi.

-  ISO 4217 alpha-3 currency codes

Per le valute è possibile basarsi sullo schema Money - ripreso dal
lavoro di standardizzazione del Berlin Group sotto l’egida dello
European Standards e contenente i campi:

-  amount (string)

-  currency [ISO-4217]

Esempio:

.. code-block:: python

	{
		"tax_id": "imu-e472",
		"value": {
			"amount": "100.23",
			"currency": "EUR"
		}
	}


.. code-block:: xml

   <payment>
	   <taxId>imu-e472</taxId>
	   <value>
		   <currency>EUR</currency>
		   <amount>100.23</amount>
	   </value>
   </payment>

.. [1]
   Cfr.
   https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/bozza/index.html

.. forum_italia::
   :topic_id: 21488
   :scope: document
