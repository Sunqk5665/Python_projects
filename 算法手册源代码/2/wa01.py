# -*- coding: utf-8 -*-
"""

题目：小青蛙晚上会踩踏稻田，从而踩倒稻子，农民需要找到造成最大损害的那只青蛙的路径，
已知：每只青蛙总是沿一条直线跳跃稻田，每次跳跃距离相同（因此最少跳3步，才有间距！）
每只青蛙跳跃步长可能不同，方向也可能不同
青蛙每一跳都跳在水稻上，将水稻拍倒
"""

max = 2
RC = input("请输入水稻的行数和列数：").split(' ')

RC = list(map(int, RC))

n = int(input("请输入被踩踏的水稻数目："))
# 输入被踩踏的水稻坐标
plants = [[0, 0]] * n
plant = [0, 0]

for i in range(n):
    plants[i] = input("请输入第" + str(i + 1) + "颗被踩踏的水稻的坐标：").split(' ')
    plants[i] = list(map(int, plants[i]))


def searchpath(secplant, dx, dy):
    plant[0] = secplant[0] + dx
    plant[1] = secplant[1] + dy
    steps = 2
    RC = [6, 7]
    while 1 <= plant[0] <= RC[0] and 1 <= plant[1] <= RC[1]:
        if plant not in plants:
            steps = 0
            break
        plant[0] += dx
        plant[1] += dy
        steps += 1
    return steps


# 将被踩踏的水稻按坐标大小进行排序，先比较 x,若x相等，则比较y
plants = sorted(plants)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        # 选取plants[i]为第一个点，plants[j]为第二个点，求取间距dX 和 dY
        dX = plants[j][0] - plants[i][0]
        dY = plants[j][1] - plants[i][1]
        # 判断选取的第一个的前一个点的坐标是否在稻田里,
        # 若在，说明选取的步长太小，换第二个点再试
        pX = plants[i][0] - dX
        pY = plants[i][1] - dY
        if 1 <= pX <= RC[0] and 1 <= pY <= RC[1]:
            continue
        # 跳跃max步后，判断其在x方向是否过早越界，
        # 其中max是程序实时比较计算出的最大步数
        # 由于plants是排序过的，当这个点越界时，换第二个点时，dX增大，
        # 那么无论怎么换第二个点，都一定越界，因此，换第一个点再试
        if plants[i][0] + (max - 1) * dX > RC[0]:
            break
        # 跳跃max步后，判断其在Y方向是否过早越界，
        # 由于plants是排序过的，换第二个点时，dX增大，但是dY减小
        # 因此，如果越界，则需换第二个点再试
        pY = plants[i][1] + (max - 1) * dY
        if pY > RC[1] or pY < 1:
            continue
        # 走到这步则说明，该条路径不仅符合条件，而且跳跃步数比之前的max要大
        # 因此，计算该条路径的步数
        steps = searchpath(plants[j], dX, dY)
        if steps > max:
            max = steps
    if steps == 2:
        max = 0
print(max)