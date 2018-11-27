from p2p import *
import threading
import traceback

class Tracker(object):

    def __init__(self, port):
        self.my_port = port
        self.peers = [] # List containing peer_id of each active peer
        self.files = {} # filename : peer_id
        self.lock = threading.Lock()
        self.running = True # State of tracker
        self.actions = {'HELO': self.action_helo,
                        'ADDF': self.action_addf,
                        'QUIT': self.action_quit} # msg_id : action method
    
    def add_peer(self, peer_id):
        self.peers.append(peer_id)
    
    def remove_peer(self, peer_id):
        self.peers.remove(peer_id)
    
    def action_addf(self, peer_id, client, msg_content):
        ''' Add files sent by peer to the files dict '''
        
        pass
    def action_helo(self, peer_id, client, msg_content):
        ''' Helo: Add me to the peers list '''
        self.lock.acquire()
        print(f"Peer {peer_id} connected.")
        # If peer_id not in peers: append peer_id
        if peer_id not in self.peers:
            self.peers.append(peer_id)
            #send ack
        else:
            #send ack already
            pass
        # send acknowladge
        # send error
        self.lock.release()
        print(self.peers)
        

    def action_rqfs(self, peer_id, client, msg_content):
        ''' Request file matching string ''' 
        self.lock.acquire()
        # Check if string in self.files
        # If .. 
        # else: client.send(ERRR)

        self.lock.release()
        pass
    
    def action_quit(self, peer_id, client, msg_content):
        ''' Quit: remove peer form self.peers ''' 
        self.lock.acquire()
        try:
            # remove peer
            self.peers.remove(peer_id)
            # send ACKN
            print(self.peers)
            
        except:
            # client.send(ERRR)
            pass
        finally:
            self.lock.release()
        pass

    def process_client(self, client_socket):
        host, port = client_socket.getpeername()
        peer_id = f"{host}:{port}"
        client = P2PCommunication(client_socket) # TODO
        # Recieve message from client and redirect to corresponing action
        msg_id, msg_content = client.recv()
        print(msg_id, msg_content)
        if msg_id in self.actions:
            self.actions[msg_id](peer_id, client, msg_content)
        
        client.close()

    
    def run(self):
        sock = create_socket('', self.my_port)

        while self.running:
            try:
                # Wait for clients to connect
                cl_sock, cl_addr = sock.accept()
                # When a client connects, create a thread and process it TODO
                # self.process_client(cl_sock)
                thrd = threading.Thread(target = self.process_client, args = [cl_sock] )
                thrd.start()

            except KeyboardInterrupt: # Ctrl + C to stop tracker
                self.running = False
                print("Quitting...")
                continue
            except:
                print("Error")
                traceback.print_exc()
                continue

    











if __name__=='__main__':
    t = Tracker(9999)
    t.run()
