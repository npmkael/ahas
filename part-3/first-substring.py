word = input("Please type in a word: ")
character = input("Please type in a character: ")

word_length = len(word)
index = word.find(character)

found_word = word[index:index+3]

if len(found_word) == 3:
  print(found_word)
