#! /usr/bin/python

#list comprehensions
print [x**2 for x in range(1,2)]
list1= [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
print [x+y for x,y in zip(list1, list2)]
print {k:v for k,v in enumerate(range(10))}
print dict([(i,chr(65+i)) for i in range(4)])
print [n for n in range(1,3) if n %2 == 0]

#map comprehensions
print [(x,y) for x in range (1,3) for y in range (1,3) if x%y == 0]


#generators
print (x for x in range(10))
sum(n for n in range(1,1000) if n%2 == 0)

#function
def func(x,y=7):
    return x**2 + y**2#returns one value

print func
func = lambda x,y=7: x**2 + y**2

print func
print func

#lambda
func = lambda x,y=7: x**2 + y**2
print func

def parrot(voltage, state='a stiff', action = 'voom', type = 'smth'):
    print action," action"
    print voltage,' voltage'
    print state,' state '
    print type, ' type'
parrot(1000)
parrot(action ='a1', voltage=2934)
parrot('a1','a2','a3')
parrot('a1','a2','a3','a4')

#function takes dictionary
def func111(kind, *args, **keywords):
    print "kind", kind
    for arg in args: print 'arg',arg
    keys = keywords.keys()
    for key in keys: print 'key',key
func111(1,[1,2,2,3], {'1':'2', '1':'3', '2':'4'} ) #doesn't work
func111('atata', 'yoyoyouyo', 'ajhkdfh', t1 = "t1", t2 = "t2") # works

#closure is a function in which there are references to variables that are declared outside of the function(and they are not arguments)
def m(p):
    def s():
        return p
    return s
a = m(2)
print a, type(a)

#higher order built-in functions
#map
def cube(x): return x**3
print map(cube, range(1,11))

list1=[1,2]
list2=[2,2]
map(lambda x,y:x*y, list1, list2)

#filter
numbers = [10, 4, 2, -1]
print filter(lambda x: x < 5, numbers)
#or
print [x for x in numbers if  x < 5]


#reduce
def add(x,y): return x+y
print reduce(add, range(1,11))
#or 
print sum(range(1,11))

print reduce(lambda res,x:res*x, numbers, 1)

#apply
def f(x,y,z, a=None, b=None):
    print x, y, z, a, b

apply(f, [1,2,3], {'a':4, 'b':5})

#iterators
for element in [1, 2, 3]:    print element
for element in (1, 2, 3):    print element
for key in {"1":'22',"23":"222"}:    print key
for char in "123":    print char
it = iter("abc")
print it.next(), it.next(), it.next()#, it.next()

#generator(__iter() and next() are alredy implemented)
def reverse(data):
        for index in range(len(data)-1, -1 , -1):      yield data[index]

for char in reverse('word'):    print char
a  = reverse('iti')
print a.next() , a.next()
a = (i*i for i in range(10));
print a


#decorator
def decorator_bold(decorated_func):
    def inner(symbols2):
        print '<b>'
        decorated_func(symbols2)
        print '</b>'
    return inner

def decorator_italic(decorated_func):
    def inner(symbols1):
        print '<i>'
        decorated_func(symbols1)
        print '</i>'
    return inner

@decorator_italic
@decorator_bold
def word(symbols):
    print "Hello", symbols
word("dupa")
print word

#decorator with parameter
def tag(name):
    def decorator(fun_hello):
        def inner(who):
            print "<%s>" % name
            fun_hello(who)
            print "</%s>" % name
        return inner
    return decorator
    
@tag("tag2")
@tag("tag1")
def hello(who):
    print who
print hello("1")

#decorator wrap
from functools import wraps
def decoratorBoldWrapper(fun_hello):
    @wraps(fun_hello)
    def inner(who):
        print "<b>"
        fun_hello(who)
        print "</b>"
    return inner

@decoratorBoldWrapper
def fun_hello(who):
    print who

fun_hello(1)


def benchmark(func):
    """
    decorator that print time that was spent on processing of decorated function
    """
    import time 
    def wrapper(*args,**kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t 
        return res
    return wrapper

def counter(func):
    def wrapper(*args,**kwargs):
        wrapper.count +=1
        res = func(*args, **kwargs)
        print "{} invoked: {}x".format(func.__name__,wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@benchmark
@counter
def calc():
    i = 0
    for n in range(1,10000000):i+=n


calc()
calc()
calc()