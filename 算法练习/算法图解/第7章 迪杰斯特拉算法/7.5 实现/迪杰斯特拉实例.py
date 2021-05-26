# 创建整个图的散列表
graph = {}

graph["start"] = {} # 添加起点及其邻居
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print(graph["start"].keys()) #可以获取起点的所有邻居

graph["a"] = {}  #添加其他节点及其邻居
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # 终结点没有任何的邻居

# 创建散列表costs存储起点到每一个节点的开销
infinity = float("inf")  # 定义一个无穷大变量
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 创建存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# print(graph)
# print(costs)
# print(parents)

# 创建一个数组用来存放处理过的节点，因为对于同一个节点不用处理多次
processed = [] # 存放处理过的节点

# 定义函数find_lowest_cost_node 用来在未处理的的节点中找出开销最小的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过，
            lowest_cost = cost                           # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)# 在未处理的节点中找出开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有的邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居更近，
            costs[n] = new_cost # 就更新该邻居的开销
            parents[n] = node   # 同时将该邻居的父节点设置为当前节点
    processed.append(node)      # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并继续参与循环
print("从起点到终点的最小花费为:{}".format(costs["fin"]))

lst = ["fin"]
a = "fin"
# print("fin",end='<--')
while(parents[a]!="start"):
    #print(parents[a],end='<--')
    lst += [parents[a]]
    a = parents[a]
lst += ['start'] # 此时路径为倒叙的
lst.reverse()    # 将路径列表取反
print("路 径 为".center(15,'*')+':',end='')
for i in lst[:-1:]:
    print(i + "——>",end='')
print("fin")
# print(lst[::],end="-->")
