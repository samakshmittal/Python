string=str(input("Enter string"))
count=0
str1=string.lower()
for i in str1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print("Number of upper vowels are:", count)
