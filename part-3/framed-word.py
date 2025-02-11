import math

word = input("Word: ")
word_length = len(word)

print("*" * 30)

if word_length % 2 == 0:
  spaces = " " * int((28 - word_length) / 2)
  print("*" + spaces + word + spaces + "*")
else: # for odd numbers
  left_spaces = " " * math.floor((28 - word_length) / 2)
  right_spaces = " " * math.ceil((28 - word_length) / 2)
  print("*" + left_spaces + word + right_spaces + "*")

print("*" * 30)