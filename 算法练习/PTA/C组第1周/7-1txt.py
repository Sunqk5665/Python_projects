n = int(input())
array = [i+1 for i in range(n)]
for i in array:
    for j in array[:]:
        if j == i:
            continue
        for k in array[:]:
            if (k == i)or(k == j):
                continue
            if(i+j+k)%2==0:
                print(i,j,k)
# print(array[1:])
# print((2+5)%5)