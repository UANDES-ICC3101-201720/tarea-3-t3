import socket

class P2PCommunication(object):
    ''' Socket based communication utility '''
    def __init__(self, socket):
        if socket:
            self.sock = socket
        else:
            # create socket? TODO
            print("no socket")
        
        self.sd = self.sock.makefile('rw',buffering=None)

    def send(self, message):
        self.sock.sendall(message) # TODO
        print("Sent...")
        return True
    
    def recv(self):
        msg_id = self.sd.read(4)
        # Wile to read next bytes TODO
        return (msg_id, 'content')
    
    def close(self):
        self.sock.close()
        self.sd = None # garbage collector
        return True

def create_socket(host, port):
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # TCP/IP Socket
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To make port availible as soon as close()
        sock.bind((host, port))
        sock.listen(5)
        return sock