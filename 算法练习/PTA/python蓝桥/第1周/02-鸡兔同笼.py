# 鸡兔同笼问题，从键盘读取脚数，头数，输出鸡数和兔数。
foot = int(input())
head = int(input())
rabbit = (foot-head*2)/2
print("%d\n%d"%(head-rabbit,rabbit))