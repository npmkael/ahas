####################################################
# Part 3 - Programming exercise: Powers of base n
####################################################

limit = int(input("Upper limit: "))
base = int(input("Base: "))
power = 1

while limit >= power:
  print(power)
  power *= base