#红黑树
from random import randint

RED = 'red'
BLACK = 'black'

class RBT:
    def __init__(self):
       # self.items = []
        self.root = None
        self.zlist = []

    def LEFT_ROTATE(self, x):
        # x是一个RBTnode
        y = x.right
        if y is None:
            # 右节点为空，不旋转
            return
        else:
            beta = y.left
            x.right = beta
            if beta is not None:
                beta.parent = x

            p = x.parent
            y.parent = p
            if p is None:
                # x原来是root
                self.root = y
            elif x == p.left:
                p.left = y
            else:
                p.right = y
            y.left = x
            x.parent = y

    def RIGHT_ROTATE(self, y):
        # y是一个节点
        x = y.left
        if x is None:
            # 右节点为空，不旋转
            return
        else:
            beta = x.right
            y.left = beta
            if beta is not None:
                beta.parent = y

            p = y.parent
            x.parent = p
            if p is None:
                # y原来是root
                self.root = x
            elif y == p.left:
                p.left = x
            else:
                p.right = x
            x.right = y
            y.parent = x

    def INSERT(self, val):

        z = RBTnode(val)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right

        z.PAINT(RED)
        z.parent = y

        if y is None:
            # 插入z之前为空的RBT
            self.root = z
            self.INSERT_FIXUP(z)
            return

        if z.val < y.val:
            y.left = z
        else:
            y.right = z

        if y.color == RED:
            # z的父节点y为红色，需要fixup。
            # 如果z的父节点y为黑色，则不用调整
            self.INSERT_FIXUP(z)

        else:
            return

    def INSERT_FIXUP(self, z):
        # case 1:z为root节点
        if z.parent is None:
            z.PAINT(BLACK)
            self.root = z
            return

        # case 2:z的父节点为黑色
        if z.parent.color == BLACK:
            # 包括了z处于第二层的情况
            # 这里感觉不必要啊。。似乎z.parent为黑色则不会进入fixup阶段
            return

        # 下面的几种情况，都是z.parent.color == RED:
        # 节点y为z的uncle
        p = z.parent
        g = p.parent  # g为x的grandpa
        if g is None:
            return
            #   return 这里不能return的。。。
        if g.right == p:
            y = g.left
        else:
            y = g.right

        # case 3-0:z没有叔叔。即：y为NIL节点
        # 注意，此时z的父节点一定是RED
        if y == None:
            if z == p.right and p == p.parent.left:
                # 3-0-0:z为右儿子,且p为左儿子，则把p左旋
                # 转化为3-0-1或3-0-2的情况
                self.LEFT_ROTATE(p)
                p, z = z, p
                g = p.parent
            elif z == p.left and p == p.parent.right:
                self.RIGHT_ROTATE(p)
                p, z = z, p

            g.PAINT(RED)
            p.PAINT(BLACK)
            if p == g.left:
                # 3-0-1:p为g的左儿子
                self.RIGHT_ROTATE(g)
            else:
                # 3-0-2:p为g的右儿子
                self.LEFT_ROTATE(g)

            return

        # case 3-1:z有黑叔
        elif y.color == BLACK:
            if p.right == z and p.parent.left == p:
                # 3-1-0:z为右儿子,且p为左儿子,则左旋p
                # 转化为3-1-1或3-1-2
                self.LEFT_ROTATE(p)
                p, z = z, p
            elif p.left == z and p.parent.right == p:
                self.RIGHT_ROTATE(p)
                p, z = z, p

            p = z.parent
            g = p.parent

            p.PAINT(BLACK)
            g.PAINT(RED)
            if p == g.left:
                # 3-1-1:p为g的左儿子，则右旋g
                self.RIGHT_ROTATE(g)
            else:
                # 3-1-2:p为g的右儿子，则左旋g
                self.LEFT_ROTATE(g)

            return


        # case 3-2:z有红叔
        # 则涂黑父和叔，涂红爷，g作为新的z，递归调用
        else:
            y.PAINT(BLACK)
            p.PAINT(BLACK)
            g.PAINT(RED)
            new_z = g
            self.INSERT_FIXUP(new_z)

    def DELETE(self, val):
        curNode = self.root
        while curNode is not None:
            if val < curNode.val:
                curNode = curNode.left
            elif val > curNode.val:
                curNode = curNode.right
            else:
                # 找到了值为val的元素,正式开始删除

                if curNode.left is None and curNode.right is None:
                    # case1:curNode为叶子节点：直接删除即可
                    if curNode == self.root:
                        self.root = None
                    else:
                        p = curNode.parent
                        if curNode == p.left:
                            p.left = None
                        else:
                            p.right = None

                elif curNode.left is not None and curNode.right is not None:
                    sucNode = self.SUCCESOR(curNode)
                    curNode.val, sucNode.val  = sucNode.val, curNode.val
                    self.DELETE(sucNode.val)

                else:
                    p = curNode.parent
                    if curNode.left is None:
                        x = curNode.right
                    else:
                        x = curNode.left
                    if curNode == p.left:
                        p.left = x
                    else:
                        p.right = x
                    x.parent = p
                    if curNode.color == BLACK:
                        self.DELETE_FIXUP(x)

                curNode = None
        return False

    def DELETE_FIXUP(self, x):
        p = x.parent
        # w:x的兄弟结点
        if x == p.left:
            w = x.right
        else:
            w = x.left

        # case1:x的兄弟w是红色的
        if w.color == RED:
            p.PAINT(RED)
            w.PAINT(BLACK)
            if w == p.right:
                self.LEFT_ROTATE(p)
            else:
                self.RIGHT_ROTATE(p)

        if w.color == BLACK:
            # case2:x的兄弟w是黑色的，而且w的两个孩子都是黑色的
            if w.left.color == BLACK and w.right.color == BLACK:
                w.PAINT(RED)
                if p.color == BLACK:
                    return
                else:
                    p.color = BLACK
                    self.DELETE_FIXUP(p)

            # case3:x的兄弟w是黑色的，而且w的左儿子是红色的，右儿子是黑色的
            if w.left.color == RED and w.color == BLACK:
                w.left.PAINT(BLACK)
                w.PAINT(RED)
                self.RIGHT_ROTATE(w)

            # case4:x的兄弟w是黑色的，而且w的右儿子是红
            if w.right.color == RED:
                p.PAINT(BLACK)
                w.PAINT(RED)
                if w == p.right:
                    self.LEFT_ROTATE(p)
                else:
                    self.RIGHT_ROTATE(p)

    def SHOW(self):
        self.DISPLAY1(self.root)
        return self.zlist

    def DISPLAY1(self, node):
        if node is None:
            return
        self.DISPLAY1(node.left)
        self.zlist.append(node.val)
        self.DISPLAY1(node.right)

    def DISPLAY2(self, node):
        if node is None:
            return
        self.DISPLAY2(node.left)
        print(node.val)
        self.DISPLAY2(node.right)

    def DISPLAY3(self, node):
        if node is None:
            return
        self.DISPLAY3(node.left)
        self.DISPLAY3(node.right)
        print(node.val)

class RBTnode:
    '''红黑树的节点类型'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def PAINT(self, color):
        self.color = color

def zuoxuan(b, c):
    a = b.parent
    a.left = c
    c.parent = a
    b.parent = c
    c.left = b

if __name__ == '__main__':
    rbt=RBT()
    b = []

    for i in range(100):
        m = randint(0, 500)
        rbt.INSERT(m)
        b.append(m)

    a = rbt.SHOW()
    b.sort()
    equal = True
    for i in range(100):
        if a[i] != b[i]:
            equal = False
            break

    if not equal:
        print('wrong')
    else:
        print('OK!')