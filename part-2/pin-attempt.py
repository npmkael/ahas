####################################################
# Part 2 - PIN and number of attempts
####################################################


pin = 4321
attempt = 0

while True:
    ask_pin = int(input("PIN:"))

    attempt += 1

    if attempt == 1 and ask_pin == pin:
        print("Correct! It only took you one single attempt!")
        break
    elif ask_pin == pin:
        print(f"Correct! It took you {attempt} attempts")
        break
    else:
        print("Wrong")

