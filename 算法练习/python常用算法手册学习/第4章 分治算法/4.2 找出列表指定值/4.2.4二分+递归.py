data = [1,3,6,13,56,123,345,1024,3223,6688]
def dichotomy(min,max,d,n):
    '''
    :param min: 有序列表头部索引
    :param max:有序列表尾部索引
    :param d:有序列表
    :param n:需要寻找的元素
    '''
    mid = (min+max)//2
    if mid ==0:
        return 'None'
    elif d[mid]<n:
        print('向右侧找！')
        return dichotomy(mid,max,d,n)
    elif d[mid]>n:
        print('向左侧找！')
        return dichotomy(min,mid,d,n)
    else:
        print('找到了%s'%d[mid])
        return
res = dichotomy(0,len(data),data,56)
print(res)