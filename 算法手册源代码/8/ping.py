# @usage   平衡二叉树
# @author  mw
# @date    2016年07月28日  星期四  15:36:42
# @param
# @return
#
###
class AVLTree(object):
    def info(self):
        a = [];
        for x in self:
            a.append(x);

        print(a);

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __contains__(self, val):
        for x in self:
            if (x == val):
                return True;

        return False;

    def __len__(self):
        a = [];
        for x in self:
            a.append(x);

        return len(a);

    class __AVLNode(object):
        def __init__(self, key, height=0, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 0

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            if (self.key != None):
                yield self.key

            if self.right != None:
                for elem in self.right:
                    yield elem

        # 迭代的是Node类型，用于删除结点
        def iternodes(self):
            if self.left != None:
                for elem in self.left.iternodes():
                    yield elem

            if self != None and self.key != None:
                yield self

            if self.right != None:
                for elem in self.right.iternodes():
                    yield elem

        def info(self):
            s = 'Key=' + str(self.key) + ', ' + \
                'LChild=' + str(self.left) + ', ' + \
                'RChild=' + str(self.right) + ', ' + \
                'H=' + str(self.height);

            print(s);

        def __str__(self):
            return str(self.key);

        def __repr__(self):
            if self != None:
                s_1 = str(self.key);
            else:
                s_1 = 'None';

            if self.left != None:
                s_2 = str(self.left.key);
            else:
                s_2 = 'None';

            if self.right != None:
                s_3 = str(self.right.key);
            else:
                s_3 = 'None';

            s_4 = str(self.height);

            return '__AVLNode(' + s_1 + ', ' + s_2 + ', ' + s_3 + ', ' + s_4 + ')';

    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if node is None:
            return None
        elif key < node.key:
            return self._find(key, self.left)
        elif key > node.key:
            return self._find(key, self.right)
        else:
            return node

    # 找最小元素
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    # 找最大元素
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    # 求结点高度
    def height(self, node):
        if (node == None):
            return 0;
        else:
            m = self.height(node.left);
            n = self.height(node.right);
            return max(m, n) + 1;

    # LL
    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    # RR
    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    # LR
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    # RL
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    # 插入
    def insert(self, key):
        if not self.root:
            self.root = AVLTree.__AVLNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            node = AVLTree.__AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)

        elif key > node.key:
            node.right = self._insert(node.right, key)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.doubleRightRotate(node)
                else:
                    node = self.singleRightRotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    # 删除
    def delete(self, key):
        if key in self:
            self.root = self.remove(key, self.root)

    def remove(self, key, node):
        if node is None:
            raise KeyError('Error,key not in tree');
        elif key < node.key:
            node.left = self.remove(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif key > node.key:
            node.right = self.remove(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self.remove(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self.remove(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left

        return node

    # 传回结点的原始信息
    def iternodes(self):
        if self.root != None:
            return self.root.iternodes()
        else:
            return [None];

    # 寻找节点路径
    def findNodePath(self, root, node):
        path = [];
        if root == None or root.key == None:
            path = [];
            return path

        while (root != node):
            if node.key < root.key:
                path.append(root);
                root = root.left;
            elif node.key >= root.key:
                path.append(root);
                root = root.right;
            else:
                break;

        path.append(root);
        return path;

    # 寻找父结点
    def parent(self, root, node):
        path = self.findNodePath(root, node);
        if (len(path) > 1):
            return path[-2];
        else:
            return None;

    # 是否左孩子
    def isLChild(self, parent, lChild):
        if (parent.getLeft() != None and parent.getLeft() == lChild):
            return True;

        return False;

    # 是否右孩子
    def isRChild(self, parent, rChild):
        if (parent.getRight() != None and parent.getRight() == rChild):
            return True;

        return False;

    # 求某元素是在树的第几层
    # 约定根为0层
    # 这个计算和求结点的Height是不一样的
    def level(self, elem):
        if self.root != None:
            node = self.root;
            lev = 0;

            while (node != None):
                if elem < node.key:
                    node = node.left;
                    lev += 1;
                elif elem > node.key:
                    node = node.right;
                    lev += 1;
                else:
                    return lev;

            return -1;

        else:
            return -1;

if __name__ == '__main__':
    avl = AVLTree();

    a = [20, 30, 40, 120, 13, 39, 38, 40, 18, 101];
    b = [[10, 1], [3, 0], [4, 0], [13, -1], [2, 0], [18, 0], [40, -1], [39, 0], [12, 0]];

    for item in b:
        avl.insert(item);

    avl.info();

    print(45 in avl);
    print(len(avl));

    '''
    avl.delete(40);
    avl.info();
    avl.delete(100);
    avl.info();
    avl.insert(1001);
    avl.info();
    '''

    for item in avl.iternodes():
        item.info();
        print(avl.findNodePath(avl.root, item));
        print('Parent:', avl.parent(avl.root, item));
        print('Level:', avl.level(item.key));
        print('\n');