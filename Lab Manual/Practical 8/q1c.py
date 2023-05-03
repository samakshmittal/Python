f = open("name.txt", "r")
count=0
for x in f:
    if(count<len(x)):
        count=len(x)
        a=x
print(a)
f.close()
