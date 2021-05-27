def Max(alist):
    pos = 0    #初始位置
    imax=alist[0]  #假设第一个元素是最大值
    while pos < len(alist):   #在列表中循环
        if alist[pos] > imax:  #当前列表的值大于最大值 ，则为最大值
            imax=alist[pos]
        pos = pos+1  #查找位置 +1
    return imax
def Min(alist):
    pos = 0   # 初始位置
    imin = alist[0]   #假设第一个元素是最小值
    for item in alist:  #对于列表中的每一个值
        if item < imin:  #当前的值小于最小的值 则为最小值
            imin = item
    return imin
def main():
    testlist=[2,3,4,5,6,8,34,23,55,234]
    print('最大值是：',Max(testlist))
    print('最小值是：',Min(testlist))
if __name__=='__main__':
    main()