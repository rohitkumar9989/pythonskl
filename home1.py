#! /usr/bin/python
# -*- coding: utf-8 -*-


# 1. What is mutable? tuple, list, map, set
# a property to alter the object
# The following are some immutable objects:
# int, float, decimal, complex, bool,string,tuple,range,frozenset,bytes
# The following are some mutable objects:
# list,dict,set,bytearray,user-defined classes (unless specifically made immutable)


# 2. What is a different between list and typle
# tuple is immutable, while list is muitable

# 3. Is it valid sentence? 1 <= a < 10 and 1 <= b < 20 -> it is ok
import os
import random
from decimal import Decimal
a = 9
b = 12
if 1 <= a < 10 and 1 <= b < 20:
    print a, b
else:
    print "oops"

# 4.  Where is a mistake here? ->
def chargen():
    # while True:
    for c in '0123456789':
        yield c

words = [c+c for c in chargen()][:10]
print words

# 5.    Please, sort it my name of author. lst = ['Pushkin, Alexander','Tolstoy, Lev','Dostoevsky, Fedor','Gorky, Maxim','Bulgakov, Mikhail','Lermontov, Mikhail','Esenin, Sergei','Tyutchev, Fedor','Turgenev, Ivan']
lst = ['Pushkin, Alexander', 'Tolstoy, Lev', 'Dostoevsky, Fedor', 'Gorky, Maxim','Bulgakov, Mikhail', 'Lermontov, Mikhail', 'Esenin, Sergei', 'Tyutchev, Fedor', 'Turgenev, Ivan']
lst.sort()
print lst

# 6.    Please, sort a list and remove items which interpreted as a False. a = [10,'','a',0,True,[],False,[1,2,3]]
a = [10, '', 'a', 0, True, [], False, [1, 2, 3]]
print a
a.sort()
while False in a:
    a.remove(False)
print a

# 7.    0.7 - 0.6 return 0.09999999999999998. How return correct value?
x = Decimal('0.7')
y = Decimal('0.6')
print x - y

# 8.    Is it palindrome?  A roza upala na lapu Azora.  Please, don't pay on attention on capital letter, spaces
b = "A roza upala na lapu Azora".lower().replace(" ", "")
c = list(b)
if c[::-1] == c:
    print "this string is palindrome:", c

# 9.    Sum of numbers extracted from strings.  W = 'fgmdfklgmdfblkdfmb4i5j34o5i3j53oi45j3kdfgmd fkmgd rkljgma;lgkm ;gmerg;k%#$%#%;lfmdflkm‘
W = 'fgmdfklgmdfblkdfmb4i5j34o5i3j53oi45j3kdfgmd fkmgd rkljgma;lgkm ;gmerg;k%#$%#%;lfmdflkm'
b = list(a)
a = 0
for character in b:
    if str(character).isdigit():
        a += int(character)
# or
print sum(int(i) for i in b if str(i).isdigit())


# 10.    Find a prime numbers a=[1, 13, 21, 17, 9, 73, 66, 31, 19, 134]
a = [1, 13, 21, 17, 9, 73, 66, 31, 19, 134]
for value in a:
    isPrime = True
    if int(value) is 1:
        print value, "is prime"
    else:
        for x in range(1, value):
            # todo: check for negative values
            if value % x == 0 and x != value and x != 1:
                isPrime = False
                break
    if isPrime == True:
        print value, "is prime"
#or
for num in a:
        if all(num%i != 0 for i in range(2, num)):
                print num, "prime second algo"
# 11.    Find all includes sub string in string. A = 'dfskdmdkvmrgoirmdfklmdfdmfbdkfbmdlfbdmflbdmfbdmkflbdkb'  B = "fb"
A = 'dfskdmdkvmrgoirmdfklmdfdmfbdkfbmdlfbdmflbdmfbdmkflbdkb'
B = "fb"
print A.count(B)
# 12.    Find all unique symbols in string.  A = 'gmdkgmdfkgmdfg35345345345kmfgdfgmkdmv ds ;lg #@#$@ dflmdkmsdgm gkmldfbmlbmdflbmfsfefjsnjnsjdnfdk'
A = 'gmdkgmdfkgmdfg35345345345kmfgdfgmkdmv ds ;lg #@#$@ dflmdkmsdgm gkmldfbmlbmdflbmfsfefjsnjnsjdnfdk'
for symbol in A:
    if A.count(symbol) == 1:
        print symbol, "is unique"

