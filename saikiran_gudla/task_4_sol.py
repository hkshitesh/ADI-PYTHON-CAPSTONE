def gen_fib_series(n):
    if n==0 or n==1:
        yield n
    else:
        yield (n-1 + n-2)

for i in range(0,11):
    print(next(gen_fib_series(i)))
