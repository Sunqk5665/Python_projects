def MinSort(arr, row, cloumn):
    if row < 1 or cloumn < 1:
        print("the number of row and column must be greater than 1")
        return
    if cloumn > 2 ** (row - 1):
        print("this row just ", 2 ** (row - 1), "numbers")
        return

    frontRowSum = 0
    CurrentRowSum = 0
    for index in range(0, row - 1):
        CurrentRowSum = 2 ** index  			#当前行的位数
        frontRowSum = frontRowSum + CurrentRowSum  # the number of  digits of all rows
    NodeIndex = frontRowSum + cloumn - 1  		#按行和列在数组中查找节点的位置

    if NodeIndex > len(arr) - 1:
        print("out of this array")
        return

    currentNode = arr[NodeIndex]

    childIndex = NodeIndex * 2 + 1

    print("Current Node:", currentNode)

    if row == 1:
        print("no parent node!")
    else:
        parentIndex = int((NodeIndex - 1) / 2)
        parentNode = arr[parentIndex]
        print("Parent Node:", parentNode)

    if childIndex + 1 > len(arr):
        print("no left child node!")
    else:
        leftChild = arr[childIndex]
        print("Left Child Node:", leftChild)

        if currentNode > leftChild:
            print("swap currentNode and leftChild")
            temp = currentNode
            currentNode = leftChild
            leftChild = temp
            arr[childIndex] = leftChild

    if childIndex + 1 >= len(arr):
        print("no right child node!")
    else:
        rightChild = arr[childIndex + 1]

        print("Right Chile Node:", rightChild)

        if currentNode > rightChild:
            print("swap rightCild and leftChild")
            temp = rightChild
            rightChild = currentNode
            currentNode = temp
            arr[childIndex + 1] = rightChild

    arr[NodeIndex] = currentNode


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 234, 562, 452, 23623, 565, 5, 26]
print("initial array:", arr)
MinSort(arr, 1, 1)
print("result array:", arr)