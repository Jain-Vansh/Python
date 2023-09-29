def swap_case(s):
    answer = ""
    for i in s:
        if(i.islower()):
            i=i.upper()
            answer+=i
        elif(i.isupper()):
            i=i.lower()
            answer+=i
        else:
            answer+=i
    return answer