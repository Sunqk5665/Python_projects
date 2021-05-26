def h_temp(li):
    li.sort(reverse=True)
    i = 0
    while(i<len(li) and li[i]>i):
        i += 1
    return i


if __name__ == '__main__':
    li = eval(input())
    print(h_temp(li))