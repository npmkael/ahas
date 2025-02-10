####################################################
# Part 3 - Programming exercise: A rectangle of hashes
####################################################

width = int(input("Width: "))
height = int(input("Height: "))

while height > 0:
  print("#" * width)
  height -= 1