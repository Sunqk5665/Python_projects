from fractions import gcd
#非递归实现
def gcd_test_one(a, b):
  if a!=0 and b!=0:
    if a>b:
      a, b=b, a
    if b%a==0:
      return a
    gcd_list=[]
    for i in range(1,a):
      if b%i==0 and a%i==0:
        gcd_list.append(i)
    return max(gcd_list)
  else:
    print('Number is wrong!!!')
#递归实现
def gcd_test_two(a, b):
  if a>b:
    a, b=b, a
  if b%a==0:
    return a
  else:
    return gcd_test_two(a,b%a)

if __name__ == '__main__':
  print(gcd_test_one(12,24))
  print(gcd_test_one(12,8))
  print(gcd_test_one(6,24))
  print(gcd_test_one(0,24))
  print( '----------------------------------------------------------------------------')
  print(gcd_test_two(12,24))
  print(gcd_test_two(12,8))
  print(gcd_test_two(6,32))
