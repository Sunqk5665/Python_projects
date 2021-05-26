#(一)
a = input()
n = 0
ans = 0
backup = a
a = a.replace('[','')
a = a.replace(']','')
nums = a.split(',')
b = backup
j = 0
for i in range(len(b)):
    if b[i] == '[':
        n += 1
    elif b[i] == ']':
        n -= 1
    elif b[i] == ',':
        continue
    elif b[i+1] == ',' or b[i+1] == ']':
        ans += int(nums[j]) * n
        j += 1
print(ans)

# (二)化简版
a = input()
n = 0  # 对应每一层元素的乘积系数
ans = 0
b = a
# backup = a
# a = a.replace('[','')
# a = a.replace(']','')
# nums = a.split(',')
# b = backup
# j = 0
for i in range(len(b)):
    if b[i] == '[':
        n += 1
    elif b[i] == ']':
        n -= 1
    elif b[i] == ',':
        continue
    elif b[i+1] == ',' or b[i+1] == ']':
        ans += int(b[i]) * n
#        j += 1
print(ans)