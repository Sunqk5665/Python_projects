n = 3 # 3个元素:头、身、腿3个元素各自的状态空间
a = [['帽1', '帽2', '帽3', '帽4'],
['衣1', '衣2', '衣3', '衣4', '衣5'],
['裤1', '裤2', '裤3']]

x = [0]*n # 一个解，长度固定，3元数组
X = [] # 一组解

#冲突检测
def conflict(k):
    return False # 无冲突套用子集树模板

def match(k): # 到达第k个元素
    global n, a, x, X

    if k >= n:  # 超出最尾的元素
        print(x)
        #X.append(x[:]) # 保存（一个解）
    else:
        for i in a[k]: # 直接a[k]，若间接则range(len(a[k]))。 遍历第k个元素的对应的所有选择状态，不同的元素状态数目不同
            x[k] = i
            if not conflict(k): # 剪枝
                match(k+1)

match(0) # 从头（第0个元素）开始