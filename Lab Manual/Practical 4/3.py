a=int(input("Enter number of terms"))
n1, n2=0, 1
count=0
if(a<=0):
    print("Enter positve integer")
elif a==1:
    print("Fibonacci series", n1)
else:
    print("Fibonacci series")
    while count<a:
        print(n1)
        t=n1+n2
        n1=n2
        n2=t
        count+=1
