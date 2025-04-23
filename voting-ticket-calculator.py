from datetime import datetime, timedelta

current_date = datetime.now()
date_now = datetime.now()
days_input = int(input("Enter the number of days: "))
current_ticket = int(input("How many tickets you currently have?\n"))

# 12 hours x 2 = 1 day, so we loop 2 times per day
steps = days_input * 2

for _ in range (steps):
  current_date += timedelta(hours=12)
  day = int(current_date.strftime("%w"))

  if day == 0 or day == 6:
    current_ticket += 2
  else:
    current_ticket += 1

print(f"You will have {current_ticket} tickets in {days_input} days - {date_now.strftime('%B %d, %Y')} - {current_date.strftime('%B %d, %Y')}.")