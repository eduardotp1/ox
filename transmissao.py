import socket
import sys



class Transmissor():
    
    def __init__(self):
        self.msg =""
        # Create a TCP/IP socket
        self.meia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 2468)
        #print >>sys.stderr, 'connecting to %s port %s' % server_address
        self.meia.connect(server_address)
    



    def envia(self):

        try:
    
            msg_bytes = self.msg.encode('utf-8')

            self.meia.sendall(msg_bytes)

            # Look for the response
            amount_received = 0
            amount_expected = len(self.msg)
            
            while amount_received < amount_expected:
                data = self.meia.recv(16)
                amount_received += len(data)
                #print >>sys.stderr, 'received "%s"' % data

        finally:
            #print >>sys.stderr, 'closing socket'
            self.meia.close()



