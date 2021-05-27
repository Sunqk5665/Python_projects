import os
import time
from datetime import datetime

class data_struct():
    def __init__(self, letter, status):
        self.letter = letter
        self.status = status  # True表示字母在头部，不能为零, False时可以取零
        if self.status == False:
            self.digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 0-9
        else:
            self.digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 0-9

def norepeat(list0):
    length = len(list0)
    list1 = [0 for i in range(0,10,1)] # 取值0-9
    for i in range(0,length,1):
        list1[list0[i]] += 1
        if int(list1[list0[i]]) > 1:
            return False
    return True

if __name__ == '__main__':
    '''wwwdot - google = dotcom'''
    letterW = data_struct('W', True)
    letterG = data_struct('G', True)
    letterD = data_struct('D', True)
    letterO = data_struct('O', False)
    letterT = data_struct('T', False)
    letterL = data_struct('L', False)
    letterE = data_struct('E', False)
    letterC = data_struct('C', False)
    letterM = data_struct('M', False)

    # list0 = [1,2,3,4,5,6,0,8,9]
    # if True == norepeat(list0):
    #     print 'hello'


    str1 = ''
    str2 = ''
    str3 = ''
    begintime = datetime.now()
    for w in letterW.digit:
        for g in letterG.digit:
            for d in letterD.digit:
                for o in letterO.digit:
                    for t in letterT.digit:
                        for l in letterL.digit:
                            for e in letterE.digit:
                                for c in letterC.digit:
                                    for m in letterM.digit:
                                        list0 = [w, g, d, o, t, l ,e, c, m]
                                        if True == norepeat(list0):
                                            str1 = str(w)*3 + str(d) + str(o) + str(t)
                                            str2 = str(g) + str(o)*2 + str(g) + str(l) + str(e)
                                            str3 = str(d) + str(o) + str(t) + str(c) + str(o) + str(m)
                                            if int(str1) - int(str2) == int(str3):  # wwwdot - google = dotcom
                                                print(str1, str2, str3)
    endtime = datetime.now()
    deltatime = endtime - begintime
    print('穷举搜索耗时： ' , deltatime)