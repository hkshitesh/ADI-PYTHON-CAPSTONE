from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model','year'])

my_car = Car('Toyota', 'Corolla', '2020')

print("Brand: ", my_car.brand)
print("Model: ", my_car.model)
print("Year: ", my_car.year)

print("Brand: ", my_car[0])
print("Model: ", my_car[1])
print("Year: ", my_car[2])