def diedai(a, b, c, d, X):
    x = X
    if a == 0 and c ** 2 - 4 * b * d < 0:
        print("无解")
    elif a == 0 and b == 0 and c == 0 and d != 0:
        print("无解")
    elif a == 0 and b == 0 and c == 0 and d == 0:
        print("恒等")
    else:
        while abs(a * x * x * x + b * x * x + c * x + d) > 0.000001:
            x = x - (a * x * x * x + b * x * x + c * x + d) / (3 * a * x * x + 2 * b * x + c)
        print("x=%.2f" % x)


a, b, c, d, x = input().split()
diedai(int(a), int(b), int(c), int(d), int(x))