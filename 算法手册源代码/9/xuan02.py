# 以序号为依据
def Selectionsort1():
    A = [-9, -8, 640, 25, 12, 22, 33, 23, 45, 11, -2, -5, 99, 0]
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):  # 上一个值右边的数组
            if A[min] > A[j]:  # 使min为最小值，遇到比min小的值就赋值于min
                min = j

        A[i], A[min] = A[min], A[i]  # 交换最小值到左边

    print ('Selectionsort1排序后的数组：', A)

# 以数值为依据
def Selectionsort2():
    A = [-9, -8, 640, 25, 12, 22, 33, 23, 45, 11, -2, -5, 99, 0]
    counter = 0  # 记录循环次数和位置
    array = []

    for i in A:
        counter += 1
        for j in A[counter:]:  # 缩小范围
            if i > j:  # 使i为最小值
                i = j

            A.remove(i)
            A.insert(counter - 1, i)
            # 把最小值置于列表左边，避免重复比较

        array.append(i)

    print('Selectionsort2排序后的数组：', array)

Selectionsort1()
Selectionsort2()