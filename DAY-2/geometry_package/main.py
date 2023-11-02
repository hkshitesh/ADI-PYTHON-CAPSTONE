from geometry_package.three_d import volume, surface_area
from geometry_package.two_d import area, perimeter

# 2D Geometry
length = 5
width = 4
print(f"2D Area: {area.calculate_area(length, width)}")
print(f"2D Perimeter: {perimeter.calculate_perimeter(length, width)}")

# 3D Geometry
length = 3
width = 2
height = 4
print(f"3D Volume: {volume.calculate_volume(length, width, height)}")
print(f"3D Surface Area: {surface_area.calculate_surface_area(length, width, height)}")
