import numpy as np

A = np.array([[5.0, 2, 1], [-1, 4, 2], [2, -3, 10]])
B = np.array([-12.0, 20, 3])
x0 = np.array([1.0, 1, 1])
x = np.array([0.0, 0, 0])
times = 0

while True:
    for i in range(3):
        temp = 0
        tempx = x0.copy()
        for j in range(3):
            if i != j:
                temp += x0[j] * A[i][j]
        x[i] = (B[i] - temp) / A[i][i]
        x0[i] = x[i].copy()
    calTemp = max(abs(x - tempx))
    times += 1
    if calTemp < 1e-4:
        break
    else:
        x0 = x.copy()

print(times)
print(x)
