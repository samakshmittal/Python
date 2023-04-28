def charcount(a):
    a=a.upper()
    b=[]
    for x in range(len(a)):
        b.append(a[x])
    print(b)
    dict1={}
    c=[]
    for x in b:
        if x not in c:
            count=b.count(x)
            dict1.update({x:count})
            c.append(x)
    for x in dict1:
        print(x,':',dict1[x])
a=str(input("Enter string"))
charcount(a)
