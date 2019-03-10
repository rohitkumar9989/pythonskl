#!/usr/bin/python3

import http.server
import socketserver
import requests

r = requests.get('https://api.github.com/user', auth=('user','pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/1234546789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')