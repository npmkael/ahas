####################################################
# Part 2 - Programming exercise: Greater than or equal to
####################################################

first_num = int(input("Please type in the first number: "))
second_num = int(input("Please type in the second number: "))

if first_num > second_num:
    print(f"The greater number was: {first_num}")
elif second_num > first_num:
    print(f"The greater number was: {second_num}")
else:
    print("The numbers are equal!")
