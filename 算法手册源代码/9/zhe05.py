import datetime
import bisect


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)


a = []
for x in range(3000):
    a.append(x)

a.reverse()

start = datetime.datetime.now()
insertion_sort(a)
end = datetime.datetime.now()
print("直接插入排序: %s" % (end - start))


a.reverse()

start2 = datetime.datetime.now()
insertion_sort_bin(a)
end2 = datetime.datetime.now()
print("折半插入排序: %s" % (end2 - start2))
