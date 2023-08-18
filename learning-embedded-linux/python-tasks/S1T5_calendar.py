import calendar

def print_calendar(year, month):
    try:
        cal = calendar.month(year, month)
        print(cal)
    except ValueError as e:
        print("Invalid input:", e)

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print_calendar(year, month)

