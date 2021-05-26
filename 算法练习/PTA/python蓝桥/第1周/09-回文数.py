def IsF(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return 0
    return 1

n = int(input())
for i in range(n+1):
    if(IsF(str(i))):
        print(i)