seconds = int(input())
m,s = divmod(seconds,60)
h,m = divmod(m,60)
print("%d:%d:%d"%(h,m,s))


# sec = int(input())
# h = sec//3600
# m = (sec-h*3600)//60
# s = sec-h*3600-m*60
# print("%d:%d:%d"%(h,m,s))