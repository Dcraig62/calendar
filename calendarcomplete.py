
def getMonth():
    month = int(input("Enter the number of the month: "))
    while month < 1 or month > 12:
        month = int(input("You must enter a valid month: "))
    return month

def getYear():
    year = int(input("Enter the year: "))
    while year < 1753:
        year = int(input("The year must be after 1753: "))
    return year

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def getDays(month, leapYear):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2 and leapYear == True:
        return 29
    elif month == 2 and not leapYear:
        return 28
    else :
        return 30

def getOffeset(year, month, isLeapYear):
    days = 0
    yearCount = 1753 
    monthCount = 1
    while yearCount < year:
        days += daysInYear(yearCount)
        yearCount += 1
    while monthCount < month:
        days += getDays(monthCount, isLeapYear)
        monthCount += 1
    print(days)
    print (days % 7)
    return (days % 7)

def daysInYear(year):
    if leapYear(year):
        return 366
    else:
        return 365

def getMonthName(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "Febuary"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    else:
        return "December"

def displayHeader(monthName, year):
    print()
    print(str(monthName) + ", " + str(year))

def display(days, offset):
    print ("Su Mo Tu We Th Fr Sa")
    daysOfMonth = 1
    daysOfWeek = 0
    for daysOfWeek in range(int(offset * 1.5)):
        print(' ', end = ' '),
    daysOfWeek = offset
    while daysOfMonth <= days:
        while daysOfWeek < 7 and daysOfMonth <= days:
            print("{:>2}".format(daysOfMonth), end = ' '),
            daysOfWeek += 1
            daysOfMonth += 1
        print()
        daysOfWeek = 0

month = getMonth()
year = getYear()
isLeapYear = leapYear(year)
days = getDays(month, isLeapYear)
offset = getOffeset(year, month, isLeapYear)
monthName = getMonthName(month)
displayHeader(monthName, year)
offset = (offset + 1) % 7
display(days, offset)