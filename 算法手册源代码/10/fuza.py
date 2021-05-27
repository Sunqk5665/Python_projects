#!/usr/bin/env python
# -*- coding:utf-8 -*-

class QueueUnderflow(ValueError):
    pass

#链表节点
class Node(object):
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

#链表实现队列,头部删除和查看O(1),尾部加入O(1)
class LQueue(object):
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    #查看队列中最早进入的元素，不删除
    def peek(self):
        if self.is_empty():
            raise QueueUnderflow
        return self._head.elem

    #将元素elem加入队列，入队
    def enqueue(self, elem):
        p = Node(elem)
        if self.is_empty():
            self._head = p
            self._rear = p
        else:
            self._rear.next = p
            self._rear =p

    #删除队列中最早进入的元素并将其返回，出队
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow
        result = self._head.elem
        self._head = self._head.next
        return result

#顺序表实现队列,头部删除和查看O(1),尾部加入O(n)
class Simple_SQueue(object):
    def __init__(self, init_len = 8):
        self._len = init_len
        self._elems = [None] * init_len
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def is_full(self):
        return self._num == self._len

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._num-1]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        result = self._elems[self._num-1]
        self._num -= 1
        return result

    def enqueue(self,elem):
        if self.is_full():
            self.__extand()
        for i in range(self._num,0,-1):
            self._elems[i] = self._elems[i-1]
        self._elems[0] = elem
        self._num += 1

    def __extand(self):
        old_len = self._len
        self._len *= 2
        new_elems = [None] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[i]
        self._elems = new_elems


#循环顺序表实现队列,头部删除和查看O(1),尾部加入O(1)
class SQueue(object):
    def __init__(self, init_num = 8):
        self._len = init_num
        self._elems = [None] * init_num
        self._head = 0
        self._num  = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow
        result = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return result

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extand()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def __extand(self):
        old_len = self._len
        self._len *= 2
        new_elems = [None] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0



if __name__=="__main__":
    q = SQueue()
    for i in range(8):
        q.enqueue(i)
    #for i in range(8):
    #    print(q.dequeue())
    #print(q._num)
    q.enqueue(8)
    print(q._len)