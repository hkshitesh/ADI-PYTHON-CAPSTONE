3,4

car = namedtuple('Car',['brand','model','year'])
my_car = car('Toyota','Corolla',2022)

print("Brand:",my_car.brand)
print("Model:",my_car.model)
print("Year:",my_car.year)

print("Brand:",my_car[0])
print("Model:",my_car[1])
print("Year:",my_car[2])

