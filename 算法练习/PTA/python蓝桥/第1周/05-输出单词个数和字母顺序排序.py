def prt(li):
    for i in li:
        print(i)
sent=""
s=input()
while s!="!!!!!":
    sent=sent + " " + s
    s = input()
li = [list(i) for i in list(set(sent.split()))] # 列表推导式；set()集合去重；(这里列表元素是列表)
li.sort()     #排序
li=[''.join(i) for i in li] # 将子列表转换为字符串
print(len(li))
prt(li[:10]) if len(li)>=10 else prt(li) # 在一定条件下调用函数


# print(list(set(['a','b','a','c','d','c'])))
# print(''.join(['aaa']))