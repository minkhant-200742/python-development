week_days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
days_of_week = int(input("Enter the day of the week "))
if days_of_week < 7:
    print("Day of the week = ", week_days[days_of_week])
else:
    print("please enter 0 to 6 number")
