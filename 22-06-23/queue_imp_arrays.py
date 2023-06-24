#implmentation of stack using arrays
q=[]
def enqueue():
    ele=int(input("enter the element"))
    q.append(ele)
    print(ele,"is added into queue")
def dequeue():
    if not q:
        print("queue is empty")
    else:
        e=q.pop(0)
        print("the removed element is:",e)
def display():
    print("queue is:",q)
while True:
    print("select operation 1.push 2.pop 3.display 4.quit\n")
    ch=int(input())
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("select correct operation")

