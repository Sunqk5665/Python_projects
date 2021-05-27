# 分块查找是对顺序查找、二分查找的综合优化，性能介于两者之间
import random

Range = 20
Length = 9
flag = 0
pos = -1
tabNum = 3
tabPos = -1

list = random.sample(range(Range), Length)
goal = random.randint(0, Range)
print('开始查找数字', goal, ', 在下面的列表中查找:')

# 子表建立,选择序列前m个元素排序后建立索引，根据索引建立子表
list_index = []  # 使用二维列表表示多个子序列
for i in range(tabNum):  # 在列表中添加m个列表
    list_index.append([])

for i in range(1, tabNum):  # 向第1-m子列表添加原序列的前m-1个元素作为索引，留出第一个子列表盛放最大索引，
    list_index[i].append(list[i - 1])  # 但会出现最大值在第二个子列表中，第一子列表为空的情况
for i in range(1, tabNum - 1):  # 将添加元素的子列表中的元素降序排列
    for j in range(1, tabNum - i):
        if list_index[j] < list_index[j + 1]:
            list_index[j], list_index[j + 1] = list_index[j + 1], list_index[j]
# print(list_index)

for i in range(tabNum - 1, Length):  # 将其余元素添加到各子列表，比索引大则放到前一个子列表中，其余放入最后一个索引中
    for j in range(1, tabNum):
        if list[i] > list_index[j][0]:
            list_index[j - 1].append(list[i])
            break
    else:
        list_index[tabNum - 1].append(list[i])
# print(list_index)
if len(list_index[0]) > 1:  # 提取第一个子列表的最大值最为索引
    for i in range(len(list_index[0]) - 1, 0, -1):
        if list_index[0][i] > list_index[0][i - 1]:
            list_index[0][i], list_index[0][i - 1] = list_index[0][i - 1], list_index[0][i]
print(list_index)  # 显示构造的子列表

for i in range(tabNum - 1, -1, -1):  # 将给定元素与各子列表进行比较，确定给定元素位置
    if len(list_index[i]) != 0 and goal < list_index[i][0]:
        for j in range(len(list_index[i])):
            if list_index[i][j] == goal:
                tabPos = i + 1
                pos = j + 1
                flag = 1

if flag:
    print("查找结果：在第", tabPos, "个列表的中，索引值是", pos, "！")
else:
    print("not found")
