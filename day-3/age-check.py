####################################################
# Part 2 - Programming exercise: Age check
####################################################


age = int(input("What is your age? "))

if age < 5:
    if age < 0:
        print("That must be a mistake")
    else:
        print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")
