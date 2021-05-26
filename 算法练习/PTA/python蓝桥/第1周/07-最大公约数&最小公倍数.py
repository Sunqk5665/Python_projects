
a,b = map(int,input().split(","))
if a<b:
    a,b = b,a
lcm = a*b   #辗转相除求最大公约数
gcd = a%b
while(gcd):
    a,b = b,gcd
    gcd = a%b
lcm /= b    # 最小公倍数=两个数的乘积除以最大公约数
print("GCD:%d, LCM:%d"%(b,lcm))