count=0 
for i in range(1,101,1): 
    if(i%5==0 or i%7==0): 
        print(i) 
        count+=1 
print("Count=", count)
