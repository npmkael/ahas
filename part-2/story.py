####################################################
# Part 2 - Part 1 & Part 2 Story exercise
####################################################


space = " "
story = ""
previous_word = ""

while True:
  word = input("Please type in a word: ")

  if word == "end":
    break
  elif word == previous_word:
    break

  story += word + space
  previous_word = word

print(story)
  
