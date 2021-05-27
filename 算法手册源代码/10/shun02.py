#coding:utf-8

'''
author:xzfreewind
'''

class SeqList(object):
    def __init__(self,max=10):
        self.max = max      #默认顺序表最多容纳10个元素
        #初始化顺序表数组
        self.num = 0
        self.date = [None] * self.max

    def is_empty(self):     #判定线性表是否为空
        return self.num is 0

    def is_full(self):      #判定线性表是否全满
        return self.num is self.max

    #获取线性表种某一位置的元素
    def __getitem__(self, i):
        if not isinstance(i,int):   #如果i不为int型，则判定输入有误，即Type错误
            raise TypeError
        if 0<= i < self.num:    #如果位置i满足条件，即在元素个数的范围内，则返回相对应的元素值，否则，超出索引，返回IndexError
            return self.date[i]
        else:
            raise IndexError

    #修改线性表种某一位置的元素
    def __setitem__(self, key, value):
        if not isinstance(key,int): #如果key不为int型，则判定输入有误，即Type错误
            raise TypeError
        if 0<= key <self.num:        #如果位置key满足条件，即在元素个数的范围内，则返回相对应的元素值，否则，超出索引，返回IndexError
            self.date[key] = value
        else:
            raise IndexError
    #按值查找元素的位置
    def getLoc(self,value):
        n = 0
        for j in range(self.num):
            if self.date[j] == value:
                return j
        if j == self.num:
            return -1       #如果遍历顺序表还未找到value值相同的元素，则返回-1表示顺序表种没有value值的元素

    #统计线性表中元素的个数
    def Count(self):
        return self.num

    #表末尾插入操作
    def appendLast(self,value):
        if self.num >= self.max:
            print('The list is full')
            return
        else:
            self.date[self.num] = value
            self.num += 1

    #表任意位置插入操作：
    def insert(self,i,value):
        if not isinstance(i,int):
            raise TypeError
        if i < 0 and i > self.num:
            raise IndexError
        for j in range(self.num,i,-1):
            self.date[j] = self.date[j-1]
        self.date[i] = value
        self.num += 1


    #删除某一位置的操作
    def remove(self,i):
        if not isinstance(i,int):
            raise TypeError
        if i < 0 and i >=self.num:
            raise IndexError
        for j in range(i,self.num):
            self.date[j] = self.date[j+1]
        self.num -= 1

    #输出操作
    def printList(self):
        for i in range(0,self.num):
            print(self.date[i])

    #销毁操作
    def destroy(self):
        self.__init__()

