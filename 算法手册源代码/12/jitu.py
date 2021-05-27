while True:
    try:
        sum = eval(input("请输入鸡和兔子脚的总数: "))
        head = eval(input("请输入鸡和兔子头的总数: "))

        if sum < 6:
            print("输入鸡和兔子脚的总数错误请重新输入>>>")
        elif head < 2:
            print("输入鸡和兔子头的总数错误请重新输入>>>")
        else:
            j = 0
            t = 0
            flag = False
            while j < head:
                j += 1
                t = head - j
                if (sum == (j * 2 + t * 4)):
                    print("有鸡 %d只有，兔子 %d只" % (j, t))
                else:
                    if flag == False:
                        flag = False
    except:
        print("能不能好好玩？")