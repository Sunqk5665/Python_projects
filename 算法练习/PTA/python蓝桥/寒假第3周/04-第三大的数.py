import sys

def F(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    firstMax = secondMax = thirdMax = -sys.maxsize - 1
    for n in arr:
        if n > firstMax:
            thirdMax = secondMax
            secondMax = firstMax
            firstMax = n
        elif firstMax == n:
            continue
        elif n > secondMax:
            thirdMax = secondMax
            secondMax = n
        elif secondMax == n:
            continue
        elif n > thirdMax:
            thirdMax = n
    return firstMax if thirdMax == -sys.maxsize - 1 else thirdMax

if __name__=="__main__":
    arr = [int(i) for i in input().split()]
    print(F(arr))