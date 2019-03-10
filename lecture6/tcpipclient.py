#!/usr/bin/python3

import socket
import random

class TcpClient:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name

    def run(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((self.host, self.port))
        self._sock.send(bytes(self.name))
        data = self._sock.recv(1024)
        print('received: ', data)
        self._sock.close()

if __name__ == '__main__':
    name = 'Python Client ' + str(random.randrange(1, 1000, 1))
    myclient = TcpClient(host='0.0.0.0', port=5555, name=name)
    myclient.run()