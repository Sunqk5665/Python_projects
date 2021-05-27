def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


list = [2, 3, 1, 4, 5, 6, 0]
print(sequentialSearch(list, 5))
print(sequentialSearch(list, 7))