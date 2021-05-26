# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#plt.figure(figsize=(20,20))
#plt.figure(dpi=480*320)
plt.rcParams['font.sans-serif']=['SimHei'] #使汉字显示
#plt.xticks(x, x, rotation=30)  # 这里是调节横坐标的倾斜度，rotation是度数

fig,y1=plt.subplots()

y2 = y1.twinx()
y3=y1.twinx()

df = pd.read_excel("2000-2020年的年度人口数据.xlsx")
#print(df["年末总人口(万人)"])
y1.plot(df["年份"],df["年末总人口(万人)"],label='年末总人口(万人)',linewidth=3,color='b',marker='v',markerfacecolor='blue',markersize=12)
y2.plot(df["年份"],df["国内生产总值GDP(亿元)"],label='国内生产总值GDP(亿元)',linewidth=3,color='r',marker='s',markerfacecolor='red',markersize=12)
y3.plot(df["年份"],df["全国CPI(1978=100)"],label='全国CPI(1978=100)',linewidth=3,color='g',marker='o',markerfacecolor='green',markersize=12)

#y1.xticks(rotation=45)
plt.xlabel("time")
#y1.ylabel('年末总人口(万人)')
#plt.title("summy of 和")
y1.tick_params(axis='y',colors='blue')# "年末总人口(万人)"纵坐标颜色为 blue
y2.tick_params(axis='y',colors='red')# "国内生产总值GDP(亿元)"纵坐标颜色为 red
y3.tick_params(axis='y',colors='green')# "全国CPI(1978=100)" 纵坐标颜色为 green

y1.legend(loc='upper left')#标签
y2.legend(loc='center left')
y3.legend(loc='upper center')
plt.grid()
plt.title(" 2000-2019年的年度人口变化数据、GDP 统计数据、CPI 数据")
#plt.figure(figsize=(12,6), dpi=100)
plt.show()

