def generator_cube():
    cube=[]
    for i in range(1,11):
        c=i*i*i
        cube.append(c)
    return cube

#print(generator_cube())

def generate_cube(i):
    yield i*i*i

# for i in range(1,11):
#     print(next(generate_cube(i)))


def generate_cube(n):
    for i in range(1, n + 1):
        yield i*i*i


c = generate_cube(10)

for i in c:
    print(i)