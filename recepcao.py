import socket
import sys
import threading as trd


class Receptor():
    
    def __init__(self):
        self.recebido = ""


    def serverSocket(self):
        PORTA = 8642

        print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', PORTA)
        print("PORTA {}".format(PORTA))
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)
        
        while True:
            # Wait for a connection
            print("waiting for a connection")
            connection, client_address = sock.accept()

            try:
                print(" connection from {}".format(client_address))
                frase = ""
                fim = ""
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    data = data.decode('utf-8')

                    if data == "}":
                        fim+=data

                    if fim == "}}}}":
                        self.recebido = frase
                        frase = ""
                        fim = ""

                    if data != "}":
                        frase += data
                    print("{}".format(data))
                    if(len(data) <= 0):
                        break

            finally:
                
                # Clean up the connection
                connection.close()




# t = trd.Thread(target=exemploSocketServer.main())
# t.daemon = True
# t.start()

# janela = screenReceptor.chatRecebido()
# janela.comeca()



