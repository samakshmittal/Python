a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a>b):
    if(a>c):
        print(a, "is greatest")
    elif(c>a):
        print(c, "is greatest")
    else:
        print("Invalid input")
elif(a<b):
    if(b>c):
        print(b, "is greatest")
    elif(c>b):
        print(c, "is greatest")
    else:
        print("Invalid input")
else:
    print("Invalid input")
