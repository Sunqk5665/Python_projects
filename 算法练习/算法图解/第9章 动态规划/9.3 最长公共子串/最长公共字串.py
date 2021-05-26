str_a = 'hfhbabababnxz'
str_b = 'fhjsababjas'
cell = [[0 for j in range(len(str_a)+1)] for i in range(len(str_b)+1)]
#print(cell)
for j in range(1,len(str_a)+1):
    for i in range(1,len(str_b)+1):
        if str_a[j-1]==str_b[i-1]:
            cell[i][j] = cell[i-1][j-1]+1
        # else:
        #     cell[i][j] = 0
#print(cell)
maxList = []
for li in cell:
    maxList.append(max(li))
print(max(maxList))