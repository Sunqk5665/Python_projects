class MatrixPath():
    def printMatrix(self, matrix, rows, cols, direction):
        if direction:
            print("---" + direction)
        for i in range(rows):
            for j in range(cols):
                print(matrix[cols * i + j], end=' ')
            print()

    def hasPath(self, matrix, rows, cols, path):
        # print("rows = %d, cols = %d" % (rows, cols))
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:  # 找到起始点
                    # tmp = matrix[i*cols+j]
                    # matrix[i*cols+j]='*'
                    if self.findPath(list(matrix), rows, cols, path[1:], i, j):
                        return True
                    # else:
                    #    matrix[i*cols+j] = tmp
        return False

    def findPath(self, matrix, rows, cols, path, x, y):
        if not path:  # 找完了？
            return True
        # 将当前位置标记为已走过
        matrix[x * cols + y] = '*'
        if y + 1 < cols and matrix[x * cols + y + 1] == path[0]:  # 比较东边
            self.printMatrix(matrix, rows, cols, "向东走")
            return self.findPath(matrix, rows, cols, path[1:], x, y + 1)
        elif y - 1 >= 0 and matrix[x * cols + y - 1] == path[0]:  # 比较西边
            self.printMatrix(matrix, rows, cols, "向西走")
            return self.findPath(matrix, rows, cols, path[1:], x, y - 1)
        elif x + 1 < rows and matrix[(x + 1) * cols + y] == path[0]:  # 比较南边
            self.printMatrix(matrix, rows, cols, "向南走")
            return self.findPath(matrix, rows, cols, path[1:], x + 1, y)
        elif x - 1 >= 0 and matrix[(x - 1) * cols + y] == path[0]:  # 比较北边
            self.printMatrix(matrix, rows, cols, "向北走")
            return self.findPath(matrix, rows, cols, path[1:], x - 1, y)
        else:
            return False


if __name__ == "__main__":
    # 调用测试
    _matrix = 'abcesfcsadee'
    _path = 'see'
    path = MatrixPath()
    path.printMatrix(_matrix, 3, 4, None)
    print(path.hasPath(list(_matrix), 3, 4, _path))