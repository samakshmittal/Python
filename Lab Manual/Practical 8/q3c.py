with open("city.txt", "r") as f:
    x=f.read()
    y=x.split("\n")
    z=[]
    for a in y:
        b=a.split()
        z.append(b)
    s=0
    for a in z:
        s+=float(a[2])
    print(s)
