def isTF(s):
    if s.isspace():
        return True
    if not s.isspace() and len(s)%2 != 0:
        return False
    p = {")":"(","]":"[","}":"{"}
    stack = list()  # 定义一个栈stack
    for i in s:
        if i in p:  # 判断i是否在字典p的键中,也就是判断i是一个右括号
            if not stack or stack[-1]!=p[i]: # 栈为空或者栈顶元素不等于字典中右括号值
                return False
            else:
                stack.pop()
        else:       # i是左括号
            stack.append(i)
    if not len(stack): # 栈为空
        return True
    return False

s = input()
if isTF(s):
    print("True")
else:
    print("False")


# stack = [1,2,3]
# a = not stack
# print(a)

# p = {")":"(","]":"[","}":"{"}
# print(')' in p)