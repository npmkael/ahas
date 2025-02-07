from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

d = (b ** 2) - (4 * a * c)

sol1 = (-b + sqrt(d)) / (2 * a)
sol2 = (-b - sqrt(d)) / (2 * a)

print(f"The roots are {sol1} and {sol2}")