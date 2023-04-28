string=str(input("Enter string"))
string1=list(string)
list1=[]
for i in string1:
    if i not in list1:
        list1.append(i)
        count=0
        for j in range(len(string1)):
            if i==string1[j]:
                count+=1
        print(i,count)
