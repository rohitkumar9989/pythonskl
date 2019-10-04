#!/usr/bin/python3

#socket.bind((host,port))       - This method binds address (hostname, port number pair) to socket.
#socket.listen()                - This method sets up and start TCP listener.
#socket.accept()                - This passively accept TCP client connection, waiting until connection arrives (blocking).
#socket.connect((host, port))   - This method actively initiates TCP server connection.

#socket.recv()                  - This method receives TCP message
#socket.send()                  - This method transmits TCP message
#socket.recvfrom()              - This method receives UDP message
#socket.sendto()                - This method transmits UDP message
#socket.close()                 - This method closes socket
#socket.gethostname()           - Returns the hostname.


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345

s.connect((host, port))
print(s.recv(1024))
s.close()