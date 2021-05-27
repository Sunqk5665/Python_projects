pt = [True] * 100
res = []

for p in range(2, 100):
    if not pt[p]: continue
    res.append(p)
    for i in range(p * p, 100, p):
        pt[i] = False

for i in range(1, len(res)):
    if res[i] - res[i - 1] == 2:
        print(res[i - 1], res[i])
