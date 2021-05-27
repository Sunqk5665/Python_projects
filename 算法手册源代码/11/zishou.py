print([n for n in range(1,10000)
       if n * n % (10 ** len(str(n))) == n]
      )