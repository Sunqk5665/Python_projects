name,luckpointtarget = input().split()
luckpointtarget = int(luckpointtarget)
huizhangpoints = 0
yourspoints = 1
while huizhangpoints<luckpointtarget and yourspoints<luckpointtarget:
    huizhangpoints += yourspoints
    yourspoints += huizhangpoints
if huizhangpoints>=luckpointtarget:
    print("jiangcheng")
    print(huizhangpoints)
else:
    print(name)
    print(yourspoints)