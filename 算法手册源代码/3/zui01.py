# 最小公倍数
def lcm(a, b, c=1):
  if a * c % b != 0:
    return lcm(a, b, c+1)
  else:
    return a*c
test_cases = [(4, 8), (35, 42), (5, 7), (20, 10)]
for case in test_cases:
  print('lcm of {} & {} is {}'.format(*case, lcm(*case)))
def lcm(a, b):
  for i in range(2, min(a,b)+1):
    if a % i == 0 and b % i == 0:
      return i * lcm(a//i, b//i)
  else:
    return a*b
test_cases = [(4, 8), (5, 7), (24, 16), (35, 42)]
for case in test_cases:
  print('lcm of {} & {} is {}'.format(*case, lcm(*case)))
# 最大公约数
def gcd(a, b):
  if a == b:
    return a
  elif a-b > b:
    return gcd(a-b, b)
  else:
    return gcd(b, a-b)
test_cases = [(35, 14), (88, 66), (5, 4), (20, 10)]
for case in test_cases:
  print('GCD of {} & {} is {}'.format(*case, gcd(*case)))
