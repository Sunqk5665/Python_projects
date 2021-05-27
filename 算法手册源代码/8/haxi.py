#除法取余法实现的哈希函数
def myHash(data,hashLength,):
    return data % hashLength
#哈希表检索数据
def searchHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
   #指定hashAddress存在，但并非关键值，则用开放寻址法解决
    while hash.get(hashAddress) and hash[hashAddress]!=data:
        hashAddress+=1
        hashAddress=hashAddress%hashLength
    if hash.get(hashAddress)==None:
        return None
    return hashAddress

#数据插入哈希表
def insertHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
    #如果key存在说明应经被别人占用， 需要解决冲突
    while(hash.get(hashAddress)):
        #用开放寻执法
        hashAddress+=1
        hashAddress=myHash(hashAddress,hashLength)
    hash[hashAddress]=data

if __name__ == '__main__':
    hashLength=20
    L=[13, 29, 27, 28, 26, 30, 38 ]
    hash={}
    for i in L:
        insertHash(hash,hashLength,i)
    result=searchHash(hash,hashLength,38)
    if result:
        print("数据已找到，索引位置在",result)
        print(hash[result])
    else:
        print("没有找到数据")
