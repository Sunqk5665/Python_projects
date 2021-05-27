def binarySearchCur(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchCur(alist[:midpoint],item)
            else:
                return binarySearchCur(alist[midpoint+1:],item)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearchCur(list, 3))
print(binarySearchCur(list, 10))