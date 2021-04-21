# Given starting and ending years, write a function to calculate the number of days

"""Function that calculates leap year"""
def isLeapYear (year):
    # leap year if it is divisible by 4 AND not divisible by 100 OR divisible by 400
    if year == year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def countDays (firstYear, lastYear):
    """Function that calculates the total number of days between two years."""
    days = 0
    leapYear = 366
    nonleapYear = 365
    # for loop with 2 arguments
    for i in range (firstYear, lastYear+1):
        # pass boolean value function to check condition
        if isLeapYear(i):
            days = days + leapYear
        else:
            days = days + nonleapYear
    # print(days) #temporary value
    return days

# Ask user for input years
year1 = (int(input("Year 1: ")))
year2 = (int(input("Year 2: ")))

print ("Number of days:", countDays(year1, year2))







