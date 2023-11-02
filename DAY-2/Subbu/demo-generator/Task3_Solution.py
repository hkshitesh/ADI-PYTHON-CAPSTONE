def generate_FibSeries(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

s = generate_FibSeries(20)

for i in s:
    print(i)