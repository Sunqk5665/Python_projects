import random

def ConfiationAlgorithm(str):
    if len(str) <= 1: #子序列
        return str
    mid = (len(str) // 2)
    left = ConfiationAlgorithm(str[:mid])#递归的切片操作
    right = ConfiationAlgorithm(str[mid:len(str)])
    result = []
    #i,j = 0,0

    while len(left) > 0 and len(right) > 0:
        if (left[0] <= right[0]):
            #result.append(left[0])
            result.append(left.pop(0))
            #i+= 1
        else:
            #result.append(right[0])
            result.append(right.pop(0))
            #j+= 1

    if (len(left) > 0):
        result.extend(ConfiationAlgorithm(left))
    else:
        result.extend(ConfiationAlgorithm(right))
    return result
if __name__ == '__main__':
    a = [20,30,64,16,8,0,99,24,75,100,69]
    print(ConfiationAlgorithm(a))
    b = [random.randint(1,1000) for i in range(10)]
    print(ConfiationAlgorithm(b))