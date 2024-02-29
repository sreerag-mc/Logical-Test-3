import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(cal)

if __name__ == "__main__":
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))

        if 1 <= month <= 12:
            display_calendar(year, month)
        else:
            print("Invalid month. Please enter a month between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for year and month.")
