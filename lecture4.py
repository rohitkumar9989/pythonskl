#! /usr/bin/python

import hashlib
m = hashlib.md5()
m.update("Turururum")
print m.digest(), m.digest_size, m.block_size


print hashlib.sha224("Pfffff").hexdigest()


import hashlib, binascii
dk = hashlib.pbkdf2_hmac("sha256",  b"password", b"salt", 100000)
print binascii.hexlify(dk)

def get_random_uuid():
    import uuid
    import hashlib
    import os
    l = os.urandom(30).encode('base64')[:-1]
    return hashlib.sha256(l).hexdigest()

print get_random_uuid()