#stack implementation using linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head =node(data)
        else:
            nn=node(data)
            nn.next=self.head
            self.head=nn
    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            popped=sel'f.head.data
            self.head=self.head.next
            print("the popped element is",popped)
            return popped
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
obj=stack()
while True:
    print("\nselect operation 1.push 2.pop 3.display 4.quit\n")
    ch=int(input())
    if ch==1:
        print("enter element to push")
        m=int(input())
        obj.push(m)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("invalid choice")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    