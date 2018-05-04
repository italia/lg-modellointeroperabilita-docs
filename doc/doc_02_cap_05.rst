Message Broker
==============

Un message broker è un modulo software che permette l'integrazione asincrona tramite scambio di messaggi. Questo tipo di interazione è fortemente disaccoppiata perché l'invio del messaggio avviene su un canale in cui è responsabilità del message broker consegnare il messaggio ai soggetti interessati. Il compito del message broker non è però solo quello di passare dati, in quanto esso si occupa anche di aspetti legati alla sicurezza, priorità dei messaggi, inoltro ordinato.

I middleware focalizzati sul fornire integrazione basata su messaggi vengono detti Message Oriented Middleware - MOM.

Un message broker supporta solitamente diverse modalità di interazione:

-   Publish/Subscribe. In questo scenario un publisher invia dei messaggi sul canale ed il message broker li invia a diversi ricevitori sulla base di sottoscrizioni. Questo tipo di interazione supporta diversi scenari tra cui uno a molti o molti a molti;

-   Queuing. In questo caso un richiedente invia una richiesta su una coda specifica (corrispondente all'erogatore) e l'erogatore invia la risposta sulla medesima coda; di fatto è una realizzazione asincrona della modalità request/reply;

-   Store/Forward. In questo caso il broker memorizza i messaggi e quindi inoltra agli interessati.

Un caso particolare di message broker è costituito dagli integration broker. Rispetto ad un message broker, questi si occupano anche della trasformazione di messaggi dai formati sorgente a quelli manipolabili dai riceventi/sottoscrittori.

L'utilizzo di message broker è consigliato in alcuni casi d'uso in cui l'interazione è asincrona o di tipo publish/subscribe (ad es., Internet-of-Things - IoT, aggregatori di dati pubblici).

Varie tecnologie e realizzazioni di message broker hanno storicamente supportato svariati protocolli quali STOMP [80]_, XMPP [81]_, MQTT [82]_, OpenWire [83]_ e AMPQ [84]_. 

.. [80] Cf. `https://stomp.github.io/ <https://stomp.github.io/>`_

.. [81] Cf. `https://xmpp.org/ <https://xmpp.org/>`_

.. [82] Cf. `http://mqtt.org/ <http://mqtt.org/>`_

.. [83] Cf. `http://activemq.apache.org/openwire.html <http://activemq.apache.org/openwire.html>`_

.. [84] Cf. `https://www.amqp.org/ <https://www.amqp.org/>`_