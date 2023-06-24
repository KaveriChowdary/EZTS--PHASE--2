#deletion in single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def deletebegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def deleteatpos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
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
print("\ndeleting at begin")
obj.deletebegin()
obj.display()
print("\ndeleting at end")
obj.deleteatend()
obj.display()
print("\n delete at pos")
obj.deleteatpos(3)
obj.display()
