"""
八皇后问题：
回溯算法
"""
# 设置棋盘的大小规模
max_coordinate = 8
# 构建数据结构
# 初始化坐标列表，
# 列表的value为纵坐标值（即棋盘上行数的标记值），
# 列表的index为横坐标值（即棋盘列数标记值）
queen_list = [None] * 8


def show():
    column = 0
    # 对列进行遍历，打印坐标
    while column < max_coordinate:
        print("(%d, %d)" % (column, queen_list[column]), end=" ")
        column += 1
    print("")


# 对第棋盘上第column列的情况进行检查，看看是否能够放置皇后
def check(column):
    column_2 = 0
    # 对比column小的列进行遍历
    while column_2 < column:
        # 如果比column小的列中有和column对应的queen_list的值相等（即在同一行），
        # 或者有二者的行标记之差的绝对值等于列标记之差的情况（即在其对角线上），
        # 则不能放置该皇后
        if (queen_list[column_2] == queen_list[column]) or (
                abs(queen_list[column_2] - queen_list[column]) == column - column_2):
            return False
        column_2 += 1
    # 否则，可以放置该皇后
    return True


# 回溯算法的递归函数主体
# 传入一个初始的横坐标值（即对应棋盘上的列数的标记值）
def put_queen(column):
    row = 0
    #
    # 对棋盘的行进行遍历：0~7行
    while row < max_coordinate:
        # 假设该皇后可以放置在棋盘的第row行，第column列上
        queen_list[column] = row
        # 对第棋盘的column列进行检查，如果满足条件则进行下一列的放置
        if check(column):
            # 如果已至最后一列，则调用显示方法，打印结果，跳出递归
            if column == max_coordinate - 1:
                show()
            else:
                # 如果未至最后一列，则递归调用自身，实现在下一列中放置另一个皇后
                put_queen(column + 1)
        row += 1


def main():
    put_queen(0)
    print("=" * 10)


if __name__ == '__main__':
    main()