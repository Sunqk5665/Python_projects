# 子问题算法（子问题规模为 1）
def is_in_list(init_list, el):
    return [False, True][init_list[0] == el]  # 若init_list[0] == el为True，返回True

# 分治法
def solve(init_list, el):
    n = len(init_list)
    if n == 1:  # 若问题规模等于 1，直接解决
        return is_in_list(init_list, el)

    # 分解（子问题规模为 n/2）
    left_list, right_list = init_list[:n // 2], init_list[n // 2:]

    # 递归（树），分治，合并
    res = solve(left_list, el) or solve(right_list, el)

    return res


if __name__ == "__main__":
    # 测试数据
    test_list = [12, 2, 23, 45, 67, 3, 2, 4, 45, 63, 24, 23]
    # 查找
    print(solve(test_list, 45))  # True
    print(solve(test_list, 5))  # False
# print([False,True][True])