def fact(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * fact(n - 1)
        print("intermediate result for ", n, " * fact(", n - 1, "): ", res)
        return res


print(fact(10))