# 13.    Find all unique symbols in string and take into account only string symbols. R = "drgm,dog,45o3,453o45,fdbpodf,dpfog,op,4o3p4,5op4k23pofbdF$%#$%@#$fgl,dfbl;,b4332423400123"
R = "drgm,dog,45o3,453o45,fdbpodf,dpfog,op,4o3p4,5op4k23pofbdF$%#$%@#$fgl,dfbl;,b4332423400123"
for symbol in R:
    if R.count(symbol) == 1 and str(symbol).isalpha():
        print symbol, "is unique char"


# 14.    Return a list of symbols appeared in string more 3 and less 10 times. F = ",dfgl,fg45345345mkmfgkdmfgkm$%%#55345,l34,5345l,4l,4353534fdjdfnndsjdnsdjnsdcjsndc"
F = ",dfgl,fg45345345mkmfgkdmfgkm$%%#55345,l34,5345l,4l,4353534fdjdfnndsjdnsdjnsdcjsndc"
result = []
for symbol in F:
    occurence = F.count(symbol)
    if occurence > 3 and occurence < 10 and symbol not in result:
        result.insert(len(result), symbol)
print result

# 15.    Return sorted list for 2 lists. A = [342, 3234, 56, 54345, 44234, 12335434, 345345345353523]   B = [-324234, 32424, 0, 312312, 334]
A = [342, 3234, 56, 54345, 44234, 12335434, 345345345353523]
B = [-324234, 32424, 0, 312312, 334]
C = A + B
C.sort()
print C


# 16    Transpose a rows with columns. initial = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]

# 17.    There are 2 numbers in binary format "0b1010" (decimal 10)   "0b101111" (decimal 47). Find sum and print it as a binary format.
print bin(int("1010", 2) + int("101111", 2))
# 16.    Find a greatest common divisor for numbers 4, 7, 3
results = []
for x in range(1, 7):
    if 4 % x == 0 and 7 % x == 0 and 3 % x == 0:
        results.insert(len(results), x)
results.sort()
print results[-1]

# 18.     Sort a list based on value of key "a" and if it equal then take into account key b.  A = [{"a": 4534234234234, "b": "34fb,flg,sld,b"}, {"a": 324234, "b": "gfldf,gdlfg,df"}]
# A = [{"a": 4534234234234, "b": "34fb,flg,sld,b"}, {"a": 324234, "b": "gfldf,gdlfg,df"}]
# print sorted(A, key = lambda x: (x[1], x[2]))

# 19.     arr = [1,2,3,4,5,6,7,8,9]. What is a list with slice started from 3 to n-1? What is a list for slice [::-2]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print arr[3:-1:1]
print arr[::-2]
# 20.     Please, write down 10 to the power of 3?
print 10**3
# 21.     How to add 3:c to map?    m={'1':'a','2':'b'}
m = {'1': 'a', '2': 'b'}
m['3'] = 'c'
# update
print m

# 22.     What intersection result between s1={1,3,5,7,8} s2=set([2,4,6,8])
s1 = {1, 3, 5, 7, 8}
s2 = set([2, 4, 6, 8])
print s1 & s2
# 23.     6-x digit number. Check if this number is happy number
number = str(322123)
if number == number[::-1]:
    print number, " is a palindrome"

# 24.     Number less 64. Need to check if it is binary palindrome
number = 33
bits = bin(number)
print bits[2:], bits[:1:-1]
if bits[2:] == bits[:1:-1]:
    print bits, " is a palindrome"

# 25.     We have a list ofnumbers. Please print a index's numbers according to index's values from max to min. example a[7,3,8] → 2, 0, 1
a = [7, 3, 8]
b = a[:]
b.sort()
print b, a
for aelement in a:
    print aelement, b.index(aelement)

# 26.     we have a list of numbers. Need to find max and second max and list of items located between max and max2.
a = [7, 3, 8, 78, 12, 22, 111]
b = a[:]
b.sort()
# todo check on length
max = b[-1]
max2 = b[-2]
indexmax = a.index(max)
indexmax2 = a.index(max2)
print max, max2, indexmax, indexmax2
if indexmax > indexmax2:
    print a[indexmax2:indexmax+1]
elif indexmax < indexmax2:
    print a[indexmax:indexmax2+1]
