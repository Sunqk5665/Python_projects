import random
def fun(l):
    count = 0
    a = l.count(0)
    b = a + l.count(1)
    k1 = a
    k2 = len(l) - 1

    # 把第一个区域全部交换成白
    for i in range(a):
        if l[i] == 0:
            continue

        if l[i] == 1:
            while l[k1] != 0: k1 += 1
            k = k1
        elif l[i] == 2:
            while l[k2] != 0: k2 -= 1
            k = k2
        l[k] = l[i]
        l[i] = 0
        count += 1

    # 把第二个区域全部交换成红
    k = len(l) - 1
    for i in range(a, b):
        if l[i] == 2:
            while l[k] != 1: k -= 1
            l[k] = l[i]
            l[i] = 1
            count += 1
    return count

t = [random.choice([0, 1, 2]) for i in range(30)]
print(t)
steps = fun(t)
print(t, steps)
