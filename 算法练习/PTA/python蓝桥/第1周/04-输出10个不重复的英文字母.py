# 要求:随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。
# 如没有10个英文字母，显示信息“not found”
# String模块 ascii_letters 和 digits 方法：ascii_letters是生成所有字母，
# 从a-z和A-Z,digits是生成所有数字0-9
from string import digits  # 所有数字
from string import ascii_letters as al #所有字母
def prt(s): # 筛选函数
    re='' #
    for i in s:
        if i in al and i.lower() not in re and i.upper() not in re: # 判断字符是否是字母并且是否重复，并筛选出来
            re += i
    return re
st = input().translate(str.maketrans('','',digits)) # 去除字符串中所有的数字
re = prt(st)
if len(re)<10:
    print("not found")
else:
    print(re[:10])