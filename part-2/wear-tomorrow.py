print("What is the weather forecast for tomorrow?")

temp = float(input("Temperature: "))
will_rain = input("Will rain? (yes/no): ")

if will_rain == "yes":
    if temp > 20:
        print("Wear jeans and a T-shirt")
    elif temp > 10:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
    elif temp > 5:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
    print("Don't forget your umbrella!")
elif will_rain == "no":
    if temp > 20:
        print("Wear jeans and a T-shirt")
    elif temp > 10:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
    elif temp > 5:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("I think gloves are in order")