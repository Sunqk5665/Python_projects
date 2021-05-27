for i in range(10000,99999):  #遍历5位数
    for j in range(0,10):   #“算”其实不能是 “0,1,2”，
        if i*j%111111==0:   #当积可以被 111111 整除时
            if len(set(str(i)))==5:  #如果是5个不同的数字。
                if str(j)==str(i)[0]:  #如果乘数与结果的个位相同。
                    print("找到了，数字是 {}".format(i))
