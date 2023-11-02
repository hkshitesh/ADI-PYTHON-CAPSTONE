
def fibonacci(n):
    if n < 0:
        print("Enter valid number")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def fib_gen(i):
    yield fibonacci(i)


for i in range(1, 11):
    print(next(fib_gen(i)))
