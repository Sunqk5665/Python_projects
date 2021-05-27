#coding:utf-8
from __future__ import division

input_a = input(u'箱数:')
input_b = input(u'最大承受重量:')

list_c = []
list_z = []

for i in range(1,int(input_a)+1):
    input_c = input('第'+str(i)+'箱的总价值:')
    input_d = input('第'+str(i)+'箱的重量:')
    avg = round(int(input_c)/int(input_d),1)#每一箱，重量为1的价值
    list_c.append(avg)#添加到列表，用于之后做比较
    list_z.append([int(input_d),avg,0])#此处列表中添加列表，中间的列表一个存放总重量，第二个存放单位价值，第三个存放是否该物品已被取走

list_c.sort(reverse=True) # 降序排序
sum =[0,0]# 用于存放取走的总重量，第一个参数是取走的重量，第二个是超出前的备份
num =0
ji = 0


for i in range(len(list_c)):
    for k in range(len(list_z)):
        if ji == 0:#做是否超出马车最大承受量的标记，未超出为0
            if (list_c[i] == list_z[k][1]) and (list_z[k][2]==0):
                sum[1] = sum[0]#备份
                sum[0] = sum[0] + list_z[k][0]#取走的重量
                v = list_z[k][0]#取走的重量
                if sum[0] > int(input_b):#如果所有取走的重量超出马车的重量，就依次减少一单元的重量
                    ji = 1#超出为1
                    t= list_z[k][0]
                    while True:#依次减去单位1的重量
                        z = sum[1] + t#使用备份进行判断，此时取走的数量已经大于最大承受量了
                        if z <= int(input_b):
                            break
                        t = t-1
                    v=t#等于最大承受量时，价值较大的一件物品应取走的数量
                    sum[0]=sum[1]#从备份恢复
                    sum[0] = sum[0] + t#此时为真正的取走数量
                num = list_c[i]*v + num#总价值
                list_z[k][2] = 1#取走的标记
print(u'能带走的糖果的最大价值为:',num)