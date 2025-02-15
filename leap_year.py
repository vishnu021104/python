import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
print(calendar.month(year, month))



# Check if it's a leap year
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

