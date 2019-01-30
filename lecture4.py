#! /usr/bin/python
import py_compile

import home2

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

def get_sha(s):
    import uuid
    import hashlib
    import os
    return hashlib.sha256(s).hexdigest()

print get_sha("")


#module -> .py 
#package -> folder with __init__.py

#module attributes:
print home2.__name__
print home2.__doc__
print home2.__file__
# print home2.__cached__
print home2.__package__
# print home2.__loader__


#import sound.effects.echo
#sound.effects.echo.echofilter(<input>)
#or
#from sound.effects import echo
#echo.echofilter(<input>)
#or
#from sound.effects.echo import echofilter
#echofilter(<input>)


#import * from <package> -> if __init__,py takes __all__

# from . import echo
#from .. import echo
#from ..Neighbour2ParentDir import something


py_compile("lecture4.py")