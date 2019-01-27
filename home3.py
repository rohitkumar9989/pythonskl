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


class Facade:
    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()

    def operation(self):
        self._subsystem_1.operation1()
        self._subsystem_1.operation2()
        self._subsystem_2.operation1()
        self._subsystem_2.operation2()


class Subsystem1:
    """
    Implement subsystem functionality.
    Handle work assigned by the Facade object.
    Have no knowledge of the facade; that is, they keep no references to
    it.
    """

    def operation1(self):
        pass

    def operation2(self):
        pass


class Subsystem2:
    """
    Implement subsystem functionality.
    Handle work assigned by the Facade object.
    Have no knowledge of the facade; that is, they keep no references to
    it.
    """

    def operation1(self):
        pass

    def operation2(self):
        pass


facade = Facade()
facade.operation()


# Write "Visitor" example. 

import abc
class Element(metaclass=abc.ABCMeta):
    """
    Define an Accept operation that takes a visitor as an argument.
    """

    @abc.abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    """
    Implement an Accept operation that takes a visitor as an argument.
    """

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    """
    Implement an Accept operation that takes a visitor as an argument.
    """

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


class Visitor(metaclass=abc.ABCMeta):
    """
    Declare a Visit operation for each class of ConcreteElement in the
    object structure. The operation's name and signature identifies the
    class that sends the Visit request to the visitor. That lets the
    visitor determine the concrete class of the element being visited.
    Then the visitor can access the element directly through its
    particular interface.
    """

    @abc.abstractmethod
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    @abc.abstractmethod
    def visit_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor1(Visitor):
    """
    Implement each operation declared by Visitor. Each operation
    implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the
    context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure.
    """

    def visit_concrete_element_a(self, concrete_element_a):
        pass

    def visit_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor2(Visitor):
    """
    Implement each operation declared by Visitor. Each operation
    implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the
    context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure.
    """

    def visit_concrete_element_a(self, concrete_element_a):
        pass

    def visit_concrete_element_b(self, concrete_element_b):
        pass


concrete_visitor_1 = ConcreteVisitor1()
concrete_element_a = ConcreteElementA()
concrete_element_a.accept(concrete_visitor_1)



# Write a fabric method.  example
class Creator(metaclass=abc.ABCMeta):
    """
    Declare the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory
    method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object.
    """

    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()


class ConcreteCreator1(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct1.
    """

    def _factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct2.
    """

    def _factory_method(self):
        return ConcreteProduct2()


class Product(metaclass=abc.ABCMeta):
    """
    Define the interface of objects the factory method creates.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProduct1(Product):
    """
    Implement the Product interface.
    """

    def interface(self):
        pass


class ConcreteProduct2(Product):
    """
    Implement the Product interface.
    """

    def interface(self):
        pass


concrete_creator = ConcreteCreator1()
concrete_creator.product.interface()
concrete_creator.some_operation()


# Write example with parent (animal) and several children (dog, cat, deer, fish) classes with method "talk". 
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Bark")
class Cat(Animal):
    def talk(self):
        print("Meow")
class Fish(Animal):
    def talk(self):
        print("*speaks in fish language*")
class Human(Animal):
    def talk(self):
        print("Earth is flat!!!")

concreteAnimal = Dog()
concreteAnimal.talk()
Human().talk()


#FROM HW2
# 7. Write a function returns a Class (not a instance!)
def function():
    return type("class", (), {})

print(function())