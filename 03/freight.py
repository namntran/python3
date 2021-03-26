# Shipping costs based on the weight of goods and the distance of shipping(discounts).

baseprice = float(input("How much is the base price? "))
weight = float(input("What is the weight? "))
distance = float(input("What is the distance? "))

if distance < 250:
    discount = 0
elif distance < 500:
    discount = 0.10
elif distance < 1000:
    discount = 0.15
elif distance < 2000:
    discount = 0.20
elif distance < 3000:
    discount = 0.35
else:
    discount = 0.50

cost = baseprice * weight * distance * (1 - discount)

print (f'The shipping cost is {cost}')