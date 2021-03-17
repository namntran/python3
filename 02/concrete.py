# program to calculate volume of concrete required

length = float(input("Length of park (m): "))
width = float(input("Width of park (m): "))
litres = float(input("Litres per square metre: "))
total = length * width * litres
print("Litres required = ", total)