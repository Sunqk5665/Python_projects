# 列表合并使用“+”，最后一项-1不使用，可以使用 pop() 弹出，
# 最后可以使用 list.sort()排序
s = []
s += [int(i) for i in input().split()]
print(s)
s.pop() # 弹出最后一项“-1”
s += [int(i) for i in input().split()]
s.pop() # 弹出最后一项“-1”
s.sort() # 非降序排序
print(" ".join(str(i) for i in s) if len(s) else 'NULL')

# print(s)