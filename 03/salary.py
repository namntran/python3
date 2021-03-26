# Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours. 
# Only whole hours are counted. If he works more hours than that (overtime) he gets paid at 1.5 times his normal rate for the overtime. 
# If he sells more than 5 cars in a week, he gets a bonus of $200 per car from the 6th car sold. 
# Write program to calculate the wages plus bonus for the car dealer in a week.

hours = int(input("How many hours were worked? "))
cars = int(input("Total number of cars sold for the week? "))
baseRate = 36.25
baseSalary = 37 * baseRate
commission = (cars - 5) * 200 
extraHours = hours-37
penaltyRate = baseRate*1.5
overTime = extraHours*penaltyRate

if hours > 37:
    salary = baseSalary + overTime
    if cars > 5:
        salary = salary + commission
else:
    salary = hours * baseRate

print(f'The salary is {salary}')

# print("base salary: ", baseSalary) # temporary
# print("commission: ", commission) # temporary
# print("extra hours: ", extraHours) # temporary
# print("over time: ",overTime) # temporary