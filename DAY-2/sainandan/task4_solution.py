def generate_fibanocci(n1, n2):
    yield n1 + n2

n1 = 0
n2 = 1
print(n1)
print(n2)

for i in range(1, 10):
    val = next(generate_fibanocci(n1, n2))
    print(val)
    n1 = n2
    n2 = val
