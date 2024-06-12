#encapsulation
class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("i am"+self.name)
        print(f"i am {self.age} years old")
obj=student(" sai",21)
obj.m1()