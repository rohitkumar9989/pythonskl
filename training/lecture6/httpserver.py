#!/usr/bin/python3

import http.server
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello World')

    def do_POST(self):
        if self.path == '/send':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Thanks!')
        else:
            self.send_response(400)

if __name__ == '__main__':
    port = 8082
    server = http.server.HTTPServer(('0.0.0.0',port), MyHandler)
    server.serve_forever()
