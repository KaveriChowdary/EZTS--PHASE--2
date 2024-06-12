class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Person("kaveri","19")
print(obj.name)
print(obj.age)
#polymorphism
#method overriding
class greeting():
    def greet_user(self,name):
        print("to greet user",name)
class india(greeting):
    def greet_user(self,name):
        print("namastey user",name)
class usa(greeting):
    def greet_user(self,name):
        print("welcome user",name)
obj=greeting()
obj1=india()
obj2=usa()
obj.greet_user("hey")
obj1.greet_user("hi")
obj2.greet_user("hello")
#method overloading
'''class vehicle():
    def bike(self,hp,m):
        self.hp=hp
        self.m=m
        print("horse power",hp,"mileage",m)
    def bike(self,hp,m,o):
        self.hp=hp
        self.m=m
        self.o=o
        print("horse poweer",hp,",",o)
obj=vehicle()
obj.bike(120,20)
obj.bike(120,90,9)'''
    