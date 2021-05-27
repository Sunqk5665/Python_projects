count = 0  # 记录第几种分法
print("假设五本书分别为1，2，3，4，5，主要借法有")

for a in range(1, 6):
    for b in range(1, 6):
        if a != b:
            for c in range(1, 6):
                if c != a and c != b:
                    count += 1
                    print("第%d种：A分到书%d,B分到书%d,C分到书%d" % (count, a, b, c))
