#! /usr/bin/python
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
class Abstract(object):
    pass
# Write class/static method which returns list of all methods of class.
# Write "Fasad" class for 2 other classes.  (https://pl.wikipedia.org/wiki/Fasada_(wzorzec_projektowy))  rus
# Write "Visitor" example.   rus   https://pl.wikipedia.org/wiki/Odwiedzaj%C4%85cy
# Write a fabric method.  example
# Write example with parent (animal) and several children (dog, cat, deer, fish) classes with method "talk". 
