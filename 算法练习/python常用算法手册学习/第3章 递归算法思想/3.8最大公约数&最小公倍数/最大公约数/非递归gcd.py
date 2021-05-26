# import math
# print(math.gcd(20,10)) # 其实可以直接调用库函数即可实现！！！
def gcd_test_one(a,b):
    if a!=0 and b!=0:
        if a>b:
            a,b=b,a
        if b%a==0:
            return a
        gcd_list=[]
        for i in range(1,a):
            if b%i==0 and a%i==0:
                gcd_list.append(i)
        return max(gcd_list)
    else:
        print("Number is Wrong!!!")

if __name__ == '__main__':
    a=int(input())
    b = int(input())
    print(gcd_test_one(a,b))