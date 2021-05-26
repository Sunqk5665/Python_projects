sum = 5
li = [0,0]
for i in range(2,20210411+1):
    li.append(i)
    sum = sum + li[i-1]+li[i] + (li[i])

print((sum-2)//((10*9)+7))