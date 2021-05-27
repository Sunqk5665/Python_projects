import math
from functools import reduce
def isPrimeNum(n):
    for k in range(2, int(math.sqrt(n) + 1)):
        if n % k == 0:
            return False
    return True

from itertools import permutations

for p in permutations([1, 3, 5, 7, 9], 5):
    # (3,5,7), (1,5,9), (1,3,5,7,9)
    for l in (p[1:-1], p[::2], p):
        s = reduce(lambda x, y: 10 * x + y, l)
        if not isPrimeNum(s):
            break
    else:
        print(p)
