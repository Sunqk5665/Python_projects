"""
    作者：Sunqk
    功能：52周春浅挑战
    版本：4.0
    日期：2019/8/4
    2.0新增功能：记录每周存款数
    3.0新增功能：把while改成for循环
"""
import math

# 全局变量
# saving = 0

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    """
        计算n周内的存款金额
    """

    # global saving

    money_list = []  # 记录每周存款数的列表

    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_money
        # print('函数内的saving:', saving)
    return saving

def main():
    """
        主函数
    """
    money_per_week = float(input('请输入每周存入的金额：'))    # 每周存的金额
    increase_money = float(input('请输入每周递增的金额：'))     # 递增的金额
    total_week = int(input('请输入总共的周数：'))         # 总共的周数

    # 局部变量
    # saving = 0              # 账户累计

    # 调用函数
    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    print('总存款金额:', saving)



if __name__ == '__main__':
    main()