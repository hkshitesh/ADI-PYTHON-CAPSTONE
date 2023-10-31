
def fibonacci_generator(n):
    for i in range(1, n+1):
        if i == 1:
            prev1 = 0
            yield prev1
        elif i == 2:
            prev2 = 1
            yield prev2
        else:
            prev = prev1+prev2
            prev1 = prev2
            prev2 = prev
            yield prev
c = fibonacci_generator(4)

for i in c:
    print(i)