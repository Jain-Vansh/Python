#Function to check if leap year

def is_leap(year):
    leap = False
    
    if year%4==0:
        if year%100==0 and year%400==0:
            leap = True
        elif year%100==0 and year%400!=0:
            leap = False
        elif year%100!=0:
            leap = True
        else:
            leap = False
    else:
        leap = False
            
    
    return leap

