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
