print("welcome to our showroom")
b=input("choose your bike")
if(b=='hero'):
    print("choose the req cc")
    cc=input()
    if(cc=='150'):
        c=input("enter your colour")
        if(c=='black' or c=='green' or c=='red'):
            print("bike in",c,"with cc",cc,"is available")
        else:
            print("Sorry!..colour is not available,The available colours are green,black and red")
    elif(cc=='200'):
        c=input("enter colour")
        if(c=='yellow' or c=='red'):
            print("bike in",c,"with cc",cc,"is available")
        else:
            print("Sorry!...colour is not available.The avalable colours are yellow and red")
    else:
        print("cc is not available.available are 150 and 200")
elif(b=='yamaha'):
    cc=input("choose the cc")
    if (cc=='150'):
        c=input("enter colour")
        if(c=='red'):
            print("bike in",c,"with cc",cc,"is available")
        else:
            print("Sorry!..colour not available.The available colour is only red")
    elif(cc=='200'):
        c=input("enter colour")
        if(c=='blue' or c=='red'):
            print("bike in",c,"with cc",cc,"is available")
        else:
            print("Sorry!..colour not avilable.The available colours are blue and red")
    elif(cc=='600'):
        c=input("enter colour")
        if(c=='white'):
            print("available but currently out of stock")
        else:
            print("Sorry!..colour not available.The available colour is only white but currently out of stock")
    else:
        print("cc not available.only available cc are 150 and 200")
elif(b=='re'):
    cc=input("enter cc")
    if (cc=='500'):
        c=input("enter colour")
        if(c=='bottlegreen'):
            print("available but diesel")
        else:
            print("Sorry!...colour not available.The available colour is bottlegreen(diesel)")
    else:
        print("cc not available,only available are 500")
else:
    print("Sorry!.. bike is not available")
print("How was the experience? Is it good or bad?")
ch=input()
if(ch=='good'):
    print("THANK YOU..VISIT AGAIN (*~*)")
elif(ch=='bad'):
    f=input("please enter your feedback")
    print("THANK YOU FOR THE FEEDBACK *~*")

            