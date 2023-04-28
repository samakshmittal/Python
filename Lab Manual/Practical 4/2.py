n=int(input("Enter number"))
s=0
a=n
while(a>0):
    b=a%10
    s+=b**3
    a//=10
if n==s:
    print(n, "is armstrong")
else:
    print(n, "is not armstrong")
