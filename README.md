# illustrated guide to python3

* list builtins
```python
dir(__builtins__)
```
* object's properties: 
  * identity(location in the memory)
  ```python
  one = '1'
  first = one //give same id
  id(one)
  id(first)
  ```
  * type(str, int, float, list, dict, tuple, function, type)
  ```python
  type(name)
  ```
    * value
* Mutability. mutable: dict, list. Immutable: string, tuple, int, float.
* coercing that is conversion from one type to another
* module, don't use negative signs
```python
-1%3
2
-1%-3
-1
1%-3
-2
```
* backslash 
```python
backslash = '\\'
print(backslash)
\
```
* escape symbols
```python
\\ Backslash
\' Single quote
\" Double quote
\b ASCII Backspace
\n Newline
\t Tab
\u12af Unicode 16 bit
\U12af89bc Unicode 32 bit
\N{SNAKE }Unicode character
\o84 Octal character
\xFF Hex character
```
* formatted string example
```python
"{name}".format(name="A")
"{[name]}".format({'name':"A"})
"{1}{0}".format('Zero','One')
```
* more on formatted strings
```python
:[[fill]align][sign][#][0][width][grouping_option][.precision][type]
```
   * fill - character used to fill in align, space is default
   * align - align output(< left align, > right align,^center, = put padding after sign)
   * sign - for numbers +(show sign on both positive and neg numbers), - - default(only on negative), or space(leading space for positive, sign on negative)
   * \# - prefix integers(0b, 0o, 0x)
   * 0 - enable zero padding
   * width - minimum field width
   * grouping_option - number separator(',' or _)
   * type - type for string or float
* Integers in formatted strings
   * b - binary, c - (unicode character), d - decimal, o - octal, x- hex, X - hex upper case
 * Floats in formatted strings
   * e/E - exponent, lower/upper case e
   * f - fixed point
   * g/G - General, fixed with exponent for large
   * n - with locale-specific separators
   * % multiplies by 100
* more examples
```python
"{:*^12}".format(Ringo)
# ***Ringo****
"{:b}".format(12)
# 1100
```
* f-strings. starting from python 3.6
```python
letter = 'A'
f'Letter is {letter} and {letter.capitalize()} and some calculation {2 **.5:5.3f}'
```
* dir - lists all the attributes of the object passed into it
* Dunder methods start(and end) with '__'
* help provides documentation for the method ```help("a") ```
* pdb, drop into the debugger at any point
```python 
import pdb
pdb.set_trace()
```
* pdb commands
  * h - list help 
  * n - executes next line
  * c - execution till breakpoint
  * w,where,bt - print stack trace
  * u,up - pop up level in the stack
  * d, down - push down a level in the stack
  * l, list - list source code around the current line
* as string is immutable all methods are not changing it, but rather are creating 
* In Python, methods and functions are first-class objects.
* call method on number
```python
(5).conjugate()
#or 
five = 5
five.conjugate()
```
* common string methods 'endswith()', 'find()', 'format()','join()', 'startswith()', 'strip()','lstrip()','rstrip()'
* usually join is faster then + operator
* to find  help on string methods - help('STRINGMETHODS')
* non-empty string -> True
* empty string '' is coerced to false
* zero int 0 coerces to False 
* empty containers(lists, dicts) are coerced to False. They are falsey. Non-empty containers are coerced to true, they are truthy
* None is an instance of NoneType. None is a singleton (Python only has one copy of None in the interpreter). The id for this
value will always be the same.
* 'is' is faster than == and connotes to the programmer that identity is being compared
rather than the value
* There are no multi-line comments
* table of comparison
    * > greater than
    * < 
    * >=
    * <=
    * ==
    * != 
    * is -> identical object (if two objects are the same actual object with the same id)
    * is not -> not identical object
 * The “rich comparison” magic methods, __gt__ , __lt__ , __ge__ , __le__ , __eq__ , and
