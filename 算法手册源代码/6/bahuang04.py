# coding=UTF-8
import random


# 冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i] - nextX) in (0, nextY - i):
            # 表示如果下一个皇后和正在考虑的前一个皇后的水平距离为0或者垂直距离相等，就返回TRUE，否则返回False
            return True
    return False


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 产生当前皇后的位置信息
            # 如果只剩一个皇后没有放置
            if len(state) == num - 1:
                yield (pos,)
            # 否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            # 程序要从前面的皇后得到包含位置信息的元组（元组不可更改）
            # 并要为后面的皇后提供当前皇后的每一种合法的位置信息
            # 所以把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


# 为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))

    for item in queens(8):
        print(item)



if __name__ == "__main__":
    prettyprint(random.choice(list(queens(8))))