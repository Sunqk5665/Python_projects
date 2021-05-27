def hanoi(n,x,y,z):

    if n==1:

        print(x,"-->",z)

    else:

        hanoi(n-1,x,z,y)

        print(x,"-->",y)

        hanoi(n-1,y,x,z)

while True:

    n=int(input("请输入汉诺塔的层数："))


    hanoi(n,"x","y","z")