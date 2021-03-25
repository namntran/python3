# alculate money
# hours   rate  bonus    result
# 5       9       0   ->  45
# 7       12      2   ->  98

regularHours = int(input("hours: "))
bonusHour = int(input("bonus hours"))
baseRate = int(input("base rate: "))
bonusRate = int(input("bonus rate: "))

print(regularHour * baseRate + bonusHour *( baseRate + bonusRate)
# print("The rate of pay:", (hours*(rate+bonus))