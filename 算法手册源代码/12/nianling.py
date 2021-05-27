def sum(a, k, n):
    s = a
    for i in range(1, n):
        s += a + i * k
    return s

def mul(a, k, n):
    s = a
    for i in range(1, n):
        s *= a + i * k
    return s


for a in range(1, 26 // 4):
    find = False
    k = 1
    while True:
        t = sum(a, k, 4)
        if t >= 26:
            if t == 26 and mul(a, k, 4) == 880:
                find = True
            break
        k += 1
    if find:
        for i in range(20):
            print(a + i * k,)
