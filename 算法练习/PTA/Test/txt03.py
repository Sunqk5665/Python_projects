days = int(input())
def hanshu(i):
    if i in (0,1):
        return 1
    return hanshu(i-1)+hanshu(i-2)
#for i in range(0,days):
#    a=hanshu(i)
print(hanshu(days))