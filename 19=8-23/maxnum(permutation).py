#find the largest num that we get when we arrange the given array of numbers
a=[54,546,548,60]
def max_per(a):
    a_s=[str(num) for num in a]
    a_s.sort(reverse=True,key=lambda x:x*3)
    max_num=''.join(a_s)
    return max_num
print(max_per(a))


