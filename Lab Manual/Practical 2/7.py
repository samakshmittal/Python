x=int(input("Enter seconds"))
sec=x%60
x-=sec
minute=x//60
x-=minute
min1=minute%60
minute-=min1
hr=minute/60
print(hr, "Hours", min1, "Minutes", sec, "Seconds")