__ne__ correspond to > , < , >= , <= , == , and != respectively.
*  functools.total_ordering(cls) helps to add absent rich comparison methods
* a range comparison like this:
```python
if 90 < value < 100:
    print('value')
```
* two ways to split statement between several lines
```python
if name == 'George' or \
   name == 'Ringo':
   print(name)
```
```python
if (name == 'George' or
    name == 'Ringo'):
    print(name)
```
* list 
```python
names = list()
names = []
names = ['Data']
names = list(['Data'])
```
* in CPython list is array of pointers, random access, append to end, remove from end is O(1), insert,remove from non-end is O(n). For inserting,removing from non-end collections.deque is better.
* sorting via .sort() method sorts in place, sorted() func -> returns new list
* sorting heterogeneous list gives in Python3 "TypeError: unorderable types"
* .sort method and sorted function allow arbitrary control of sorting by passing in a function for the key parameter.
* ranges in python
```python
range(5) # half open interval
# or 
range(0,10,2)
```
* tuples - immutable sequences
```python
one = tuple([1])
one = (1,)
one = 1,

#several elements
p = tuple(['one'],['two'],['three'])
p = 'one','two','three'
p = ('one','two','three')
```
* note about tuples
```python
d = (3)
type(d) 
# <class 'int'>
d = (3,)
type(d)
#<class 'tuple>
```
* Tuples also use less memory than lists. If you have sequences that you are not mutating, consider using tuples to conserve memory.
* set. unordered collection with unique content. Useful for removing duplicates and checking membership. Lookup is based on hash function. Sets can contain only hashable elements. In python mutable objects are not hashable. You cannot hash list or dict. 
```python
a = set([1,2,3,4,5,6])
a = {1,2,3,4,5,6}
# looking for membership
9 in a
```
* object is hashable when it has methods: ```__hash__``` and ```__eq__```
* contains protocol: if calss implements the ```__container``` methods it is possible to use ```in```
* membership check is quicker in set then in list.
* operations on set
  * union(|) - returns a set composed of both sets
  * intersection(&) - returns items found in both sets
  ```python
  prime = set([2,3])
  prime_even = prime & even
  ```
  * difference(-) - removes items in one set from another
  ```python
  odd = {1,3}
  digits = {1,3,5}
  even = digits - odd
  ```
  * xor(^) - items found only in one set or another, but not both
* enumerate returns a tuple (index, item)
```python
for index,value in enumerate(animals):
    print(index, value)
```
* break - jums out from the nearest loop
* continue - jumps to the next iteration
* index in collection
```python
animals = [1, 2, 3, 4]
1 in animals
animals.index(1)
```
* remove from the list 
```python
# WRONG
for name in names:
    if name not in ['a','b']:
        names.remove(name)
        
# CORRECT n1
names = ['a','b','c']
names_to_remove = []
for name in names:
     if name not in ['a','b']:
         names_to_remove.append(name)
for name in names_to_remove:
     names.remove(name)
     
# CORRECT n2, iterate over copy of a list
names = ['a','b','c']
for name in names[:]: # copy list
     if name not in ['a','b']:
         names.remove(name)
```
* in python 3.6 dictionary's keys are sorted by insertion order
* dictionaries
```python
info = {'first': 'Pete','last':'Greta'}
info = dict([('first','Pete'),('last':'Greta')])
info['first']
```
* accessing non-existing key -> exception
```python
info['medium']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'medium'
```
* dict operator ```in``` 
```python
'first' in info
# True
```
* dict method ```get```(if key is not found, returns the default value)
```python
names =  info.get('first','nobody')
```
* dict method ```setdefault```, same as get, but also adds this key:value pair in dict
* collections.Counter - counts appeareances of key in the dict
```python
import collections
count = collections.Counter(['Ringo'],['John'],['Ringo'])
# Counter({'Ringo': 2, 'Paul': 1, 'John': 1})
```
* ```collections.defaultdict``` = allows for setting the default values of a key to an arbitrary factory. If the default factory is None, it is initialized and inseted as a value any time a key is missing.
* deleting keys(no dict increase,decrease during looping)
```python
del names_to_bands['Ringo']
```
* dictionary method ```keys``` - returns view(a window in current keys found in the dictionary, which is not a copy of the keys.i.e. if to remove the key -> window-view knows about it). Similar are dictionary methods ```values``` and ```items```
* it is possible to have keys of different types. but the key should be hashable
* Classes, namespaces, and modules in Python are all implemented using a dictionary under the covers
* locals and globals
```python
print((locals()))
print((globals()))
```
* Default parameters must be declared after non-default parameters. Otherwise, Python will give  a SyntaxError 
* don't use mutable types(lists, dicts) as default parameters as python are creating them once at function definition time. There is a solution with moving creation of default parameters from definition time, to running time(set defaults to None):
```python
def to_list(value, default = None):   
    if default is None:
        default = []
    # or 
    default = default if default is not None else []
    default.append(value)
    return default
```
* naming conventions for function names(pep8):
  * lowercase
  * have_underscores
  * not start with number
  * not override built-ins
  * not be a keyword
