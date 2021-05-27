import math
import time
from  multiprocessing import cpu_count
from multiprocessing import Pool


# 判断数字是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 验证大于2的偶数可以分解为两个质数之合
# T为元组，表示需要计算的数字区间
def GDBH(T):
    S = T[0]
    E = T[1]
    if S < 4:
        S = 4
    if S % 2 == 1:
        S += 1
    for i in range(S, E + 1, 2):
        isGDBH = False
        for j in range(i // 2 + 1): # 表示成两个质数的和,其中一个质数不大于1/2
            if isPrime(j):
                k = i - j
                if isPrime(k):
                    isGDBH = True
                    if i % 100000 == 0:  # 每隔10万个数打印一次
                        print('%d=%d+%d' % (i, j, k))
                    # print('%d=%d+%d' % (i, j, k))
                    break
        if not isGDBH:  # 打印这句话表示算法失败 或是猜想失败（怎么可能...）
            print('哥德巴赫猜想失败！！')
            break


# 对整个数字空间N进行 分段CPU_COUNT
def seprateNum(N, CPU_COUNT):
    list = [[i + 1, i + N // 8] for i in range(4, N, N // 8)]
    list[0][0] = 4
    if list[CPU_COUNT - 1][1] > N:
        list[CPU_COUNT - 1][1] = N
    return list


if __name__ == '__main__':
    N = 10 ** 6

    # 多进程
    time1 = time.process_time()
    CPU_COUNT = cpu_count()  ##CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = seprateNum(N, CPU_COUNT)

    result = pool.map(GDBH, sepList)
    pool.close()
    pool.join()
    print('多线程耗时:%d s' % (time.clock() - time1))

    # 单线程
    time2 = time.clock()
    GDBH((4, N))
    print('单线程耗时:%d s' % (time.clock() - time2))