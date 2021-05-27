def sequest(alist, item):
    pos=0 #初始查找位置
    found=False   #未找到数据对象
    while pos<len(alist) and not found:  # 列表未结束并且还未找到则一直循环
        if alist[pos] == item:     # 找到匹配对象，返回TRUE
            found=True
        else:       #否则查找位置  + 1
            pos = pos+1
    return found
def main():
    testlist=[1,3,5,6,7,8,9,11,23,44]
    print(sequest(testlist,11))
if __name__=='__main__':
    main()