def getNum(l,r,k):
    d_index = {1:0}

    def getF(x):
        if x in d_index:
            return  d_index[x]
        d_index[x] = (getF(x*3+1)if x%2==1 else getF(x//2))+1
        return d_index[x]
    arr = list(range(l,r+1))
    arr.sort(key=lambda x:(getF(x),x))
    # print(d_index)
    # print(arr)
    return arr[k-1]

if __name__ == '__main__':
    l,r = map(int,input().split())
    k = int(input())
    print(getNum(l,r,k))