#3.直接插入排序：

def Insert_sort(num_list):
    for i in range(len(num_list)):
        for j in range(0,i):
            if num_list[j] > num_list[i]:
                num_list[i],num_list[j] = num_list[j],num_list[i]
    return num_list
print(Insert_sort(num_list=[77,88,66,50,21,33,100]))

