####################################################
# Part 2 - Programming exercise: Alphabetically in the middle
####################################################

first_letter = input("Enter first letter: ")
second_letter = input("Enter second letter: ")
third_letter = input("Enter third letter: ")

if second_letter > first_letter and second_letter < third_letter:
    print(f"The letter in the middle is {second_letter}")
elif first_letter < second_letter and first_letter > third_letter:
    print(f"The letter in the middle is {first_letter}")
elif first_letter > second_letter and first_letter < third_letter:
    print(f"The letter in the middle is {first_letter}")
elif second_letter < first_letter and second_letter > third_letter:
    print(f"The letter in the middle is {second_letter}")
elif third_letter > first_letter and third_letter < second_letter:
    print(f"The letter in the middle is {third_letter}")
elif third_letter < first_letter and third_letter > second_letter:
    print(f"The letter in the middle is {third_letter}")
