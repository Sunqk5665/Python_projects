a = input()
n = 11  # 对应每一层元素的乘积系数
ans = 0
b = a
for i in range(len(b)):
    if b[i] == '[':
        n -= 1
    elif b[i] == ']':
        n += 1
    elif b[i] == ',':
        continue
    elif b[i+1] == ',' or b[i+1] == ']':
        ans += n
#        j += 1
print(ans)