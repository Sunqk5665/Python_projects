def GetMac_PM(li):
    li.sort()
    for i in range(len(li)-1,1,-1):
        if li[i-2]+li[i-1] > li[i]:
            return li[i-2]+li[i-1]+li[i]
    return 0


if __name__ == '__main__':
    li = eval(input())
    print()