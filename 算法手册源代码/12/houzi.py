def show(n):
    for i in range(1, 6):
        t = (n - 1) / 5
        print('%d. 总数%d个, 第%i只猴吃一个, 拿走%s个。' % (i, n, i, t))
        n = 4 * t

def fun():
    k = 1
    while True:
        t = k
        # 当前猴子拿走tc，吃拿之前总量应为 5 * tc + 1
        # 前个猴子拿走tp，则有 4 * tp = 5 * tc + 1
        for i in range(4):
            t = 5 * t + 1
            if t % 4: break
            t /= 4
        else:
            print(5 * t + 1)

            show(5 * t + 1)
            # 我们只找最小整数解
            break
        k += 1

fun()