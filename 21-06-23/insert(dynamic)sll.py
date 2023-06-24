#implementation of single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.last=None
    def append(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
obj=sll()
n=int(input("how may elements would you like to add"))
for i in range(n):
    data=int(input("enter data items: "))
    obj.append(data)
print("the linked list:",end= ' ')
obj.display()
