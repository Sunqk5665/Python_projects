class Good:
    def __init__(self, weight, value, status):
        self.weight = weight
        self.value = value
        self.status = status  # 0是未放入背包，1是已经放入背包


class Greedy(object):

    def greedy(self, goods, W):  # goods是物品的集合，W是背包的空闲重量
        result = []
        sum_weight = 0
        while True:
            s = self.strategy(goods, W)
            if s == -1:
                break
            sum_weight = sum_weight + goods[s].weight
            result.append(goods[s].weight)
            W = W - goods[s].weight
            goods[s].status = 1
            goods.pop(s)
        return result, sum_weight

    def strategy(self, goods, W):  # 按最小重量贪心策略
        index = -1
        minWeight = goods[0].weight
        for i in range(0, len(goods)):
            currentGood = goods[i]
            if currentGood.status == 0 and currentGood.weight <= W and currentGood.weight <= minWeight:
                index = i
                minWeight = goods[index].weight
        return index


if __name__ == '__main__':
    goods = [Good(35, 10, 0), Good(30, 40, 0), Good(60, 30, 0), Good(50, 50, 0),
             Good(40, 35, 0), Good(10, 40, 0), Good(25, 30, 0)]
    g = Greedy()
    result, sum_weight = g.greedy(goods, 150)
    print("--------------按照取最小重量贪心策略--------------")
    print("最终总重量为：" + str(sum_weight))
    print("重量选取依次为：", end='')
    print(result)
