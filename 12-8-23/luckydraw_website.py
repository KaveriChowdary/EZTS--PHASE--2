print("choose a colour in black,red,blue,pink")
c=input()
print("choose a shape spade,club,diamond,heart")
s=input()
print("choose any number from 1 to 4")
n=int(input())
if(c=='black'  and s=='spade' and n==4):
    print("congrats u won ")
else:
    print("better luck next time")