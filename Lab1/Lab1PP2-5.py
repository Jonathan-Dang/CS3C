#Lab 1| Jonathan Dang and Shichang Wang

#Input
var1 = int(input("Please input var1: "))
var2 = int(input("Please input var2: "))

sum = var1 + var2
dif = var1 - var2
product = var1 * var2
distance = abs(var1 - var2)
average = sum / 2
Max = max(var1,var2)
Min = min(var1,var2)

#Printing | Output
print("%-15s %10.2f" %("Sum:", sum))
print("%-15s %10.2f" %("Difference:", dif))
print("%-15s %10.2f" %("Product:", product))
print("%-15s %10.2f" %("Distance:", distance))
print("%-15s %10.2f" %("Average:", average))
print("%-15s %10.2f" %("Max:", Max))
print("%-15s %10.2f" %("Min:", Min))

#Sample Output
'''
Please input var1: 5
Please input var2: 4
Sum:             9.00
Difference:      1.00
Product:        20.00
Distance:        1.00
Average:         4.50
Max:             5.00
Min:             4.00
'''