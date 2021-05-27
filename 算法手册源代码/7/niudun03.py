import math
from math import sqrt


def check_precision(l, h, p, len1):  # 检查是否达到了精确位
    l = str(l);
    h = str(h)
    if len(l) <= len1 + p or len(h) <= len1 + p:
        return False
    for i in range(len1, p + len1):  # 检查小数点后面的p个数是否相等
        if l[i] != h[i]:  # 当l和h某一位不相等时，说明没有达到精确位
            return False
    return True


def print_result(x, len1, p):
    x = str(x)
    if len(x) - len1 < p:  # 没有达到要求的精度就已经找出根
        s = x[:len1] + "." + x[len1:] + '0' * (p - len(x) + len1)
    else:
        s = x[:len1] + "." + x[len1:len1 + p]
    print(s)


def binary_sqrt(x, p):
    x0 = int(sqrt(x))
    if x0 * x0 == x:  # 完全平方数直接开方，不用继续进行
        print_result(x0, len(str(x0)), p)
        return
    len1 = len(str(x0))  # 找出整数部分的长度
    l = 0;
    h = x
    while (not check_precision(l, h, p, len1)):  # 没有达到精确位，继续循环
        if not l == 0:  # 第一次l=0，h=x时不用乘以10，直接取中间值
            h = h * 10  # l,h每次扩大10倍
            l = l * 10
            x = x * 100  # x每次要扩大100倍，因为平方
        m = (l + h) // 2
        if m * m == x:
            return print_result(m, len1, p)
        elif m * m > x:
            h = m
        else:
            l = m
    return print_result(l, len1, p)  # 当达到了要求的精度，直接返回l


# 牛顿迭代法求平方根
def newton_sqrt(x, p):
    x0 = int(sqrt(x))
    if x0 * x0 == x:  # 完全平方数直接开方，不用继续进行
        print_result(x0, len(str(x0)), p)
        return
    len1 = len(str(x0))  # 找出整数部分的长度
    g = 1;
    q = x // g;
    g = (g + q) // 2
    while (not check_precision(g, q, p, len1)):
        x = x * 100
        g = g * 10
        q = x // g  # 求商
        g = (g + q) // 2  # 更新猜测值为猜测值和商的中间值
    return print_result(g, len1, p)


while True:
    x = int(input("请输入待开方数："))
    p = int(input("请输入精度："))
    print("binary_sqrt:", end="")
    binary_sqrt(x, p)
    print("newton_sqrt:", end="")
    newton_sqrt(x, p)


