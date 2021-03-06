from p2p import *
import threading
from os import walk
from time import sleep

class Peer(object):

    def __init__(self, host, port, tracker_id, files_dir='./'):
        self.my_host = host
        self.my_port = port
        self.my_id = f"{host}:{port}"
        self.lock = threading.Lock()
        self.running = True # State of peer
        self.t_host, self.t_port = tracker_id.split(':')
        self.t_port = int(self.t_port)
        self.files_dir = files_dir
        self.files = []

    def populate_files(self):
        self.files.extend(next(walk(self.files_dir))[2]) 

    def connect_tracker(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        s.connect((self.t_host, self.t_port))
        tracker = P2PCommunication(s)
        tracker.send("HELO", "hi")
        sleep(5)
        tracker.send("QUIT", "listado")
        s.close()
        return True

    def run(self):
        # First run
        self.populate_files()
        self.connect_tracker()
        # Loop that listens for connections
        sock = create_socket(self.my_host, self.my_port)

        while self.running:
            try:
                # Wait for clients (tracker / other peer) to connect
                cl_sock, cl_addr = sock.accept()
                # When a client connects, create a thread and process it
                # thrd = threading.Thread( target = self.CHANGE, args = [ ARGS ] )
                # thrd.start()

            except KeyboardInterrupt: # Ctrl + C to stop peer
                self.running = False
                print("Quitting...")
                continue
            except:
                print("Error")
                continue

        sock.close()
        print(f"Peer {self.my_id} says goodbye")







if __name__=='__main__':
    p1 = Peer('localhost', 9997, 'localhost:9999')
    p1.run()
