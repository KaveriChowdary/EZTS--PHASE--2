class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    #insert a new node at beginning
    def push(self,new):
        nn=node(new)
        nn.next=self.head
        self.head=new
    def detectandremove(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        sp=self.head
        fp=self.head
        while(sp and fp and fp.next):
            sp=sp.next
            fp=fp.next.next
            if sp==fp:
               print("meeting point",sp.data)
               sp=self.head
               while(sp.next !=fp.next):
                  sp=sp.next
                  fp=fp.next
               print("start of loop",fp.next.data)
               fp.next=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
list=ll()
list.head=node(50)
list.head.next=node(20)
list.head.next.next=node(30)
list.head.next.next.next=node(10)
list.head.next.next.next.next=node(70)
extra=node(1)
list.head.next.next.next.next.next=extra
extra.next=list.head.next
list.detectandremove()
print("linked list after removing loop")
list.printlist()