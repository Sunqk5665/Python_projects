# 要求:编写程序，用于计算有n(1<n<10)个字符串中最长的字符串的长度。前导空格不要计算在内！
# 前导空格不计算在内，输入的时候采用字符串的lstrip()处理左边的字符串，再将长度存储在列表中，
# 求出列表的最大值就是字符串的最大长度
n = int(input())
li = []
for i in range(n):
    s = input()
    li.append(len(s.lstrip()))
print("length={}".format(max(li)))



# n=eval(input())
# a=[]
# b=[]
# for i in range(n):
#     a.append(input().strip())
#     b.append(len(a[i]))
# print('length=',max(b),sep='') # sepPython中sep不是函数，它是print函数的一个参数，
#                                # 用来定义输出数据之间的间隔符号