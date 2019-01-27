#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Write function with one attribute which returns a class depends on name attribute.
def functionWithOneAttribute(oneattribute):
    if(oneattribute == "ororo"): return type("ORORORO",(),{})
    elif(oneattribute == "ururu"): return type("URURURU",(),{})
print(functionWithOneAttribute("ororo")) #class is returned
print(functionWithOneAttribute("ororo")()) #instance is created from class returned

# Write Singlton.
class Singletone(object):
    obj = None
    def __new__(cls, *dt, **mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)
        return cls.obj
x = Singletone()
y = Singletone()
if x is y: print("X IS Y")

# Write abstract class.
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        # pass
        print("abstr")
#N = AbstractClassExample() => TypeError: Can't instantiate abstract class AbstractClassExample with abstract methods do_something
class Concrete(AbstractClassExample):
    def do_something(self):
        print("conc")
N = Concrete()
N.do_something()

# Write class/static method which returns list of all methods of class.
from types import FunctionType
import inspect

class Atatata(object):
    def aAA(self):
        print("a() - a simple method")
    @staticmethod
    def methodLister1():
        return [func for func in dir(Atatata) if callable(getattr(Atatata, func))]
    @classmethod
    def methodLister2(cls):
        return [func for func in dir(cls) if callable(getattr(cls, func))]
    @classmethod
    def methodLister3(cls):
        return [x for x, y in cls.__dict__.items() if type(y) == FunctionType] #list only user defined methods
    @classmethod
    def methodLister4(cls):
        return [member for member in (inspect.getmembers(cls, predicate = inspect.isroutine ))]#some more metadata  
    @classmethod
    def attributeLister1(cls):#list attributes(including methods), by the way it lists also inherited stuff
        return (dir(cls))

print(Atatata().methodLister1())
print(Atatata().methodLister2())
print(Atatata().methodLister3())
print(Atatata().methodLister4())
print(Atatata().attributeLister1())

# Write "Fasad" class for 2 other classes.  (https://pl.wikipedia.org/wiki/Fasada_(wzorzec_projektowy))

# Write "Visitor" example.   rus   https://pl.wikipedia.org/wiki/Odwiedzaj%C4%85cy
# Write a fabric method.  example
# Write example with parent (animal) and several children (dog, cat, deer, fish) classes with method "talk". 
