####################################################
# day 1 of 100 days of python for thesis!
####################################################

# The first look at print() function
# Programming exercise: Emoticon

# first_part = input("The 1st part: ")
# second_part = input("The 2nd part: ")
# third_part = input("The 3rd part: ")
# print(first_part + "-" + second_part + "-" + third_part)


# f-strings (print(f"{variable_name}"))
#

"""
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")
"""

# end=" " parameter
"""
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)
"""

name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))

print(f"Hi {name}, you will be {2021 - birth_year} years old at the of the year 2021")
