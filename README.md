
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
- 
De peer a peer:
- 

- RQLT: (**R**e**q**uest **L**is**t**) Solicitar lista de peers a otro peer
- PING: Obtener respuesta para verificar que un peer aún está vivo
- RQFS `<string>` : (**R**e**q**uest **f**iles matching **s**tring) Solicitar una lista de los archivos que posee el peer destino que hacen match con el string
- RPFL `<# of files> <dict(filename:hash)>`: (**R**es**p**onse **F**ile **l**ist) Respuesta a RQFS. Numero de matches y dichos matches
- RQFH `<hash of wanted file>`: (**R**e**q**est **f**ile of **h**ash) Solicitar a peer el archivo con hash determinado
- TPHF `<peer id> <string>`: (**T**his **p**eer **h**as **f**iles matching string): Un peer puede consultar a los peers en su lista si alguno tiene un archivo con la string e informar al peer que le consultó por dicho string (hay que ver a que profundidad llegar)
- ERRR `<error id>`: (**Err**o**r**) Informar que ocurrió un error (id's por definir)
- ACKN `<message>`: Informar la recepción de los diversos mensajes.


## Conclusión












[1]: Descripción oficial del protocolo DHT, implementado sobre UDP http://www.bittorrent.org/beps/bep_0005.html
