# 散列表定义
graph = {}
# graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["jonny"] = []
graph["thom"] = []

def person_is_seller(name):  # 函数person_is_seller，判断一个人是不是芒果销售商
    return  name[-1] == 'm'
# 创建一个队列
from collections import deque
search_queue = deque()   # 创建一个（搜索）队列
search_queue += graph["you"]  #将你的邻居都加到这个搜索队列中
                  # graph["you"]是一个数组，其中包含你的所有的邻居，如["alice", "bob", "claire"]。

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller!")
        break
    else:
        search_queue += graph[person]


