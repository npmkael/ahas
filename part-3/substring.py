

word = input("Please type in a string: ")
word_length = len(word)
add = 1

while add <= word_length:
  print(word[0:add])
  add += 1