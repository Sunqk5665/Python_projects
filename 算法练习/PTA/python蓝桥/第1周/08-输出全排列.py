n = int(input())
import itertools
items = list(map(str,range(1,n+1)))
for p in itertools.permutations(items):
    print(''.join(p))
# print(list(items))