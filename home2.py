#! /usr/bin/python
# -*- coding: utf-8 -*-

#1. Write list/set comprehensions returns 4 random IP4 addresses like this ['192.133.45.99', '23.245.90.77', '78.213.118.145', '232.97.3.67']
from random import choice
print [[".".join(str(choice(range(255))) for i in range(4))][0] for b in range(4)]#todo: remove magic numbers

# 2. Write generator function returns 4 random IP4 addresses like it mentioned above
generator4IPAddresses = ([".".join(str(choice(range(255))) for i in range(4))][0] for b in range(4))#todo: remove magic numbers
for a in generator4IPAddresses: print a
#or
def generator4IPAddressesAnotherTry():
    for i in range(4):  yield ".".join(str(choice(range(255))) for i in range(4))
for a in generator4IPAddressesAnotherTry(): print a

#3. What closure does mean?
#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step
def bigFunction(message):
    print "{} : {}".format(bigFunction.__name__,message)
    def closureFunction():
        print "{} : {}".format(closureFunction.__name__,message)
    closureFunction()
bigFunction("gansta message")

#4. Return list of cube of numbers generated randomly. Please, use functional programming map
def makeNumberCubic(number):
    print number, "to be cubed"
    return number**3
print map(makeNumberCubic, [choice(range(100)) for i in range(5)])
#or
print map(lambda x: x*x*x, [choice(range(100)) for i in range(5)])

#5. Return list of numbers which divided by 7 from list of numbers generated randomly. Please use list comprehensions and functional programming filter + lambda
for a in filter(lambda x: x%7==0, (choice(range(6,40)) for i in range(20)) ): print a, 'filtered'
#or
import random
for a in filter(lambda x: x%7==0, (random.randint(1,40) for i in range(20)) ): print a, 'filtered second algo'

# 6.What is a difference? (i for i in arr) от [i for i in arr]?
#first is generator expression second is a list comprehension

# 7. Write a function returns a Class (not a instance!)
def function():
    return "a Class(not a instance)"
#or
class A:
    pass

def functionReturnClass():
    return A().__class__

#redo!


print functionReturnClass(), type(functionReturnClass())
# 8. Write decorator (benchmark) which evaluate how much time took by decorated function
import time 
def decoratorBenchmarker(func):
    def wrapperBenchmarker(*args,**kwargs):
        t = time.clock()
        func(*args, **kwargs)
        print "{}() took {}s".format(func.__name__, time.clock() - t) 
    return wrapperBenchmarker

@decoratorBenchmarker
def decorated():
    def makeNumberCubic(number):
        number**number
    [a in map(makeNumberCubic, range(1000))]

decorated()

# 9.What result will be printed?
a = []
for i in [1, 2, 3, 4, 5]:
    a.append(lambda: i)
for fn in a:
    print fn()

# 10.Write decorator which will print decorated function name and parameter names and parameter values
import time 
def decoratorNameParameters(func):
    def wrapperBenchmarker(*args,**kwargs):
        func(*args, **kwargs)
        print "{}()".format(func.__name__) 
        for a in args: print a, "parameter"
        for name, value in kwargs.items(): print name, "name", value, "value"
    return wrapperBenchmarker

@decoratorNameParameters
def decoratedParameters(value1, value2, dict):
    def makeNumberCubic(number):
        number**number
    [a in map(makeNumberCubic, range(1000))]
decoratedParameters(1, 2, {'smth': 1})

# 11. Write dict comprehensions  from string generated randomly and where key is a uniq symbol and value is symbol code
import string
randomString = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
d = {k:v for k,v in [(i, ord(i)) for i in set(randomString)] }
#almost proper solution(except non unique symbols):
# d = {symbol: ord(symbol) for symbol in randomString}
# print randomString
# print d


#12. Write generator which go trough file and print string number and position of substring if it has been found in string or None
filename ="home2.py" 
fo = open(filename, "r")
print "Name of the file: ", fo.name
i = 0
for line in fo:
    i+=1
    if "Write" in line: print i,line
    else: print i, None
fo.close()

#13. Write a function returns all combination of all symbols of your name.
import itertools
def allCombinations(word): 
    return list(itertools.permutations(word))
print allCombinations("Se")

#14. Write a function with tag name and uncounted list of parameters returns a string. Example: <a href=”ololo” target=”alala” id=”ululu” class=”elele” custom=”ilili”> </a>
def tagger(tagname,tagvalue, **kwargs):
    return "<{} {}>{}</{}>".format(tagname,"".join({ " {}={}".format(key, value) for key, value in kwargs.iteritems()}),tagvalue,tagname)
print tagger(tagname="a", tagvalue="JustSomeStupidText", href="olololo",id="alalala", smth="tururu", txt="bebebe")