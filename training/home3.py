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

# Write "Fasad" class for 2 other classes.
# Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
# Wrap a complicated subsystem with a simpler interface.

class Facade2SecurityCheck:
    def __init__(self):
        self._subsystem_mac = SecurityCheckMAC()
        self._subsystem_dac = SecurityCheckDAC()

    def checkAccessRights(self, file):
        if (self._subsystem_mac.mac_access_file(file) or self._subsystem_mac.mac_access_folder(file) or self._subsystem_dac.dac_access_file(file) or self._subsystem_dac.dac_access_folder(file)):
            print("Security check succeeded. You can change this file.")
        else: 
            print("Security check failed. You have no rights there!")

class SecurityCheckMAC:
    """Implement subsystem functionality. Handle work assigned by the Facade object. Have no knowledge of the facade; that is, they keep no references to it."""
    def mac_access_file(self, file):     return True #todo: implement function
    def mac_access_folder(self, file):   return True #todo: implement function

class SecurityCheckDAC:
    """Implement subsystem functionality. Handle work assigned by the Facade object. Have no knowledge of the facade; that is, they keep no references to it."""
    def dac_access_file(self,file):        return True #todo: implement function
    def dac_access_folder(self, folder):   return True #todo: implement function


securityCheck = Facade2SecurityCheck()
securityCheck.checkAccessRights("vmlinuz-4.15.0-38-generic")


# Write "Visitor" example. 
# - Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
# - The classic technique for recovering lost type information.
# - Do the right thing based on the type of two objects.
# - Double dispatch

class TransportCompany(ABC):
    """Define an Accept operation that takes a visitor as an argument."""
    @abstractmethod
    def accept(self, visitor):  pass

class Cab(TransportCompany):
    """Implement an Accept operation that takes a visitor as an argument."""
    def accept(self, visitor): visitor.visit_cab(self)

class Bus(TransportCompany):
    """Implement an Accept operation that takes a visitor as an argument."""
    def accept(self, visitor):visitor.visit_bus(self)

class Visitor(ABC):
    """Declare a Visit operation for each class of ConcreteElement in the object structure. The operation's name and signature identifies the
    class that sends the Visit request to the visitor. That lets the visitor determine the concrete class of the element being visited.
    Then the visitor can access the element directly through its particular interface."""
    @abstractmethod
    def visit_cab(self, concrete_element_a): pass
    @abstractmethod
    def visit_bus(self, concrete_element_b): pass

class Passenger(Visitor):
    """Implement each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure."""
    def visit_cab(self, concrete_element_a):  print("visits cab")
    def visit_bus(self, concrete_element_b):  print("visits bus")

class GroupOfPassengers(Visitor):
    """Implement each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure."""
    def visit_cab(self, concrete_element_a): print("visits cab")
    def visit_bus(self, concrete_element_b): print("visits bus")

passenger = Passenger()
passengersGroup = GroupOfPassengers()
cab= Cab()
cab.accept(passenger)
bus = Bus()
bus.accept(passengersGroup)


 # Write a fabric method.
# Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
# Defining a "virtual" constructor.
# The new operator considered harmful.
class Creator(ABC):
    """Declare the factory method, which returns an object of type Product.Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object."""
    def __init__(self):self.product = self._factory_method()
    @abstractmethod
    def _factory_method(self):pass
    def product_usage(self):self.product.interface()

class CakeCreator(Creator):
    """Override the factory method to return an instance of a ConcreteProduct1."""
    def _factory_method(self):return Cake()

class SmartphoneCreator(Creator):
    """Override the factory method to return an instance of a ConcreteProduct2."""
    def _factory_method(self):return Smartphone()

class Product(ABC):
    """Define the interface of objects the factory method creates."""
    @abstractmethod
    def interface(self):pass

class Cake(Product):
    """Implement the Product interface."""
    def interface(self):print("throwing cake into face")

class Smartphone(Product):
    """Implement the Product interface. """
    def interface(self):print("setting alarm to 3 AM")

smartphoneCreator = SmartphoneCreator()
smartphoneCreator.product.interface()
smartphoneCreator.product_usage()


# Write example with parent (animal) and several children (dog, cat, deer, fish) classes with method "talk". 
class Animal(ABC):
    @abstractmethod
    def talk(self):pass

class Dog(Animal):
    def talk(self):print("Bark")
class Cat(Animal):
    def talk(self):print("Meow")
class Fish(Animal):
    def talk(self):print("*speaks in fish language*")
class Human(Animal):
    def talk(self):print("Earth is flat!!!")
concreteAnimal = Dog()
concreteAnimal.talk()
Human().talk()



#FROM HW2
# 7. Write a function returns a Class (not a instance!)
def function():
    return type("class", (), {})

print(function())