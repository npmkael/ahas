word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    index = word.find(character)
    
    if index == -1 or len(word) < 3:
        break
    
    found_word = word[index:index+3]
    
    if len(found_word) == 3:
        print(found_word)

        word = word[index + 1:]  

    else:
        break