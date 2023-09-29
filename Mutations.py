def mutate_string(string, position, character):
    l = list(string)
    answer = ""
    for i in range(len(l)):
        if(i == position):
            l[i] = character   
        answer += l[i] 
    return answer