n=int(input("Enter number")) 
s=0 
while n!=0: 
    r=n%10 
    n=int(n/10) 
    s+=r 
print(s)
