def max_list(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_list(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max_list([1,2,3,4,5,6]))