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