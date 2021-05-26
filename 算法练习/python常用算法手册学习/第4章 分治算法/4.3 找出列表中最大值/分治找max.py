# 基本子算法（子问题规模小于等于 2 时）
def get_max(max_list):
    return max(max_list)  # 这里偷个懒！

# 分治法 版本二
def solve2(init_list):
    n = len(init_list)
    if n <= 2:  # 若问题规模小于等于 2，解决
        return get_max(init_list)

    # 分解（子问题规模为 n/2）
    left_list, right_list = init_list[:n // 2], init_list[n // 2:]

    # 递归（树），分治
    left_max, right_max = solve2(left_list), solve2(right_list)

    # 合并
    return get_max([left_max, right_max])

if __name__ == "__main__":
    # 测试数据
    test_list = [12, 2, 23, 45, 67, 3, 2, 4, 45, 63, 24, 23]
    # 求最大值
    print(solve2(test_list))  # 67