n = input().split()
n = list(map(int,n))
for i in range(len(n)):
    if i!= n[i]:
        print(i)
        break