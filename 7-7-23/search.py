a=[1,2,3,4,5]
n=int(input("enter search element"))
c=0
for i in range(0,len(a)):
    if a[i]==n:
        print("element found at",i)
        c+=1
        break
if c==0:
      print("not found")