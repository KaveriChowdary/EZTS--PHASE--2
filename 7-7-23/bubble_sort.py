a=[6,4,56,2,89,99,3]
n=len(a)
for i in range(n-1):
    swap=False  
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            swap=True
            a[j],a[j+1]=a[j+1],a[j]
    if swap==False:
        break
print(a)