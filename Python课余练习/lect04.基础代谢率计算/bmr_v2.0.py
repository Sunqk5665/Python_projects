"""
    作者：Sunqk
    功能：BMR计算器
    版本: 2.0
    日期：2019/8/2
    新增功能：根据用户输入计算BMR，程序持续运行
"""

def main():
    """
        主函数
    """
    y_or_n = input('是否退出程序(y/n)?')

    while y_or_n != 'y':
        # 性别
        gender = input('性别：')

        # 体重（kg）
        weight = float(input('体重(kg)：'))

        # 身高
        height = float(input('身高（cm）：'))

        # 年龄
        age = int(input('年龄:'))

        if gender == '男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('基础代谢率（大卡）：',bmr)
        else:
            print('暂不支持g该性别')
        y_or_n = input('是否退出程序（y/n）?')

if __name__ == '__main__':
    main()