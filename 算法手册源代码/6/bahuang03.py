"""
八皇后问题
递归回溯算法
"""


def queen(queen_list, current_column=0):
    for row in range(len(queen_list)):
        # 如果已至最后一列，则打印结果，跳出递归
        if current_column == len(queen_list):
            for i in range(len(queen_list)):
                print("(%d, %d)" % (i, queen_list[i]), end=" ")
            print("")
            return

            # 假设当前列能够放置一个皇后，用queen_list的index记录列标，value记录行标
        # flag为可行性的标记
        queen_list[current_column], flag = row, True
        # 对当前列之前的各列进行遍历
        for column in range(current_column):
            # 排除同行及对角线上的位置，将flag设置为False
            if (queen_list[column] == row) or (abs(row - queen_list[column]) == current_column - column):
                flag = False
                # 只要有一个不满足的条件，就跳出遍历
                break
        # 如果可以放置，则递归调用自身，对下一列进行筛选
        if flag:
            queen(queen_list, current_column + 1)


queen([None] * 8)