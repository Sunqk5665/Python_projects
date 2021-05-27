a_list = [1, 2, 3, 4, 5, 6]

for t in range(len(a_list)-1):

    for i in range(0, len(a_list)-1):
        tmp = a_list[i]
        if a_list[i] < a_list[i+1]:
            a_list[i] = a_list[i+1]
            a_list[i+1] =tmp

print(a_list)