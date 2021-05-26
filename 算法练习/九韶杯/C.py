from fractions import Fraction
li = [1,1]
new = []
fenzi = []
s = 1
bigfenzi = 0
bigfenmu = 1
for i in range(2,14):
    li.append(li[i-2]+li[i-1])

for i in range(0,13):
    new.append(li[i]*li[i+1])
for i in new:
    for j in new:
        if j!=i:
            s = s*j
    fenzi.append(s)
    s=1
bigfenzi = sum(fenzi)
for i in new:
    bigfenmu = bigfenmu*i
print(li)
print(new)
print(bigfenzi)
print(bigfenmu)
print(fenzi)
print(Fraction(bigfenzi,bigfenmu))

