s1=input()
s2=input()
s1=s1.replace("","").lower()
s2=s2.replace("","").lower()
#method 1
count=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if(s1[i]==s2[j]):
            count+=1
if (count==len(s1)):
    print("yes")
else:
    print("no")
#method 2
s1=sorted(s1)
s2=sorted(s2)
if(s1==s2):
    print("yes")
else:
    print("no")
