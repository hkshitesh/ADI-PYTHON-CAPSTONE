def fibbonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


f = fibbonacci()

for _ in range(10):
    print(next(f))
