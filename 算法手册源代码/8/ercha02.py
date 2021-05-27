import random

class BiTNode():
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.lchild = left
        self.rchild = right

class BinarySortTree():
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            if bt.val < key:
                bt = bt.rchild
            elif bt.val > key:
                bt = bt.lchild
            else:
                return bt.val
        return None

    def insert(self, key):
        bt = self._root

        # 空树插入的第一步
        if not bt:
            self._root = BiTNode(key)
            return

        while True:
            if bt.val < key:
                if bt.rchild is None:
                    bt.rchild = BiTNode(key)
                    return
                bt = bt.rchild
            else:
                if bt.lchild is None:
                    bt.lchild = BiTNode(key)
                    return
                bt = bt.lchild

    def delete(self, key):
        parent_node, cur_node = None, self._root

        if not self._root:
            print('The tree is empty!')
            return

        while cur_node and cur_node.val != key:
            parent_node = cur_node
            if key < cur_node.val:
                cur_node = cur_node.lchild
            else:
                cur_node = cur_node.rchild
            if not cur_node:
                print('No such kty!')
                return

        if not cur_node.lchild:
            # cur_node左子树不存在，直接将cur_node的右子树接入parent_node
            if parent_node is None:
                self._root = cur_node.rchild
            elif parent_node.lchild is cur_node:
                parent_node.lchild = cur_node.rchild
            else:
                parent_node.rchild = cur_node.rchild

        # 查找cur_node的左子树的最右节点，将cur_node的右子树链接为该节点的右子树
        right_node = cur_node.lchild
        while right_node.rchild:
            right_node = right_node.rchild
        right_node.rchild = cur_node.rchild

        # 将新的左子树接入parent_node
        if parent_node is None:
            self._root = cur_node.lchild
        elif parent_node.lchild is cur_node:
            parent_node.lchild = cur_node.lchild
        else:
            parent_node.rchild = cur_node.lchild

    def __iter__(self):
        data = []
        node = self._root
        while node or data:
            while node:
                data.append(node)
                node = node.lchild
            node = data.pop()
            yield node.val
            node = node.rchild


if __name__ == '__main__':
    list = [random.randint(1,9) for i in range(20)]
    bst = BinarySortTree()
    for i in list:
        bst.insert(i)
    for j in bst:
        print(j)
    bst.delete(1)
    for j in bst:
        print(j)
