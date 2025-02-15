import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

mycal=calendar.month(year, month)

print(mycal)
