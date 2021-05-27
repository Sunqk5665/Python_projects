def mergesort(seq):
    mid = len(seq) // 2
    if len(seq) <= 1:
        return seq
    lft = mergesort(seq[:mid])
    rgt = mergesort(seq[mid:])
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    # 返回合并排序后的序列
    return lft + rgt + res

print(mergesort([1,6,12,3,8]))