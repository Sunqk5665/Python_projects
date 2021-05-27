# 导入 numpy 函数，以 np 开头
import numpy as np

if __name__ == '__main__':
    # 矩阵相乘
    mat1 = np.mat([1, 3])
    mat2 = np.mat([[3], [4]])
    mat3 = mat1 * mat2
    print(mat3)

    # 1 * 2 矩阵乘以 2 * 1 矩阵，得到 1 * 1 矩阵
    # ==> [[15]]

    # 矩阵求逆
    mat4 = np.mat([[1, 0, 1], [0, 2, 1], [1, 1, 1]])
    mat5 = mat4.I  # I 对应 getI(self) ，返回可逆矩阵的逆
    print(mat5)

    # 矩阵的逆
    # ==> [[-1. -1.  2.]
    # ==>  [-1.  0.  1.]
    # ==>  [ 2.  1. -2.]]


    # 转置矩阵
    mat6 = np.mat([[1, 1, 1], [0, 2, 1], [1, 1, 1]])
    mat7 = mat6.T  # I 对应 getT(self) ，返回矩阵的转置矩阵
    print(mat7)

    # 矩阵的转置矩阵
    # ==> [[1 0 1]
    # ==>  [1 2 1]
    # ==>  [1 1 1]]



    # 矩阵每一列的和
    sum1 = mat6.sum(axis=0)
    print(sum1)
    # 矩阵每一行的和
    sum2 = mat6.sum(axis=1)
    print(sum2)

    # 矩阵所有行列的总和
    sum3 = sum(mat6[1, :])
    print(sum3)

    # 矩阵与数组之间的转换
    mat8 = np.mat([[1, 2, 3]])
    arr1 = np.array(mat8)  # 矩阵转换成数组
    print(arr1)

    arr2 = [1, 2, 3]
    mat9 = np.mat(arr2)  # 数组转换成矩阵
    print(mat9)