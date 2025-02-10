####################################################
# Part 2 - The next leap year exercise
####################################################

year = int(input("Year: "))
leap_year = year

if year % 4 == 0:
  while True:
    leap_year += 1 
    if leap_year % 4 == 0 and leap_year % 100 != 0:
      break
    elif leap_year % 4 == 0 and leap_year % 100 == 0 and leap_year % 400 == 0:
      break
else:
  while True:
    leap_year += 1 
    if leap_year % 4 == 0 and leap_year % 100 != 0:
      break
    elif leap_year % 4 == 0 and leap_year % 100 == 0 and leap_year % 400 == 0:
      break

print(f"The next leap year after {year} is {leap_year}")