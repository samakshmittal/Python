n=int(input("Enter any number"))
a=n
r=0
while(n>0):
    num=n%10
    r=r*10+num
    n//=10
if(a==r):
    print(a, "is a palindrome number")
else:
    print(a, "is not a palindrome number")
