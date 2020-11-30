Sicurezza del canale di trasporto
=================================

Al fine di garantire autenticazione, integrità dei dati e
confidenzialità tra ente fruitore, le comunicazione DEVONO avvenire
tramite protocollo di comunicazione HTTPS (HTTP over TLS). Di seguito
sono elencate i requisiti crittografici minimi per stabilire una
connessione sicura, riguardanti versione del protocollo TLS, cipher
suite.

Versione protocollo
-------------------

La versione minima del protocollo TLS DEVE essere maggiore o uguale a
1.2. Versioni precedenti non DEVONO essere utilizzate.

Cipher suite
------------

Le ciphersuite da utilizzare DEVONO supportare perfect forward secrecy
(PFS). Si raccomanda di utilizzare le seguenti ciphersuite.

+-----------+-----------+-----------+-----------+-----------+-----------+
|           | **Key     |           | **Cifratu | **Mode of | **Hash**  |
|           | agreement |           | ra**      | operati   |           |
|           | and       |           |           | on**      |           |
|           | authentic |           |           |           |           |
|           | ation     |           |           |           |           |
|           | mechanism |           |           |           |           |
|           | s**       |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| TLS\_     | ECDHE_ECD | WITH\_    | AES_128\_ | CBC\_     | SHA256    |
|           | SA\_      |           |           |           |           |
|           |           |           | AES_256\_ | GCM\_     | SHA384    |
+-----------+-----------+-----------+-----------+-----------+-----------+
| TLS\_     | ECDHE_RSA | WITH\_    | AES_128\_ | CBC\_     | SHA256    |
|           | \_        |           |           |           |           |
|           |           |           | AES_256\_ | GCM\_     | SHA384    |
+-----------+-----------+-----------+-----------+-----------+-----------+
| TLS\_     | DHE_RSA\_ | WITH\_    | AES_128\_ | CBC\_     | SHA256    |
|           |           |           |           |           |           |
|           |           |           | AES_256\_ | GCM\_     | SHA384    |
+-----------+-----------+-----------+-----------+-----------+-----------+
