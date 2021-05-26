n = int(input())
amo = 0
def f(r):
    global amo
    st = ""
    while(r):  # 二进制生成
        # print(r&1,end=" ")
        st += str((r & 1))
        r >>= 1

    while(len(st) < n):
        st += "0"
    if st.count("1") > len(st)/2:
        print(st[::-1])
        amo += 1

temp = 2**n
for i in range(0,temp):
    f(i)
print("amount = {}".format(amo))

# st = ''
# r=3
# while(r):
#         # print(r&1,end=" ")
#         st += str((r & 1))
#         r >>= 1
# print(st[::-1])
# r>>=1
# print(2&1)