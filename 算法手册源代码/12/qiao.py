def fun(arr, time=0):
    ll = len(arr)
    if ll == 1:
        return arr[0]
    if ll == 2:
        return arr[1] + time
    if ll == 3:
        return arr[0] + arr[1] + arr[2] + time
    x = 2 * arr[0] + arr[-1] + arr[-2]
    y = arr[0] + 2 * arr[1] + arr[-1]
    if x < y:
        return fun(arr[0:ll - 2], time + x)
    else:
        return fun(arr[0:ll - 2], time + y)

arr = [2, 5, 6, 9, 13]
print(fun(arr))
