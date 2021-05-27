if __name__ =="__main__":
    num_lst = list(map(int, input().split()))
    n = len(num_lst)
    out_lst = []

    for i in range(0,n,2):
        xishu = num_lst[i]
        zhishu = num_lst[i+1]
        if zhishu == 0:
            continue

        out_lst.append(str(xishu * zhishu))
        out_lst.append(str(zhishu-1))

    out_str = " ".join(out_lst)
    if out_str:
        print(out_str.strip())

    else:
        print("0 0")