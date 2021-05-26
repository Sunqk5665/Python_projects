def kaishi(a):
    for i in a:
        if(i=="哺乳动物"):
            for i in a:
                if(i=="食肉动物"):
                    for i in a:
                        if(i=="黄褐色"):
                            for i in a:
                                if(i=="暗斑点"):
                                    print("金钱豹")
                                elif(i=="黑色条纹"):
                                    print("虎")
    for i in a:
        if(i=="蹄类动物"):
            for i in a:
                if(i=="长脖子"):
                    for i in a:
                        if(i=="长腿"):
                            for i in a:
                                if(i=="暗斑点"):
                                    print("长颈鹿")
                elif(i=="黑色条纹"):
                    print("斑马")
    for i in a:
        if(i=="鸟"):
            for i in a:
                if(i=="长脖子"):
                    for i in a:
                        if(i=="长腿"):
                            for i in a:
                                if(i=="不会飞"):
                                    for i in a:
                                        if(i=="黑白二色"):
                                            print("鸵鸟")
                elif(i=="会游泳"):
                    for i in a:
                        if("不会飞"):
                            for i in a:
                                if(i=="黑白二色"):
                                    print("企鹅")
                elif(i=="会飞"):
                    print("信天翁")




if __name__ == '__main__':
    print("动物的各种特征")
    a=[]
    while(1):
        st = input()
        if(st=='0'):
            break
        a.append(st)
    kaishi(a)
