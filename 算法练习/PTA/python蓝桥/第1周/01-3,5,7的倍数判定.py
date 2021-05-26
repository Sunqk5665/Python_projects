# 编程序实现功能：
# 输入一个整数，判断其是否能同时被3、5、7整除。
# 能被整除则输出“Yes”，否则, 输出“No”。
num = int(input())
if num%3==0 and num%5==0 and num%7==0:
    print('Yes')
else:
    print('No')