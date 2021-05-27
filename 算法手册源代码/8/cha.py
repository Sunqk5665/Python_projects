aList=[1,2,3,4,5,6,3,8,9]
sign=False                           #初始值为没找到
x=int(input("请输入要查找的整数："))
for i in range(len(aList)):
   if aList[i]==x:
      print("整数%d在列表中，在第%d个数"%(x,i+1))
      sign=True
if sign==False:
   print("整数%d不在列表中"%x)