num_one = int(input("Number 1: "))
num_two = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
  print(f"{num_one} + {num_two} = {num_one + num_two}")
elif operation == "subtract":
  print(f"{num_one} - {num_two} = {num_one - num_two}")
elif operation == "multiply":
  print(f"{num_one} * {num_two} = {num_one * num_two}")
elif operation == "divide":
  print(f"{num_one} / {num_two} = {num_one / num_two}")
else:
  print("Invalid operation")