# 完全背包问题，贪心算法
import time

class goods:
  def __init__(self, goods_id, weight=0, value=0):
    self.id = goods_id
    self.weight = weight
    self.value = value
# 不适用于0-1背包
def knapsack(capacity=0, goods_set=[]):
  # 按单位价值量排序
  goods_set.sort(key=lambda obj: obj.value / obj.weight, reverse=True)
  result = []
  for a_goods in goods_set:
    if capacity < a_goods.weight:
      break
    result.append(a_goods)
    capacity -= a_goods.weight
  if len(result) < len(goods_set) and capacity != 0:
    result.append(goods(a_goods.id, capacity, a_goods.value * capacity / a_goods.weight))
  return result
some_goods = [goods(0, 2, 4), goods(1, 8, 6), goods(2, 5, 3), goods(3, 2, 8), goods(4, 1, 2)]
start_time = time.perf_counter()
res = knapsack(6, some_goods)
end_time = time.perf_counter()
print('花费时间：' + str(end_time - start_time))
for obj in res:
  print('物品编号:' + str(obj.id) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.value), end=',')
  print('单位价值量为:' + str(obj.value / obj.weight))