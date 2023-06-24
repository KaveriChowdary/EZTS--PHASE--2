#implementation of single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        nn=Node(data)
        nn.next=self.head
        self.head=nn
    def insertatend(self,data):
        nn=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nn
        nn.next=None
    def insertatloc(self,data,pos):
        nn=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nn.next=temp.next
        temp.next=nn
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
obj=sll()
n1=Node(1)
obj.head=n1
n2=Node(2)
obj.head.next=n2
n3=Node(3)
n2.next=n3
n4=Node(4)
n3.next=n4
n5=Node(5)
n4.next=n5
n6=Node(6)
n5.next=n6
obj.display()
print("\ninserting at begin")
obj.insertatbegin(20)
obj.display()
print("\ninsert at end")
obj.insertatend(30)
obj.display()
print("\ninsert at position")
obj.insertatloc(1000,8)
obj.display()