n=int(input("Enter number"))
fact=1
if(n<0):
    print("No factorial")
elif n==0:
    print("Factorial=1")
else:
    for i in range(1, n+1):
        fact*=i
    print("Factorial =", fact)
