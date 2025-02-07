hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_week = input("Day of the week: ")

if day_week == "Sunday":
    print(f"Daily wages: {float(hourly_wage * hours_worked) * 2} euros")
else:
    print(f"Daily wages: {float(hourly_wage * hours_worked)} euros")