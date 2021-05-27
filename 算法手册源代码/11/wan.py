def approximateNumber(num:int):
    # 函数名已经已经限制了参数类型， 这里就不用做参数类型判断了
    result = []#所有满足条件的结果存到 result 数组中
    for divisor in range(1,num):#遍历 1-1000
        #temp 中存放约数
        temp = []
        for dividend in range(1,divisor):#遍历 1-divisor 求所有约数
            if divisor%dividend==0:#判断是不是约数
                temp.append(dividend)#加入约数数组
        tempSum = sum(temp)#求约数和
        if tempSum == divisor:#判断这个数的约数和  是否等于 这个数
            result.append(tempSum)#得到我们需要的结果，存到数组 result中
    return  result #返回结果

print(approximateNumber(1000))
