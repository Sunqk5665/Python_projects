class Solution:
    def movingCount(self, threshold, rows, cols):
        "产生 0 矩阵 "
        board=[[0 for i in range(cols)] for j in range(rows)]
        global acc
        acc = 0
        "下标之和,若大于threshold则TRUE,否则False"
        def block(r,c):
            s=sum(map(int,str(r)+str(c)))
            return s>threshold

        def traverse(r,c):
            global acc
            if not (0<=r<rows and 0<=c<cols):   # 超出角标范围挑出
                return
            if board[r][c]!=0:    # 不等于0 跳出
                return
            if board[r][c]==-1 or block(r,c):
                board[r][c]=-1    #超出门限的点记录-1
                return

            board[r][c]=1 #符合规定的点记录1，并计数加一
            acc+=1
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)

        traverse(0,0)
        return acc


o = Solution()
print(o.movingCount(4 ,3 ,3))
