def generator_cube():
    cube=[]
    for i in range(1,11):
        cu = i*i*i
        cube.append(cu)
    return cube

#print(generator_cube())

#def generate_cube(i):
    #yield i*i*i #only creates one instance

#for i in range(1,11):
    #print(next(generate_cube(i)))

def generate_cube(n):
    for i in range(1, n+1):
        yield i ** 3


c = generate_cube(9)

for i in c:
    print(i)