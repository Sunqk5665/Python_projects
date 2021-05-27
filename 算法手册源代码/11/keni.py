def getPrimeTable(n):
    pt = [True] * n
    for p in range(2, n):
        if not pt[p]: continue
        for i in range(p * p, n, p):
            pt[i] = False
    return pt

pt = getPrimeTable(900)
for p in range(10, 900):
    if not pt[p]: continue
    q = int(str(p)[::-1])
    if p != q < 900 and pt[q]:
        pt[q] = False
        print(p, q)
