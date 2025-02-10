####################################################
# Part 3 - Programming exercise: Sum of consecutive numbers part 2
####################################################

limit = int(input("Limit: "))
sum = 1
add = 2
solution = ""

while limit > sum:
  solution += f" + {add}"
  sum += add
  add += 1
  
print(f"The consecutive sum: 1{solution} = {sum}")