# -*- coding: utf-8 -*-
"""

#功能：实现分块查找算法
#三个函数
#1装饰器，计算函数的运行时间
#2分组，输入每一组的大小，然后计算要分多少组
#3查找函数
"""
import time

continue0 = 0
# 每一组的最大值，开始序号，结尾序号

key = []
start = []
end = []
list_data = []
while 1:
    num_all = input('请输入数字总个数：')
    if num_all.isdigit():  # 判断输入的是否为数字，是则强制转换为int型
        num_all = int(num_all)
        break
for i in range(num_all):
    list_data.append(i)


# 装饰器，计算函数的运行时间
def timer(func):
    def wrapper(*arg, **karg):
        time_0 = time.time()  #
        func(*arg, **karg)  #
        time_1 = time.time()  #
        print('初始时间time_0=', time_0)
        print('结束时间time_1=', time_1)
        print('运行总时间为%f' % (time_1 - time_0))
        return 0

    return wrapper


# 分组，分成n组
@timer
def div_group_func(list_data, long):
    # n 分n组数，list_data输入的数据

    n = num_all // long
    n1 = num_all / long
    if n == n1:
        pass
    else:
        n = n + 1
    print('共分为%d组' % n)
    for i in range(n):
        begin = long * i
        ending = long * (i + 1) - 1
        min_f = list_data[begin]
        start.append(begin)  # 每一组的开始
        end.append(ending)  # 每一组的结尾
        for j in range(1, long):  # 获得最小值
            if (begin + j) < num_all:  # 防止索引超出范围
                if min_f > list_data[begin + j]:
                    min_f = list_data[begin + j]
        key.append(min_f)
    return 0


# 查找函数
# 装饰器解释
# search_func=timer(search_func)，则search_func=wrapper
# search_func(list_data,search,n)=wrapper(list_data,search,n)
@timer  # 等价于 search_func=timer(search_func)
def search_func(list_data, search, long):
    # list_data数据
    # search要搜索的数，
    # n 分组数
    flag = num_all % long
    n = num_all // long
    n1 = num_all / long
    if n == n1:
        pass
    else:
        n = n + 1
    for i in range(n):
        if search >= key[i]:
            if flag == 0:  # 数据整分时
                for j in range(start[i], end[i] + 1):
                    if (j) <= num_all:  # 防止索引超出范围
                        if search == list_data[j]:
                            print('查找成功，您要查找的数在第%d处' % (j + 1))
                            return 0
            else:
                if i < n - 1:
                    for j in range(start[i], end[i] + 1):
                        if search == list_data[j]:
                            print('查找成功，您要查找的数在第%d处' % (j + 1))
                            return 0
                else:
                    for j in range(end[i - 1] + 1, end[i - 1] + 1 + flag):
                        if search == list_data[j]:
                            print('查找成功，您要查找的数在第%d处' % (j + 1))
                            return 0
    else:
        print('查找失败，您查的数不再数据库中！')


while True:
    div_group = input('每一组多少个数')
    if div_group.isdigit():  # 判断输入的是否为数字，是则强制转换为int型
        print('总数据个数为%d' % num_all)
        div_group = int(div_group)
        break

div_group_func(list_data, div_group)
# print('每一组最大值：',key)
# print('每一组的开始序号：',start)
# print('每一组的结尾序号：',end)

# 可以重复查找，输入n退出查找
while True:
    if continue0:  # 第一次运行不执行
        continue_or_break = input('输入n退出，输入其他继续查找')
        if continue_or_break == 'n':
            break
    search = input('请输入要查找的数：')
    if search.isdigit():  # 判断输入的是否为数字，是则强制转换为int型
        search = int(search)
    else:
        print('输入错误请重新输入！')
        continue
    search_func(list_data, search, div_group)
    continue0 = 1
