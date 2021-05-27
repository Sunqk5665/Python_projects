import copy

#节点数据结构
class Node(object):
    # 初始化一个节点
    def __init__(self,value = None):
        self.value = value  # 节点值
        self.child_list = []    # 子节点列表
    # 添加一个孩子节点
    def add_child(self,node):
        self.child_list.append(node)

# 初始化一颗测试二叉树
def init():
    '''
    初始化一颗测试二叉树:
            A
        B   C   D
      EFG       HIJ
    '''
    root = Node('A')
    B = Node('B')
    root.add_child(B)
    root.add_child(Node('C'))
    D = Node('D')
    root.add_child(D)
    B.add_child(Node('E'))
    B.add_child(Node('F'))
    B.add_child(Node('G'))
    D.add_child(Node('H'))
    D.add_child(Node('I'))
    D.add_child(Node('J'))
    return root


# 深度优先查找 返回从根节点到目标节点的路径
def deep_first_search(cur,val,path=[]):
    path.append(cur.value)  # 当前节点值添加路径列表
    if cur.value == val:    # 如果找到目标 返回路径列表
        return path

    if cur.child_list == []:    # 如果没有孩子列表 就 返回 no 回溯标记
        return 'no'

    for node in cur.child_list: # 对孩子列表里的每个孩子 进行递归
        t_path = copy.deepcopy(path)    # 深拷贝当前路径列表
        res = deep_first_search(node,val,t_path)
        if res == 'no': # 如果返回no，说明找到头 没找到  利用临时路径继续找下一个孩子节点
            continue
        else :
            return res  # 如果返回的不是no 说明 找到了路径

    return 'no' # 如果所有孩子都没找到 则 回溯

# 获取最短路径 传入两个节点值，返回结果
def get_shortest_path( start,end ):
    # 分别获取 从根节点 到start 和end 的路径列表，如果没有目标节点 就返回no
    path1 = deep_first_search(root, start, [])
    path2 = deep_first_search(root, end, [])
    if path1 == 'no' or path2 == 'no':
        return '无穷大','无节点'
    # 对两个路径 从尾巴开始向头 找到最近的公共根节点，合并根节点
    len1,len2 = len(path1),len(path2)
    for i in range(len1-1,-1,-1):
        if path1[i] in path2:
            index = path2.index(path1[i])
            path2 = path2[index:]
            path1 = path1[-1:i:-1]
            break
    res = path1+path2
    length = len(res)
    path = '->'.join(res)
    return '%s:%s'%(length,path)

# 主函数、程序入口
if __name__ == '__main__':
    root = init()
    res = get_shortest_path('F','I')
    print(res)