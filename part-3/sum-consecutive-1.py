####################################################
# Part 3 - Programming exercise: Sum of consecutive numbers part 1
####################################################



limit = int(input("Limit: "))
sum = 1
add = 2

while limit > sum:
  sum += add
  add += 1

print(sum)