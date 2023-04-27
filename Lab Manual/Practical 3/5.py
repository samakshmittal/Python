import math 
a=int(input("Enter coefficient of x^2: "))
b=int(input("Enter coefficient of x:")) 
c=int(input("Enter constant value:")) 
discriminant=(b*b)-(4*a*c) 
if(discriminant==0): 
    print("Roots are real and equal") 
    print("Both the roots are",((-b+math.sqrt(discriminant))/2*a)) 
elif(discriminant>0): 
    print("Roots are real and distinct") 
    print("Root 1 is",((-b+math.sqrt(discriminant))/2*a)) 
    print("Root 2 is",((-b-math.sqrt(discriminant))/2*a)) 
elif(discriminant<0): 
    print("Roots are imaginary") 
    print("Root 1 is",(-b/2*a),"+",(math.sqrt(-discriminant))/2*a,"i") 
    print("Root 2 is",(-b/2*a),"-",(math.sqrt(-discriminant))/2*a,"i") 
else: 
    print("Invalid expression")
