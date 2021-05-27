def binarySearch(alist, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearch(list, 3))
print(binarySearch(list, 10))