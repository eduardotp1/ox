# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys
import screenReceptor

def main():
    PORTA = 12345

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
            result = ""
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                data = data.decode('utf-8')
                result += data
                print("{}".format(data))
                screenReceptor.putText(data)
                if(len(data) <= 0):
                    print("{}".format(result))
                    break

        finally:
            
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    main()

