####################################################
# Part 2 - Programming exercise: The elder
####################################################


print("Person 1: ")
person_one_name = input("Name: ")
person_one_age = int(input("Age: "))

print("Person 2: ")
person_two_name = input("Name: ")
person_two_age = int(input("Age: "))

if person_one_age > person_two_age:
    print(f"The elder is {person_one_name}")
elif person_two_age > person_one_age:
    print(f"The elder is {person_two_name}")
else:
    print(f"{person_one_name} and {person_two_name} are the same age")