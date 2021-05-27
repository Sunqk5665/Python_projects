def fixUp(a): #在堆尾加入新元素，fixUp恢复堆的条件
  k=len(a)-1
  while k>1 and a[k//2]<a[k]:
    a[k//2],a[k]=a[k],a[k//2]
    k=k//2
def fixDown(a): #取a[1]返回的值，然后把a[N]移到a[1]，fixDown来恢复堆的条件
  k=1
  N=len(a)-1
  while 2*k<=N:
    j=2*k
    if j<N and a[j]<a[j+1]:
      j+=1
    if a[k]<a[j]:
      a[k],a[j]=a[j],a[k]
      k=j
    else:
      break
def insert(a,elem):
  a.append(elem)
  fixUp(a)
def delMax(a):
  maxElem=a[1]
  N=len(a)
  if N<=1:
    print('There\'s none element in the list')
    return -1
  if N==2:
    return a[1]
  else:
    a[1]=a.pop()
    fixDown(a)
    return maxElem
data=[-1,] #第一个元素不用，占位
insert(data,26)
insert(data,5)
insert(data,77)
insert(data,1)
insert(data,61)
insert(data,11)
insert(data,59)
insert(data,15)
insert(data,48)
insert(data,19)
result=[]
N=len(data)-1
for i in range(N):
  print(data)
  result.append(delMax(data))
print(result)