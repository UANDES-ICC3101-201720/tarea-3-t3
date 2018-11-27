
Protocolo P2P para compartir archivos
==============================
> Pedro Ricci

[Versión PDF](./Protocolo.pdf)

## Introducción
Este protocolo tiene como objetivo permitir el intercambio de archivos a través de internet (IPv4) por medio de un modelo semi-descentralizado, es decir, no existe una estructura Servidor-Cliente estricta.

## Hosts
Existen dos tipos de host:
- Peer: Hosts que poseen los archivos a compartir. Intercambian archivos entre ellos gracias a la información proporcionado por el Tracker
- Tracker: Host específico central que mantiene una lista de los peers conocidos y los archivos que cada uno de ellos posee. Si un peer solicita un archivo, le entrega la información necesaria para que se contacte con el peer que posee dicho archivo


## Interacciones entre peers
Cada peer posee un identificador único de la forma: ```<ip o hostname>:<puerto>```.
Los peers pueden:
- Conectarse con un tracker
- Desconectarse del tracker
- Solicitar archivos que coincidan con un string al tracker
- Solicitar un archivo a partir de su nombre a otro peer
El tracker puede:
- Mantener una lista de peers
- Mantener una lista de archivos y sus respectivos dueños


![diagram](https://snag.gy/CmQt4o.jpg)

## Mensajes
Se utilizará el protocolo TCP para enviar mensajes entre peers/tracker.
4  Bytes para el identificador de mensaje
Los mensajes posibles son:
De peer a tracker:
- HELO: Peer solicita ser añadido a lista de peer del tracker
- ADDF: Envia la lista de archivos que posee el peer, para ser añadida por el tracker a su listado de pares Nombre-archivo:peer_id
- RQFS: Peer solicita archivo:peer que coincidan con string
- QUIT: Peer avisa a tracker que se va.

De peer a peer:
- REQF: solicita a otro peer que envie el archivo de nombre determinado

Otros:
- ERRR: se produjo un error manejando un mensaje 


## Implementación PoC
- p2p.py: Utilidades que wrappean la librería sockets de python
- peer.py: Clase Peer
- tracker.py Clase Tracker

Al ser solo un PoC tiene varias limitaciónes:
- Los archivos a compartir no deben tener espacios y deben ser pocos, livianos y tener nombres cortos.
- Se utiliza un buffer de 1024












[1]: Descripción oficial del protocolo DHT, implementado sobre UDP http://www.bittorrent.org/beps/bep_0005.html
