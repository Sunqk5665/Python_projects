def change(bills):
    if bills[0]!=5:
        return False
    else:
        bills2 = bills[1:]
        five_money=1
        ten_money=0
        for i in bills2:
            if i == 5:     # 有支付 5元的
                five_money += 1
            elif i == 10:  # 有支付10元的
                five_money -= 1
                ten_money += 1
            else:          # 有支付20元的
                if ten_money >= 1:
                    ten_money -= 1
                    five_money -= 1
                else:
                    five_money -= 3
                if five_money < 0 or ten_money < 0: #看看是否是把5元的和10元的给减没了
                    return False
        return True


if __name__=='__main__':
    bills = list(map(int,eval(input())))
    # bills = eval(input())
    #print(bills)
    canchange = change(bills)
    if canchange==False:
        print('False',end="")
    else:
        print("True",end="")
# a = list(map(int,eval(input())))
# print(a)