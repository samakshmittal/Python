f = open("integer.txt", "r")
count=0
for x in f:
    if(int(x)>100):
        count+=1
print(count)
f.close()
