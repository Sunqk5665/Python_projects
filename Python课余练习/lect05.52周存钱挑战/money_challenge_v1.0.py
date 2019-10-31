"""
    作者：Sunqk
    功能：52周春浅挑战
    版本：1.0
    日期：2019/8/3
"""
def main():
    """
        主函数
    """
    money_per_week = 10     # 每周存的金额
    i = 1                   # 记录周数
    increase_money = 10     # 递增的金额
    total_week = 52         # 总共的周数
    saving = 0              # 账户累计

    while i <= total_week:
        # 存钱操作
        saving += money_per_week

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_money
        i += 1

if __name__ =='__main__':
    main()