####################################################
# Part 3 - Second and second to last characters
####################################################

word = input("Please type in a string: ")

if word[1] == word[len(word) - 2]:
    print(f"The second and second last characters {word[1]}")
else:
    print("The second and the second to last characters are different")