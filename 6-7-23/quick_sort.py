def quicksort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left_a=[i for i in a if i<pivot]
    right_a=[i for i in a if i>pivot]
    return quicksort(left_a)+[pivot]+quicksort(right_a)
a=[5,3,67,55,2,1]
res=quicksort(a)
print(res)