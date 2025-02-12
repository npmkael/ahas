# Part 1

"""

word = input("Please type in a string: ")
word_length = len(word)
add = 1

while add <= word_length:
  print(word[0:add])
  add += 1

"""

# Part 2

word = input("Please type in a string: ")
word_length = len(word)

while word_length > 0:
  print(word[word_length - 1:])
  word_length -= 1