# 27.     We have list of numbers. Need to find sum of numbers of even indexes and sum of numbers of odd indexes
a = [1, 2, 3]
list_o = [x for x in a if x % 2 == 1]  # using list comprehension
list_e = [x for x in a if x % 2 == 0]
print sum(list_o), sum(list_e)

# or even better
print sum(n for n in a if n % 2 == 0)  # using generator
print sum(n for n in a if n % 2 == 1)

# 28.     We have sting with several words. Need return a string with random mixed words.
base = "some words to start with"
splitWords = base.split()
random.shuffle(splitWords)
new = ' '.join(splitWords)
print new

# 29.     we have a file path. Need to find filename without extension
print(os.path.splitext("/tmp/test.txt")[0])
# 30.     Define a function reverse() that computes the reversal of a string. For example, reverse(&quot;I am testing&quot;) should return the string &quot;gnitset ma I&quot;.
a = (r'"I am testing reversing"')
print a, a[::-1]
# 31.     We have sting. Need to find count of symbols A. Need to return dict where key is unique symbols in string and value is count how much this symbols appear in string
a = "some  A words B to start with"
print 'A', 'was counted time(s)', a.count('A')
d = {}
for key in a:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print d

# 32.     We have a list of items belong to file path. Need return full path. example. a=['c:', 'tmp', 'myfile.txt']
a = ['c:', 'tmp', 'myfile.txt']
pathJoined = os.path.join(*a)  # todo check what is splat
print pathJoined


# generate 4 unique ip4 address, dec 1 line


# fibonacci, n!

# function that calculates the calculates times of function execution


# generator ip adress
print m

# 21.     What intersection result between s1={1,3,5,7,8} s2=set([2,4,6,8])
s1 = {1, 3, 5, 7, 8}
s2 = set([2, 4, 6, 8])
print s1 & s2
# 22.     6-x digit number. Check if this number is happy number
number = str(322123)
if number == number[::-1]:
    print number, " is a palindrome"

# 23.     Number less 64. Need to check if it is binary palindrome
number = 33
bits = bin(number)
print bits[2:], bits[:1:-1]
if bits[2:] == bits[:1:-1]:
    print bits, " is a palindrome"

# 24.     We have a list ofnumbers. Please print a index's numbers according to index's values from max to min. example a[7,3,8] → 2, 0, 1
a = [7, 3, 8]
b = a[:]
b.sort()
print b, a
for aelement in a:
    print aelement, b.index(aelement)

# 25.     we have a list of numbers. Need to find max and second max and list of items located between max and max2.
a = [7, 3, 8, 78, 12, 22, 111]
b = a[:]
b.sort()
# todo check on length
max = b[-1]
max2 = b[-2]
indexmax = a.index(max)
indexmax2 = a.index(max2)
print max, max2, indexmax, indexmax2
if indexmax > indexmax2:
    print a[indexmax2:indexmax+1]
elif indexmax < indexmax2:
    print a[indexmax:indexmax2+1]
# 26.     We have list of numbers. Need to find sum of numbers of even indexes and sum of numbers of odd indexes
a = [1, 2, 3]
list_o = [x for x in a if x % 2 == 1]  # using list comprehension
list_e = [x for x in a if x % 2 == 0]
print sum(list_o), sum(list_e)

# or even better
print sum(n for n in a if n % 2 == 0)  # using generator
print sum(n for n in a if n % 2 == 1)

# 27.     We have sting with several words. Need return a string with random mixed words.
base = "some words to start with"
splitWords = base.split()
random.shuffle(splitWords)
new = ' '.join(splitWords)
print new

# 28.     we have a file path. Need to find filename without extension
print(os.path.splitext("/tmp/test.txt")[0])
# 29.     Define a function reverse() that computes the reversal of a string. For example, reverse(&quot;I am testing&quot;) should return the string &quot;gnitset ma I&quot;.
a = (r'"I am testing reversing"')
print a, a[::-1]
# 30.     We have sting. Need to find count of symbols A. Need to return dict where key is unique symbols in string and value is count how much this symbols appear in string
a = "some  A words B to start with"
print 'A', 'was counted time(s)', a.count('A')
d = {}
for key in a:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print d

# 31.     We have a list of items belong to file path. Need return full path. example. a=['c:', 'tmp', 'myfile.txt']
a = ['c:', 'tmp', 'myfile.txt']
pathJoined = os.path.join(*a)  # todo check what is splat
print pathJoined
