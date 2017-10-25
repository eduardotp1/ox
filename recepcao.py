import socket
import sys
import exemploSocketServer
import threading as trd
import screenReceptor



t = trd.Thread(target=exemploSocketServer.main)
t.daemon = True
t.start

screenReceptor.main()


