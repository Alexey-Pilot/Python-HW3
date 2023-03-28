def fib(i):
    if i in [1 , 2]:
        return 1
    return fib(i - 1) + fib(i -2)


n = fib(7)
print(n)