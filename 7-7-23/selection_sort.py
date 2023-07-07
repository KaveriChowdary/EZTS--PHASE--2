a=[5,3,67,55,2,1]
for i in range(len(a)):
    min=i #inittial value
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min=j #finding the min element index
    a[i],a[min]=a[min],a[i]
print(a)
            
        