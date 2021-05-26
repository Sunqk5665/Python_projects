from collections import Counter
dict1 = eval(input())
dict2 = eval(input())
print(dict1)
print(dict2)
dic = dict(Counter(dict1) + Counter(dict2))  # 用Counter()进行字典合并，然后恢复dict形式
sort_dic = dict(sorted(dic.items(),key=lambda x:ord(x[0]) if type(x[0])==str else x[0]))
print(sort_dic)
s = str(sort_dic).replace(" ","").replace("'","\"")
print(s)

c = dict(Counter({'a':4,'b':2}) + Counter({'a':4,'b':2}))
print(c)

print(ord('a'))
dict1 = eval(input())
print(dict1)
from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (dict(c))

# a = {'a':4,'b':2}
# b = {'c':3,'a':2}
