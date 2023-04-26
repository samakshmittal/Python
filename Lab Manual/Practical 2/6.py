from math import sqrt
x=float(input("enter 1st side"))
y=float(input("enter 2nd side"))
z=float(input("enter 3rd side"))
s=(x+y+z)/2
print("Area is ", sqrt(s*(s-x)*(s-y)*(s-z)))
