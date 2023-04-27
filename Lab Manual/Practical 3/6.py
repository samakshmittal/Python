n=int(input("Enter year"))
if(n%400==0):
    print("Leap year")
else:
    if(n%100==0):
        print("Not leap year")
    elif(n%4==0):
        print("leap year")
    else:
        print("Not leap year")
