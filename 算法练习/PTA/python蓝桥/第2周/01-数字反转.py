# 题设：给出一个 32 位的有符号整数，想请你将整数中的每位上的数字进行反转
num = input()
temp = list(num.replace('-',''))  # 如果是一个负数就去掉“-”
temp.reverse()  # reverse() 函数用于反向列表中元素
s = "".join(temp)
if (-2)**31 <= int(s) <= 2**31-1:
    print(int(s) if int(num)>0 else -1*int(s))
else:
    print(0)
# print(temp)