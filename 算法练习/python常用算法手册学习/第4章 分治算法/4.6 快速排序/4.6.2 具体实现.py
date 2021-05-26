def quick_sort(n):
    if len(n) < 2:
        return n
    else:
        pivot = n[0]
        left = [x for x in n[1:] if x > pivot]
        right = [x for x in n[1:] if x > pivot]
    # return quick_sort(left) + [x for x in n if x == n[0]] + quick_sort(right)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5,11,3,5,8,2,6,7,3]))
# a =[5,11,3,5,8,2,6,7,3]
# print(a[0:])