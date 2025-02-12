
"""
word = input("Please type in a string: ")

if "a" in word:
  print("a is found")
else:
  print("a is not found")

if "e" in word:
  print("e is found")
else:
  print("e is not found")

if "o" in word:
  print("o is found")
else:
  print("o is not found")
"""

word = input("Please type in a string: ")
vowels = "aeo"
x = 0

while x < len(vowels):
  if vowels[x] in word:
    print(f"{vowels[x]} is found")
  else:
    print(f"{vowels[x]} not found")
  
  x += 1
