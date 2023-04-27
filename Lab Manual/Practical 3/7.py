day=int(input("Enter day")) 
month=int(input("Enter month")) 
year=int(input("Enter year")) 
print("Day : ", day, "Month : ", month, "Year : ", year) 
if(year%400==0): 
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10): 
        if(day<31): 
            day+=1 
        elif(day==31): 
            day=1 
            month+=1 
        else: 
            print("Invalid input") 
    elif(month == 12): 
        if(day<31): 
            day+=1 
        elif(day==31): 
            day=1 
            month=1 
            year+=1 
        else: 
            print("Invalid input") 
    elif(month == 4 or month == 6 or month == 9 or month == 11): 
        if(day<30): 
            day+=1 
        elif(day==30): 
            day=1 
            month+=1 
        else: 
            print("Invalid input") 
    elif(month == 2): 
        if(day<29): 
            day+=1 
        elif(day==29): 
            day=1 
            month+=1 
        else: 
            print("Invalid input") 
    else: 
        print("Invalid input") 
else: 
    if(year%100!=0 and year%4==0): 
        if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10): 
            if(day<31): 
                day+=1 
            elif(day==31): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        elif(month == 12): 
            if(day<31): 
                day+=1 
            elif(day==31): 
                day=1 
                month=1 
                year+=1 
            else: 
                print("Invalid input") 
        elif(month == 4 or month == 6 or month == 9 or month == 11): 
            if(day<30): 
                day+=1 
            elif(day==30): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        elif(month == 2): 
            if(day<29): 
                day+=1 
            elif(day==29): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        else: 
            print("Invalid input") 
    else: 
        if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10): 
            if(day<31): 
                day+=1 
            elif(day==31): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        elif(month == 12): 
            if(day<31): 
                day+=1 
            elif(day==31): 
                day=1 
                month=1 
                year+=1 
            else: 
                print("Invalid input") 
        elif(month == 4 or month == 6 or month == 9 or month == 11): 
            if(day<30): 
                day+=1 
            elif(day==30): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        elif(month == 2): 
            if(day<28): 
                day+=1 
            elif(day==28): 
                day=1 
                month+=1 
            else: 
                print("Invalid input") 
        else: 
            print("Invalid input") 
print("Day : ", day, "Month : ", month, "Year : ", year)
