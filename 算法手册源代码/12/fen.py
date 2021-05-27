def xf(n):
  a=1
  b=a
  while 1:
   for i in range(n-1):
    a=(a-1)/n*(n-1)*1.0
   if (a-1)%n==0:
    return b
   b+=1
   a=b
print(xf(5))