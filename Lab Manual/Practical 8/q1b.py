f = open("name.txt", "r")
count=0
for x in f:
    if(x[0]=="a" or x[0]=="e" or x[0]=="i" or x[0]=="o" or x[0]=="u" or x[0]=="A" or x[0]=="E" or x[0]=="I" or x[0]=="O" or x[0]=="U"):
        count+=1
print(count)
f.close()
