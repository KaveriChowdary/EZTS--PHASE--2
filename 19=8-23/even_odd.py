def q1(n):
    n=int(input())
    a=[]
    e=[]
    o=[]
    for i in range(n):
        l=input()
        a.append(l)
    a=a.sorted()
    for i in range(len(a)):
        if(i%2==0):
            e.append(i)
        else:
            o.append(i)
    s=e[n-1]+o[1]
    return s

            
        