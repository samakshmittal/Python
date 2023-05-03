with open("city.txt", "r") as f:
    x=f.read()
    y=x.split("\n")
    z=[]
    for a in y:
        b=a.split()
        z.append(b)
    for a in z:
        if(float(a[1])>10):
           print(a[0])
