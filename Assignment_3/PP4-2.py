'''
•• P4.2 Write programs that read a sequence of integer inputs and print
	    a.The smallest and largest of the inputs.
		b.The number of even and odd inputs.
		c.Cumulative totals. For example, if the input is 1 7 2 9, the program should print 1 8 10 19. 
		d.All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the program should print 3 5 6.
'''

data = [] 
dups = []
smallest, largest, sum, even, odd= 0,0,0,0,0
prev = 0
flag = False
while (True):
    ins = input("Please input a number [enter X to exit]: ")
    if (ins == 'x' or ins == 'X'):
        break;
    num = float(ins)
    data.append(num)

smallest = data[0]
for i in range(data.__len__()):
    sum += data[i]
    if (smallest > data[i]):
        smallest = data[i]
    if (largest < data[i]):
        largest = data[i]
    if (data[i] % 2 == 0):      #Even number definition: A number that is divisible by 2 and has no remainder is an Even number | 0 is an Even Number
        even += 1
    if (data[i] % 2 == 1):    #Odd number definition: A number that is an integer, that cannot be divided by 2 with 0 remainder
        odd += 1
    if (i > 0 and data[i] == data[i - 1] and dups.count(data[i]) == 0):
        dups.append(data[i])

        
print(f"Smallest Entry: {smallest}")
print(f"Largest Entry: {largest}")
print(f"Sum of all Entries: {sum}")
print(f"Amount of Even numbered Entries: {even}")
print(f"Amount of Odd numbered Entries: {odd}")
print(f"Amount of Adjacent Duplicates within Data set: {dups}")
'''
TEST ENTRY: 1->10 -----------------------------------------------
Please input a number [enter X to exit]: 1
Please input a number [enter X to exit]: 2
Please input a number [enter X to exit]: 3
Please input a number [enter X to exit]: 4
Please input a number [enter X to exit]: 5
Please input a number [enter X to exit]: 6
Please input a number [enter X to exit]: 7
Please input a number [enter X to exit]: 8
Please input a number [enter X to exit]: 9
Please input a number [enter X to exit]: 10
Please input a number [enter X to exit]: x
Smallest Entry: 1.0
Largest Entry: 10.0
Sum of all Entries: 55.0
Amount of Even numbered Entries: 5
Amount of Odd numbered Entries: 5
Amount of Adjacent Duplicates within Data set: []
TEST ENTRY: 0,0,0,0,0,0,0,1,1,1,3 -------------------------------
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 0
Please input a number [enter X to exit]: 1
Please input a number [enter X to exit]: 1
Please input a number [enter X to exit]: 1
Please input a number [enter X to exit]: 3
Please input a number [enter X to exit]: x
Smallest Entry: 0
Largest Entry: 3.0
Sum of all Entries: 6.0
Amount of Even numbered Entries: 7
Amount of Odd numbered Entries: 4
Amount of Adjacent Duplicates within Data set: [0.0, 1.0]
'''