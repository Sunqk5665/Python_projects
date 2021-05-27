a = [56,52,-96,-53,23,-789,520]    #测试案例
b = len(a)                         #列表长度
gap = b // 2                       #初始步长设置为总长度的一半
while gap >= 1:
    for i in range (b):
        j = i
        while j>=gap and a[j-gap] > a[j]:   #在每一组里面进行直接插入排序
            a[j],a[j-gap] = a[j-gap],a[j]
            j-= gap
    gap=gap//2                              #更新步长
print(a)
