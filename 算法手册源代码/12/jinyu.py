n = 11
while True:
    x = n
    for i in range(2, 5+1):
        x = x-(x/i+1/i)
    if x == 11:
        print(n)
        #####
        x = n
        for i in range(2, 5+1):
            m = x/i+1/i
            x = x - m
            print('%d: mai-->%d shend-->%d' %(i-1, m, x))
        #####
        break
    n = n + 1