def InsertSort(myList):
    # 获取列表长度
    length = len(myList)

    for i in range(1, length):
        # 设置当前值前一个元素的标识
        j = i - 1

        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
        if (myList[i] < myList[j]):
            temp = myList[i]
            myList[i] = myList[j]

            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            j = j - 1
            while j >= 0 and myList[j] > temp:
                myList[j + 1] = myList[j]
                j = j - 1

            # 将临时变量赋值给合适位置
            myList[j + 1] = temp


myList = [49, 38, 65, 97, 76, 13, 27, 49]
InsertSort(myList)
print(myList)