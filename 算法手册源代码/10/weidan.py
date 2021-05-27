#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


class LinkedListUnderflow(ValueError):
    pass


class LinkedListUnderflow(ValueError):
    pass
class LList(object):
    def __init__(self):
        self._head = None
        self._num = 0

    #清楚单链表
    def clear(self):
        LList.__init__(self)

    #判断单链表是否为空
    def is_empty(self):
        return self._head is None

    #计算单链表元素的个数 两种方式：遍历列表 或 返回 _num
    def count(self):
        return self._num
        """
        p = self._head
        num = 0
        while p:
            num += 1
            p = p.next
        return num
        """
    def __len__(self):
        p = self._head
        num = 0
        while p:
            num += 1
            p = p.next
        return num

    #表首端插入元素
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self._num += 1

    #删除表首端元素
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        self._num -= 1
        return e

    #表末端插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._num += 1
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)
        self._num += 1

    #删除表末端元素
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        #表中只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            self._num -= 1
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._num -= 1
        return e

    #发现满足条件的第一个表元素
    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
            p = p.next

    #发现满足条件的所有元素
    def filter(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next

    #打印显示
    def printall(self):
        p = self._head
        while p:
            print(p.elem, end="")
            if p.next:
                print(", ",end="")
            p = p.next
        print("")

    #查找某个值，列表有的话返回为True，没有的话返回False
    def search(self, elem):
        p = self._head
        foundelem = False
        while p and not foundelem:
            if p.elem == elem:
                foundelem = True
            else:
                p = p.next
        return foundelem

    #找出元素第一次出现时的位置
    def index(self, elem):
        p = self._head
        num = -1
        found = False
        while p and not found:
            num += 1
            if p.elem == elem:
                found = True
            else:
                p = p.next
        if found:
            return num
        else:
            raise ValueError("%d is not in the list!" % elem)

    #删除第一个出现的elem
    def remove(self, elem):
        p = self._head
        pre = None
        while p:
            if p.elem == elem:
                if not pre:
                    self._head = p.next
                else:
                    pre.next = p.next
                break
            else:
                pre = p
                p = p.next
        self._num -= 1

    #在指定位置插入值
    def insert(self, pos, elem):
        #当值大于count时就默认尾端插入
        if pos >= self.count():
            self.append(elem)
        #其他情况
        elif 0<=pos<self.count():
            p = self._head
            pre = None
            num = -1
            while p:
                num += 1
                if pos == num:
                    if not pre:
                        self._head = LNode(elem, self._head)
                        self._num += 1
                    else:
                        pre.next = LNode(elem,pre.next)
                        self._num += 1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError

    #删除表中第i个元素
    def __delitem__(self, key):
        if key == len(self) - 1:
            #pop_lasy num自减
            self.pop_last()
        elif 0<=key<len(self)-1:
            p = self._head
            pre = None
            num = -1
            while p:
                num += 1
                if num == key:
                    if not pre:
                        self._head = pre.next
                        self._num -= 1
                    else:
                        pre.next = p.next
                        self._num -=1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError

    #根据索引获得该位置的元素
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if 0<=key<len(self):
            p = self._head
            num = -1
            while p:
                num += 1
                if key == num:
                    return p.elem
                else:
                    p = p.next
        else:
            raise IndexError

    # ==
    def __eq__(self, other):
        #两个都为空列表 则相等
        if len(self)==0 and len(other)==0:
            return True
        #两个列表元素个数相等 当每个元素都相等的情况下 两个列表相等
        elif len(self) == len(other):
            for i in range(len(self)):
                if self[i] == other[i]:
                    pass
                else:
                    return False
            #全部遍历完后则两个列表相等
            return True
        #两个列表元素个数不相等 返回Fasle
        else:
            return False
    # !=
    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True
    # >
    def __gt__(self, other):
        l1 = len(self)
        l2 = len(other)
        if not isinstance(other, LList):
            raise TypeError
        # 1.len(self) = len(other)
        if l1 == l2:
            for i in range(l1):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            #遍历完都相等的话说明两个列表相等 所以返回False
            return False
        # 2.len(self) > len(other)
        if l1 > l2:
            for i in range(l2):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            #遍历完后前面的元素全部相等 则列表个数多的一方大
            #if self[l2-1] == other[l2-1]:
            return True
        # 3.len(self) < len(other)
        if l1 < l2:
            for i in range(l1):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            #遍历完后前面的元素全部相等 则列表个数多的一方大
            #if self[l2-1] == other[l2-1]:
            return False
    # <
    def __lt__(self, other):
        #列表相等情况下>会返回False,则<这里判断会返回True,有错误.所以要考虑在==的情况下也为False
        if self.__gt__(other) or self.__eq__(other):
            return False
        else:
            return True
    # >=
    def __ge__(self, other):
        """
        if self.__eq__(other) or self.__gt__(other):
            return True
        else:
            return False
        """
        #大于等于和小于是完全相反的，所以可以依靠小于实现
        if self.__lt__(other):
            return False
        else:
            return True
    # <=
    def __le__(self, other):
        """
        if self.__eq__(other) or self.__lt__(other):
            return True
        else:
            return False
        """
        ##小于等于和大于是完全相反的，所以可以依靠大于实现
        if self.__gt__(other):
            return False
        else:
            return True


#example 大于5返回True的函数
def greater_5(n):
    if n>5:
        return True

    # 根据索引获得该位置的元素
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < len(self):
            p = self._head
            num = -1
            while p:
                num += 1
                if key == num:
                    return p.elem
                else:
                    p = p.next
        else:
            raise IndexError

    # 判断两个列表是否相等 ==
    def __eq__(self, other):
        # 两个都为空列表 则相等
        if len(self) == 0 and len(other) == 0:
            return True
        # 两个列表元素个数相等 当每个元素都相等的情况下 两个列表相等
        elif len(self) == len(other):
            for i in range(len(self)):
                if self[i] == other[i]:
                    pass
                else:
                    return False
            # 全部遍历完后则两个列表相等
            return True
        # 两个列表元素个数不相等 返回Fasle
        else:
            return False

    # 判断两个列表是否不相等 ！=
    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True

    # >
    def __gt__(self, other):
        l1 = len(self)
        l2 = len(other)
        if not isinstance(other, LList):
            raise TypeError
        # 1.len(self) = len(other)
        if l1 == l2:
            for i in range(l1):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            # 遍历完都相等的话说明两个列表相等 所以返回False
            return False
        # 2.len(self) > len(other)
        if l1 > l2:
            for i in range(l2):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            # 遍历完后前面的元素全部相等 则列表个数多的一方大
            # if self[l2-1] == other[l2-1]:
            return True
        # 3.len(self) < len(other)
        if l1 < l2:
            for i in range(l1):
                if self[i] == other[i]:
                    continue
                elif self[i] < other[i]:
                    return False
                else:
                    return True
            # 遍历完后前面的元素全部相等 则列表个数多的一方大
            # if self[l2-1] == other[l2-1]:
            return False

    # <
    def __lt__(self, other):
        # 列表相等情况下>会返回False,则<这里判断会返回True,有错误.所以要考虑在==的情况下也为False
        if self.__gt__(other) or self.__eq__(other):
            return False
        else:
            return True

    # >=
    def __ge__(self, other):
        """
        if self.__eq__(other) or self.__gt__(other):
            return True
        else:
            return False
        """
        # 大于等于和小于是完全相反的，所以可以依靠小于实现
        if self.__lt__(other):
            return False
        else:
            return True

    # <=
    def __le__(self, other):
        """
        if self.__eq__(other) or self.__lt__(other):
            return True
        else:
            return False
        """
        ##小于等于和大于是完全相反的，所以可以依靠大于实现
        if self.__gt__(other):
            return False
        else:
            return True
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    #表头插入
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    #表尾插入
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    #表头删除
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
        #self._rear不变仍然指向最后一个元素

    #表尾删除
    def pop_last(self):
        p = self._head
        if p is None:
            raise LinkedListUnderflow("in pop_last")
        if p.next is None:
            self._head = None
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

if __name__=="__main__":
    mlist1 = LList1()
    mlist1.prepend(98)
    mlist1.printall()

    for i in range(10,20):
        mlist1.append(random.randint(1,20))

    mlist1.printall()

    for i in mlist1.filter(lambda y: y%2 == 0):
        print(i)