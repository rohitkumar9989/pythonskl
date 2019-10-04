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

import threading
import socket

class ClientThread(threading.Thread):

    def __init__(self, socket, address):
        self._socket_ = socket
        self._address_ = address
        threading.Thread.__init__(self)

    def run(self):
        print('Connect from address: ', self._address_)
        data = self._socket_.recv(1024)
        print('received', data)
        self._socket_.send(data)
        self._socket_.close()
        print('Closed connection: ', self._address_)


class TcpServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def run(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.listen(5)
        self._running = True

        print('Server is up')
        while self._running:
            connected_socket, addr = self._sock.accept()
            ClientThread(connected_socket, addr).start()

        def stop(self):
            self._running = False
            self._sock.close()
            print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='0.0.0.0', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()


