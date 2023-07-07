a=[5,3,67,55,2,1]
for i in range(1,len(a)):
    j=i
    while a[j-1]>a[j] and j>0:
        a[j-1],a[j]=a[j],a[j-1]
        j-=1
print(a) 