# 实现树结构的类，树的节点有三个私有属性 左指针 右指针 自身的值
class Node():

    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right


if __name__ == '__main__':
    # 实例化根节点
    root_node = Node('a')
    # root_node.set_data('a')
    # 实例化左子节点
    left_node = Node('b')
    # 实例化右子节点
    right_node = Node('c')

    # 给根节点的左指针赋值，使其指向左子节点
    root_node.set_left(left_node)
    # 给根节点的右指针赋值，使其指向右子节点
    root_node.set_right(right_node)

    print(root_node.get_data(), root_node.get_left().get_data(), root_node.get_right().get_data())
