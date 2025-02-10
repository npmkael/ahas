####################################################
# Part 2 - Gift tax calculator
####################################################

value_gift = int(input("Value of gift: "))

if value_gift < 5000:
    print("No tax!")
elif value_gift >= 5000 and value_gift < 25000:
    print(f"Amount of tax: {100 + (value_gift - 5000) * 0.08} euros")
elif value_gift >= 25000 and value_gift < 55000:
    print(f"Amount of tax: {1700 + (value_gift - 25000) * 0.10} euros")
elif value_gift >= 55000 and value_gift < 200000:
    print(f"Amount of tax: {4700 + (value_gift - 55000) * 0.12} euros")
elif value_gift >= 200000 and value_gift < 1000000:
    print(f"Amount of tax: {22100 + (value_gift - 200000) * 0.15} euros")
elif value_gift >= 1000000:
    print(f"Amount of tax: {142100 + (value_gift - 1000000) * 0.17} euros")