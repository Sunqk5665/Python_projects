import json

def dictsum(list, keyname):
    num = 0
    for item in list:
        num += item[keyname]
    return num

class Greedy():
    def __init__(self,data,maxWeight):
        self.maxWeight=maxWeight
        self.dataList=sorted(self.readData(data), key=lambda e: e.__getitem__('average'), reverse=True)
        self.selectedList=[]
    def readData(self,data):
        for item in data:
            value=item["price"]/item["weight"]
            item.setdefault("average", value)
        return data
    def pick(self):
        for i in range(len(self.dataList)-1):
            tempList=[]
            totleWeight = self.maxWeight
            for j in range(i,len(self.dataList)):
                if self.dataList[j]["weight"]<=totleWeight:
                    tempList.append(self.dataList[j])
                    totleWeight=totleWeight-self.dataList[j]["weight"]
            if tempList!=[]:
                if dictsum(tempList,"price")>dictsum(self.selectedList,"price"):
                    self.selectedList = tempList
                elif dictsum(tempList,"price")==dictsum(self.selectedList,"price"):
                    if dictsum(tempList,"price")<dictsum(self.selectedList,"price"):
                        self.selectedList = tempList
                tempList = []
        return self.selectedList,dictsum(self.selectedList,"weight"),dictsum(self.selectedList,"price")

class Genetic():
    def __init__(self):
        pass

if __name__ == "__main__":
    # 贪婪算法求解01背包问题
    data = [
        {"weight": 4, "price": 4},
        {"weight": 2, "price": 1.9},
        {"weight": 3, "price": 2.9},
    ]
    maxWeight = 5
    selected, subweight, subprice = Greedy(data, maxWeight).pick()
    result = json.dumps([{'select': selected, 'all weight': subweight, 'all price': subprice}])
    print(result )