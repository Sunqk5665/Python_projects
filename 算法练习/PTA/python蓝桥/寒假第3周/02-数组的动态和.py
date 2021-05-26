
def F(arr):
    output = []
    temp = 0
    for i in arr:
        output.append(i + temp)
        temp += i
    return output

if __name__=="__main__":
    nums = [int(i)for i in input().split()]
    st_arr = [str(i)for i in F(nums)]
    # print(st_arr)
    st = ','.join(st_arr)
    print(st)
