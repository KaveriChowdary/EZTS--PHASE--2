stack=[]
even=[]
odd=[]
n=int(input("enter size"))
def push():
    for i in range(n):
        ele=int(input("enter the element"))
        stack.append(ele)
def display():
    if not stack:
        print("stack is empty")
    else:
        print("select 1.even and 2.odd 3.quit\n")
        ch=int(input())
        if ch==1:
              for i in range(len(stack)):
                    if stack[i]%2==0:
                        even.append(stack[i])
              print(even)
        elif ch==2:
            for i in range(len(stack)):
                    if stack[i]%2!=0:
                        odd.append(stack[i])
            print(odd)
        else:
            print("invalid choice")
while True:
    print("select operation 1.push 2.display 3.quit\n")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        display()
    elif ch==3:
         break
    else:
        print("select correct operation")
           
            
        
