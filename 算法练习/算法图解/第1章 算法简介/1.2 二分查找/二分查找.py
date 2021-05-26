def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high)//2    # 向下取整
        guss = lst[mid]
        if guss == item:
            return mid
        if guss > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# print("请输入一串有序数字，以空格分隔：",end="")
# my_list = [int(i) for i in input().split()]
my_list = [int(i) for i in input("请输入一串有序数字，以空格分隔：").split()]  # 将上面两句合并
# my_list = [1,3,5,7,9]
a = int(input("请 输 入 要 二 分 查 找 的 数 字："))
print(binary_search(my_list,a))