a = 'belong'
b = 'cnblogs'

x = []  # 一个解（长度不固定）xi是b中字符的序号
X = []  # 一组解

best_x = []  # 最佳解
best_len = 0  # 最大子序列长度


# 冲突检测
def conflict(k):
    global n, x, X, a, b, best_len

    # 如果两个字符不相等
    if x[-1] < len(b) and a[k] != b[x[-1]]:
        return True

    # 如果两个字符相等，但是相对于前一个在b中的位置靠前
    if a[k] == b[x[-1]] and (len(x) >= 2 and x[-1] <= x[-2]):
        return True

    # 如果部分解的长度加上后面a剩下的长度，小于等于best_len
    if len(x) + (len(a) - k) < best_len:
        return True

    return False  # 无冲突


# 回溯法（递归版本）
def LCS(k):  # 到达a中的第k个元素
    global x, X, a, b, best_len, best_x
    # print(k, x)
    if k == len(a):  # 超出最尾的元素
        if len(x) > best_len:
            best_len = len(x)
            best_x = x[:]
    else:
        for i in range(len(b) + 1):  # 遍历 状态空间：0~len(b)-1，技巧：人为增加一种状态len(b)，表示改行没有元素选取
            if i == len(b):  # 此状态不放入解x内
                LCS(k + 1)
            else:
                x.append(i)
                if not conflict(k):  # 剪枝
                    LCS(k + 1)
                x.pop()  # 回溯


# 根据一个解x，构造最长子序列lcs
def get_lcs(x):
    global b

    return ''.join([b[i] for i in x])


# 测试
LCS(0)
print(b)
print(best_x)
print(get_lcs(best_x))