* slicing
```python
numbers = [1,2,3,4,5]
numbers[0:2] # start,amount
# 1,2
numbers[:2] # start from begin
# 1,2
numbers[-1] # last  element
```
* striding slices (each n'th element in slice)
```python
numbers = [1,2,3,4,5]
print(numbers[0:-1:2])
#same as in range
list(range(1,5,2))
```
* revert using slices
```python
'die-hard'[::-1]
```
* file open
```python
open(filename, mode='r',buffering=-1, encoding=None,errors=None, newline=None, closefd=True, opener=None)
```
* for windows paths with theirs ```\``` use r"C:\test"
* open command modes:
  * 'r' - read only
  * 'w' - write(overwrites if exist)
  * 'x' - write(throw FileExistsError if exists)
  * 'a' - append to text file
  * 'rb' - read binary
  * 'wb' - write binary(overrides)
  * 'w+b' - opens bin file for reading and writing
  * 'xb' - same as 'b'
 * reading file
 ```python
 file = open('/etc/passwd')
 file.readline()
 #or 
 file.read()
 # or 
 for line in file.readlines(): #because of __iter__ method
       print(line)
 ```
* reading binary files gives not strings but byte strings.It is possible to read with ```readline```, but need to check for symbol b'\n' to end
* ```close()``` method should be called, or file to be open with ```with```
* to write in file use ```write()``` or ```writelines()``` methods
* to add newline in new file to pass `\n` on Linux, and `\r\n` on Windows or better is to use linesep
```python
import os
os.linesep
```
* file closing
   * if file is in global variable - never be closed during lifetime of program
   * cPython closes garbage collected files(other implementations may not)
   * until .flush is called there is no guarantee that file is written(?)
   * OS has limits on open files per process
   * some OS block deleting open files.
* ```with``` is used with context managers to enforce conditions that occur before and after a block is executed
```python
with open(file,'w') as fout:
    fout.write('Ringo')
#or 
fout = open(file,'w')
fout.write('Ringo')
fout.close()
```
* Unicode is a standart for representing glyphs(the characters that create most of written language, symbols and emoji). It is updated frequently. It has a code points (hexes) that represent glyphs.
```python
print("\N{GRINNING FACE}")
#or 
print("\U0001f600")
#or utf-8 bytestring
print(b"\xf0\x9f\x98\x80".decode('utf8'))
```
* utf8 used from 8 bits to 32 bits, it is backward compatible to ascii
* how to find preferred encoding on machine
```python
import locale
locale.getpreferredencoding(False)
```
* utf8 is  Unicode Transformation Format - 8-bit, ie. it is a format for Unicode.
* python3 strings are unicode strings
* encoding -> encoding unicode to bytestring, decoding - decoding bytestring to unicode
* Unicode strings
```python
"x2"
"x\u00b2"
"x\N{SUPPERSCRIPT TWO}"
```
can be transferred to bytestring ```b"x\xcb\xb2"``` via ```.encode('utf-8')``` and bytestring can be decoded to utf-8 via ```.decode('utf-8')```. Encoding transforms a human-readable representation to abstract representation.  Decoding transforms abstract representation to human readable. 
* if python doesn't support an encoding it will throw UnicodeEncodeError. 
```python
"x\u00b2".encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode character '\xb2' in position 1: ordinal not in range(128)
```
* it possible to ignore unicodeerror or replace unknown symbol with question mark
```python
x_sq.encode('ascii', errors='ignore')
#b'x'
x_sq.encode('ascii', errors='replace')
#b'x?'
```
* python3.6 supports 99 encodings. Mapping is in encodings.aliases.aliases
* When you read a text file, Python will give you Unicode strings. By default, Python will use
the default encoding ( locale.getpreferredencoding(False) ).
```python3
data = open('/tmp/sq.cp949').read() //implicit, nok
data = open('/tmp/sq.cp949', encoding='cp949').read() //explicit, ok
```
* class names in CamelCase
* inspect class ```dir(MyClass)```
* get help on class ```help(MyClass)```
* attribute lookup 1) check instance 2) check class 3) if not found -> AttributeError raised
* variable lookup 1) local scope 2) global scope 3) built-in scope 4) if not found -> NameError raised
* class vs instance
```python
type(str)
<class 'type'>
s = str("s")
type(s)
#<class 'str'>
```
* calling function
```python
chair.load(3)
#same as
Chair.load(chair,3)
```
* __dict__ lists all attributes, dir() is rather to retrieve attributes visible by the variable. Non instance attributes are in class variable ```X.__class___```. 
* kinda show that attribute,method is not for user is to put underscore, e.g. ```._variable```
