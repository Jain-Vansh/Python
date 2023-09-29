main_list = []
n = int(input())
for i in range(n):
    for j in range(1):
        secondary_list = []
        name = input()
        secondary_list.append(name)
        marks = float(input())
        secondary_list.append(marks)
    main_list.append(secondary_list)

min = 100
for i in range(n):
    if(main_list[i][1] < min):
        min = main_list[i][1]
second_min = 100
for i in range(n):
    if(min < main_list[i][1] < second_min):
        second_min = main_list[i][1]
answer = []
for i in main_list:
    if(i[1] == second_min):
        answer.append(i[0])
answer = sorted(answer)
for i in answer:
    print(i)