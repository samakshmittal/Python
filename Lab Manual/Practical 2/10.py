print("A\t B\t A&B\t A|B\t ~A\t A^B")
for i in range(0,4,1): 
    temp=i
    a=int(i%2)
    temp/=2
    b=int(temp%2)
    print(b,"\t",a,"\t",a&b,"\t", a|b,"\t", ~a,"\t", a^b)
