def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fib()
print(next(fibonacci))

for i in range(10):
    print(next(fibonacci))
