n=input("Enter your name:\n") 
sap=int(input("Enter your sap id:\n")) 
r=input("Enter your roll no.:\n") 
c=input("Enter your course name:\n") 
sem=int(input("Enter your semester:\n")) 
print("Name:\t\t",n) 
print("Roll no:\t",r) 
print("Sap Id:\t\t",sap) 
print("Semester:\t",sem) 
print("Course Name:\t",c) 
 
PDS=int(input("enter your marks in PDS")) 
Python=int(input("enter your marks in Python")) 
Chemistry=int(input("enter your marks in Chemistry")) 
English=int(input("enter your marks in English")) 
Physics=int(input("enter your marks in Physics")) 
 
print("Subject Name :\t Marks") 
print("PDS :\t\t", PDS) 
print("Python :\t", Python) 
print("Chemistry :\t", Chemistry) 
print("English :\t", English) 
print("Physics :\t", Physics) 
 
percentage=((PDS+Python+Chemistry+English+Physics)/500)*100 
print("Percentage:",percentage,"%") 
CGPA=percentage/10 
print("CGPA:",CGPA) 
if(CGPA>9 and CGPA<=10): 
    print("Grade:O") 
elif(CGPA>8 and CGPA<=9): 
    print("Grade:A+") 
elif(CGPA>7 and CGPA<=8): 
    print("Grade:A") 
elif(CGPA>6 and CGPA<=7): 
    print("Grade:B+") 
elif(CGPA>5 and CGPA<=6): 
    print("Grade:B") 
elif(CGPA>3.5 and CGPA<=5): 
    print("Grade:C+") 
elif(CGPA>0 and CGPA<3.5): 
    print("Grade:F") 
else: 
    print("Invlaid Input")
