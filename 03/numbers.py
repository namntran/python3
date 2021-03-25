# program that sorts inputs in descending order
integer1 = int(input("Integer 1? "))
integer2 = int(input("Integer 2? "))
integer3 = int(input("Integer 3? "))

#store user input of numbers in list
list = [integer1, integer2, integer3]
#sort list in descending order
list.sort(reverse=True)
#use map function to convert items in list to a string and then join use space ' ' as separator 
print ("Sorted: ", ' '.join(map(str, list)))
