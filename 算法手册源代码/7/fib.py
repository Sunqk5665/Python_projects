def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n<1:
        print('对不起，输入有误!')
        return -1
    else:
        while (n - 2) > 0:
            n3 = n2 + n1
            n1 = n2
            n2 = n3
            n -= 1
    return n3
month = int(input('请输入月数：'))
result = fab(month)
print("%d 个月后的兔子数量为 %d"%(month,result))
