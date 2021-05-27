from heapq import *

inp = input("请输入要构建哈夫曼树的字符串")


# 统计每个自字符出现的频率 并生成字典
def generate_dict(s):
    dic = {}

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    return dic


dic = generate_dict(inp)


# 节点类
class Node(object):
    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight
        self.parent = None
        self.left = None
        self.right = None
        self.id = None

    # 自定义类的比较
    def __lt__(self, other):
        return int(self.weight) < int(other.weight)


# 按权值排序
def sort(list):
    return sorted(list, key=lambda Node: Node.weight)


def generate_node2(dic):
    lis = []

    for i in dic:
        newNode = Node(i, dic[i])
        heappush(lis, newNode)

    return lis


# lis = generate_node(dic)
lis = generate_node2(dic)


# Huffman编码2 使用堆的方式
def HuffmanTree2(lis):
    global id
    while (len(lis) != 1):
        a = heappop(lis)
        b = heappop(lis)
        new = Node()
        new.weight = a.weight + b.weight
        new.left, new.right = a, b

        a.parent = new
        b.parent = new

        heappush(lis, new)
    return lis


lis = HuffmanTree2(lis)

node = lis[0]  # 获取根结点


# 前序遍历方法 并执行一定的操作
def pre_order(root, code):
    if root is None:
        code = code[:-1]
        return

    pre_order(root.left, code + "0")

    if root.name is not None:
        print(root.name, "的权重为", root.weight, "编码为", code)

    pre_order(root.right, code + "1")


code = ""
# print(res)
print("构建的哈夫曼树为:")
pre_order(node, code)