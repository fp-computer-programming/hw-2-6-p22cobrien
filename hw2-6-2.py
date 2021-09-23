# Author: CMOB 9/23/2021

height = input("what is the height? ")
radius = input("what is the radius? ")

height = float(height)
radius = float(radius)

surface_area = (2 * 3.14 * radius * (height + radius))

volume = (3.14 * (radius ** 2) * height)

print(surface_area)
print(volume)
