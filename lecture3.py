#! /usr/bin/python3
#!/usr/bin/env python
#inheritance
class Person:
    
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname
    
    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        #Person.__init__(self,first, last)
        super().__init__(first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

    def __str__(self):
        #return self.firstname + " " + self.lastname + ", " +  self.staffnumber
        return super().__str__() + ", " +  self.staffnumber

x = Person("A", "1")
y = Employee("B", "2", "3")
print(x.Name())
print(y.GetEmployee())
print(y.Name())
print(x, y)


#properties vs getters/setters
class P:
    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
    @x.getter
    def x(self):
        return self.__x
    @x.deleter
    def x(self):
        self._x = "deleted"

a = P(1)
print (a.x) 

#or 
class D:
    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)

#class vs instance attributes
class A:
    a = "I am a class attribute!"
x = A()
y = A()
print (y.a)
print (x.a)
x.a="Ha ha looser that is not a class attribute"
print (y.a)
print (x.a)
A.a="I am still class attribute, and you are a looser"
print (y.a)
print (x.a)
print (A.__dict__)
print (x.__dict__)
print (x.__class__.__dict__)


# static:
# Static methods shouldn't be confused with class methods.
# Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances():
        return Robot.__counter

    @staticmethod
    def RobotInstancesStatic():
        return Robot.__counter

    def RobotInstancesPerInstance(self):
        return self.__counter

z = Robot()
print (Robot.RobotInstances())
r = Robot()
print (Robot.RobotInstances())
#print (z.RobotInstances()) -> it is static 
print (Robot.RobotInstancesStatic())
print (z.RobotInstancesStatic())

#Class Methods
class Tobot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def TobotInstances(cls):
        return cls, Tobot.__counter
print(Tobot.TobotInstances())
x = Tobot()
print(x.TobotInstances())



#create class instance
class Point:
    def __init__(self, x, y, z):
        self.coord = (x,y,z)

    def __repr__(self):
        return "Point (%s, %s, %s)" % self.coord
#using new

class Singleton(object):
    obj = None
    def __new__(cls, *dt, **mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)
        return cls.obj

obj = Singleton()
obj.attr = 12
new_obj = Singleton()
print(new_obj.attr)
print (new_obj is obj)

#inheritance
class Parent(object):
    def isParOrChild(self): return True
    def who(self):          return 'Parent'
class Child(Parent):
    def who(self): return 'Child'

x = Parent()
y = Child()
print(x.who())
print(y.who())

class ChildV2(Parent):
    def __init__(self):
        #old way
        #Parent.__init__(self)
        #or
        #super().__init__(self)
        #or
        super(ChildV2, self).__init__()

a = ChildV2()


# NotImplementedError
class abstobj(object):
    #self for passing class instances
    def abstmeth(self):
       raise NotImplementedError('Method is not implemented. Why are you calling it?')
    def __del__(self):
        pass
#static 
    @staticmethod
    def printStatic():
        print(1)

    @classmethod
    #cls for passing class objects
    def printClass(cls):
        print(2)
try:
    abstobj().abstmeth()
except:
    print('some exception')

abstobj.printStatic()
abstobj.printClass()
a = abstobj()
a.printClass()
a.printStatic()


#magic methods
class AccessCounter(object):
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''
    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)
    def __getattribute__(self, name):
            return "No such attribute... go away"
x = AccessCounter("Fa")
#x.__setattr__('attr1','attr1value')
setattr(x, 'attr1', 'attrvalue1')
print (getattr(x, 'attr1'))


#type create a class on the go
MyClass = type("MyClass", (), {})
print(MyClass)
print(MyClass())