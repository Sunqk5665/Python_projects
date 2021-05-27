def ordersequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found
list = [1,2,3,4,5,6,7]
print(ordersequentialSearch(list,3))
print(ordersequentialSearch(list,9))