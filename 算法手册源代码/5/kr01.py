edges = [("A", "B", 5), ("A", "G", 7),
         ("B", "F", 1), ("C", "F", 4),
         ("C", "D", 3), ("C", "E", 7),
         ("E", "F", 6), ("D", "E", 4),
         ("E", "G", 12),("F", "G", 12)]
vertices=list('ABCDEFG')
edges.sort(key=lambda x:x[2])
ori_trees=dict()
for i in vertices:
    ori_trees[i]=i
#寻找根节点
def find_node(x):
    if ori_trees[x]!=x:
        ori_trees[x]=find_node(ori_trees[x])
    return ori_trees[x]
#定义最小生成树
mst=[]
#定义循环次数，n为需要添加的边数=顶点数-1
n=len(vertices)-1
#循环
for edge in edges:
    v1,v2,_=edge
    if find_node(v1)!=find_node(v2):
        ori_trees[find_node(v2)]=find_node(v1)
        mst.append(edge)
        print('添加第'+str(7-n)+'条边后：')
        n-=1
        print(ori_trees)
        print(mst)
        if n==0:
            break