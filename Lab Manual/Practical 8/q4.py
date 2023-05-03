n=int(input("Enter number of test cases"))
i=0
while(i<n):
    try:
        a,b = map(int,input().split())
        print (a/b)
    except ZeroDivisionError as e:
        print ("Error Code: %s" % e)
    except ValueError as e:
        print ("Error Code: %s" % e )
    i+=1
