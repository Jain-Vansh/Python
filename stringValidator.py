if __name__ == '__main__':
    s = input()
    alnum = al = dig = lo = up = 0
    for i in s:
        if(i.isalnum() == True):
            alnum = 1
        if(i.isalpha() == True):
            al = 1
        if(i.isdigit() == True):
            dig = 1
        if(i.islower() == True):
            lo = 1
        if(i.isupper() == True):
            up = 1
    
    if(alnum == 1):
        print("True")
    else:
        print("False")
    if(al == 1):
        print("True")
    else:
        print("False")
    if(dig == 1):
        print("True")
    else:
        print("False")
    if(lo == 1):
        print("True")
    else:
        print("False")
    if(up == 1):
        print("True")
    else:
        print("False")
    
            
