print("Please type in integer numbers. Type in 0 to finish.")

sum = 0
postive_numbers = 0
negative_numbers = 0
number_typed = 0

while True:
  number = int(input("Number: "))

  if number == 0:
    break

  if number < 0:
    negative_numbers += 1
  else:
    postive_numbers += 1

  number_typed += 1
  sum += number

print(f"Numbers typed in {number_typed}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / number_typed}")
print(f"Positive numbers {postive_numbers}")
print(f"Negative numbers {negative_numbers}")