def x(n):

    if n<10:

        list1=[]

        list1.append(n)

        return list1

    else:

        s=n%10

        n=n//10

        list1=list(x(n))

        list1.append(s)

        return list1

print(x(12345))