####################################################
# Part 3 - Programming exercise: The longer string
####################################################

word_one = input("Please type in string 1: ")
word_two = input("Please type in string 2: ")

if len(word_one) > len(word_two):
  print(f"{word_one} is longer")
elif len(word_two) > len(word_one):
  print(f"{word_two} is longer")
elif len(word_one) == len(word_two):
  print("The strings are equally long")