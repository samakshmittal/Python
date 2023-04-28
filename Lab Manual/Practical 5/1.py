string=str(input("Enter string"))
count=0
for i in string:
    if(i.isupper()):
        count+=1
print("Number of upper letters are:", count)
