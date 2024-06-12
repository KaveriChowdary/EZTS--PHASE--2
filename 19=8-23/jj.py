n=int(input())
a=[]
e=[]
o=[]
for i in range(n):
    l=int(input())
    a.append(l)
a=sorted(a)
for i in range(len(a)):
    if(i%2==0):
        e.append(a[i])
    else:
        o.append(a[i])
e=sorted(e)
o=sorted(o)
s=e[-2]+o[1]
print(s)