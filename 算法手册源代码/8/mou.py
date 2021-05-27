# 待查找数据集合 value
# 查找的值 key
def linear(value, key):
    # 从头到尾遍历待查找数据
    for i in range(len(value)):
        if value[i] == key:
            # 成功，返回下标值
            return i
    else:
        # 失败，返回-1
        return -1

values = [9, 1,11, 3, 2, 6, 12, 5, 4, 7, 8, 10, 13]
# 查找 7
result = linear(values, 7)
if result == -1:
    print('查找失败')
else:
    print('查找成功，对于下标：',result)
