for i in range(10000,99999):
    for j in range(0,10):
        if i*j % 111111 == 0:
            if len(set(str(i))) == 5:
                if (str(j) == str(i)[0]) and (str(i)[4] == str(i*j)[0]):
                    print("满足“算法描述题x算=题题题题题题”的数字是：{}".format(i))
# print(set(str(123456)))