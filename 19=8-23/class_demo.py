class A:
    def m1(self):
        print("methid m1 in class A")
    def m2(self):
        print("methid m2 in classA")
obj=A()
obj.m1()
obj.m2()
#single inheritance
print("\n")
class B:
    def m1(self):
        print("method m1 in class B")
    def m2(self):
        print("method m2 in class B")
class C(B):
    def m3(self):
        print("method m3 in class C")
obj=C()
obj.m1()
obj.m2()
obj.m3()
#multi levle inheritance
print("\n")
class D:
    def m1(self):
        print("method m1 in class D")
    def m2(self):
        print("method m2 in class D")
class E(D):
    def m3(self):
        print("method m3 in class E")
class F(E):
    def m4(self):
        print("method m4 in class F")
obj=F()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
#hierarchial inheritance
print("\n")
class H1:
    def m1(self):
        print("method m1 in class H1")
    def m2(self):
        print("method m2 in class H1")
class H2(H1):
    def m3(self):
        print("method m3 in class H2")
class H3(H1):
    def m4(self):
        print("method m4 in class H3")
obj=H2()
obj1=H3()
obj.m1()
obj.m2()
obj.m3()
obj1.m4()
#multiple inheritance
print("\n")
class M1:
    def m1(self):
        print("method m1 in class M1")
    def m2(self):
        print("method m2 in class M1")
class M2():
    def m3(self):
        print("method m3 in class M2")
class M3(M1,M2):
    def m4(self):
        print("method m4 in class M3")
obj=M3()
obj.m1()
obj.m2()
obj.m3()
obj.m4()