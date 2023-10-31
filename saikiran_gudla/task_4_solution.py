def gen_fib_series():
    i = 0
    j = 1
    while True:
        yield i
        i,j = j, i+j

value = gen_fib_series()

for i in range(0,11):
    print(next(value))
