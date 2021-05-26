num = input().split(',')  # split本身就返回列表，所以不用list()转换
# num.sort(reverse=True)  #从小到大排序
j = 0  # 计数器
print(num)
for i in reversed(num):
    j += 1
    if int(i) <= j:
        break
print(j - 1)
