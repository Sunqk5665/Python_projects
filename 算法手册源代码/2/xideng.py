import numpy as np

line = [[0] * 6] * 5
for i in range(5):
    line[i] = input("请输入第" + str(i) + "行：").split(',')
    # 将line中的元素转换为整型
    line[i] = list(map(int, line[i]))

puzzle = np.array(line)
zero = np.zeros(6)
# 向puzzle中的最上面加入一行0
puzzle = np.insert(puzzle, 0, values=zero, axis=0)
# 向puzzle中的最后一列加入一列0
puzzle = np.insert(puzzle, 6, values=zero, axis=1)
# 向puzzle中的第0列加入一行0
puzzle = np.insert(puzzle, 0, values=zero, axis=1)

b = [[0 for col in range(8)] for row in range(6)]  # 6*8  不要写反
press = np.array(b)


# 或 press=np.zeros((6,8))
def guess():
    for r in range(1, 5):
        for c in range(1, 7):
            # 根据press的第一行和puzzle的第一行，确定press其他行的值
            press[r + 1][c] = (puzzle[r][c] + press[r][c] + press[r - 1][c] + press[r][c - 1] + press[r][c + 1]) % 2
    # 判断所计算的press能否熄灭最后一行的所有灯
    for c in range(1, 7):
        if (press[5][c - 1] + press[5][c] + press[5][c + 1] + press[4][c]) % 2 != puzzle[5][c]:
            return 0
    return 1
    # 枚举第一行按下开关的所有可能性，有2^6个


def enumeration():
    while guess() == 0:
        press[1][1] += 1
        c = 1
        while (press[1][c] > 1):
            press[1][c] = 0
            c += 1
            press[1][c] += 1
        continue


enumeration()
print("灯的初始状态：\n", puzzle[1:6, 1:7])
print("按下结果为：\n", press[1:6, 1:7])