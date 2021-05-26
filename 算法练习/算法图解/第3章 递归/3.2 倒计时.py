def countdown(i):
    print(i)
    if i<=1:    # 基线条件：函数不再调用自己
        return
    else:       # 递归条件：函数调用自己
        countdown(i-1) 

countdown(5)