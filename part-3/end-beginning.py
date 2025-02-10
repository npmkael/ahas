####################################################
# Part 3 - Programming exercise: End to beginning
####################################################

# Dogshet solution

"""
word = input("Please type in a string: ")
acc = -1
acs = 0

while len(word) - 1 >= acs:
    print(word[acc])
    acc -= 1
    acs += 1
"""

word = input("Please type in a string: ")
index = len(word) - 1

while index >= 0:
    print(word[index])
    index -= 1