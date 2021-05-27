def check(n):
    '''
    计算各因子之和模块
    '''
    s = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            s += i
    return s


if __name__ == '__main__':
    for i in range(1, 3000):
        res = check(i)  # 对1至3000所有数依次求因子和
        if i != res and check(res) == i:  # 因子和不等于本身，且是亲密数，输出
            print(i, res)