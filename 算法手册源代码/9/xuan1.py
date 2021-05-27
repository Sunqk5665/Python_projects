def SelectSort(lists):
    count=len(lists)
    for i in range(0,count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i] , lists[j] = lists[j] , lists[i]
            print("===========")
            print(i,j)
            print(lists)

if __name__ == "__main__":
    lists = [3, 5, 4, 2, 1, 6]
    print(lists)
    SelectSort(lists)