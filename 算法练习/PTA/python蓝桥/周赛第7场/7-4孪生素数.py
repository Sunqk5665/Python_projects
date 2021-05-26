#埃氏筛法
n = int(input())
li = [1 for i in range(n+1)]
#li[2]=0
#li[3]=0
count = 0    # 计数
for i in range(2,n+1-2):
    if li[i]==1:
        if i*i<n+1:
            for j in range(i*i,n+1,i):
                li[j]=0
    if li[i] and li[i+2]:
        count += 1
        #print("({},{})".format(i,i+2))
print(count)


# def sushu(n):
#     k = int(float(n)**0.5)
#     for i in range(2,k+1):
#         if(n%i != 0):
#             continue
#         else:        # 不是素数
#             return False
#     return True
#
#
# n = int(input())
# array = [int(i) for i in range(3,n+1)]  # 生成[3,n]的数组
# count = 0
# for i in range(len(array)-2):
#     if sushu(array[i]) and sushu(array[i+2]):
#         #print("({},{})".format(array[i],array[i+2]))
#         count += 1
# print(count)




# print(sushu(10))

# print(array)



# for i in range(4):
#     print(i)