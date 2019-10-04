#! /usr/bin/python
#!/usr/bin/env python

# -*- coding: utf-8 -*-
__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"


null_variable = None
if null_variable is None:
    print('null variable is none')
if null_variable == None:
    print('null variable == none')
    
listAA = [x**2 for x in range(10) if x % 2 == 1]
for x in listAA:
    print "atata", x


listA = [1,2,3,'4']
for element in listA:
    print element, type(element)

dicA = {'1':'one', '2':'two'}
for key,val in dicA.items(): 
    print key, val



setA = set('hello')
setB = {'a', 'b', 'c', 'd', 'e'}
for x in setA :
    print x 
for x in setB :
    print x   

setUnite = setA|setB
for x in setUnite:
    print 'unite', x

setIntersect = setA&setB
for x in setIntersect:
    print 'intersection', x

setDifference = setA-setB
for x in setDifference:
    print 'difference', x

symdiffDifference = setA^setB
for x in symdiffDifference:
    print 'symmetric difference', x

bytearrayA = bytearray("Python", "cp1251")
for element in bytearrayA:
    print "bytearray", element



frozensetA = frozenset((1, 2, 3))
tupple1 = tuple(('a','n','v'))
stringS = 'string'
steingS = "string"
steingS = '''string'''
steingS = """string"""
steingS = "'string'"

#slices
a = [1,3,4,6]
print a[:]
print a[::-1]
a[1:3] = [0,1,2]
print a[:]
del a[:3]
print a[:]


#x = int(raw_input("number"))
x = 1
if x < 0:
    x = 0
    print "neg"
elif x == 0:
    print '0'
else:
    print "STOP"


a,b =0,1
while b < 10:
    print (b)
    a,b = b,a+b


for x in listA[:]:
    print x

for i in range(-1,2):
    print i

for i in range(0,10):
    for x in range(0,i):
        if i > 0:
            break
    else:
        print 'atata',i
    
try:
    x = 10/0
except (ZeroDivisionError, TypeError):
    print "division by zero... wtf?"
# except: 
#     print "some other shit"
else:
    "program cannot be executed because of some problem took place here"

try:
    try:
        x = 10/0
    except ZeroDivisionError:
        print "division by zero"
        raise NameError , "WTF"
except NameError:
    print "boolshit"

a = int('10', base=16)
print a