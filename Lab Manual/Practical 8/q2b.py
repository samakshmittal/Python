f = open("integer.txt", "r")
count=0
sum1=0
for x in f:
    count+=1
    sum1+=int(x)
print(sum1/count)
f.close()
