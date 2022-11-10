#Jonathan Dang | PP2.9 | Assignment 1
#I Jonathan Dang do hereby certify that I have derived no assistance for this project or examination from any sources whatever, whether oral, written, or in print
#except from explicit descrestion from the source material itself.
#P2.9 Improve the program discussed in How To 2.1 to allow input of quarters in addition to bills.
##
#  This program simulates a vending machine that gives change.
#

#INPUT: Money input in terms of bills and quarters, Cost of item in vending machine
#OUTPUT: Change given in bills and quarters.

# Define constants.
PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

# Obtain input from user.
userInput = input("Enter bill value (1 = $1 bill, 5 = $5 bill, etc.): ")
billValue = int(userInput)
userInput = input("Enter quarter value (1 = $0.25, 4 = $1): ")
quarterValue = int(userInput)
userInput = input("Enter item price in pennies: ")
itemPrice = int(userInput)

# Compute change due.
changeDue = PENNIES_PER_DOLLAR * billValue + PENNIES_PER_QUARTER * quarterValue - itemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER

# Print change due.
print("Dollar coins: %6d" % dollarCoins)
print("Quarters:     %6d" % quarters)
'''
#####SAMPLE RUN#####
Enter bill value (1 = $1 bill, 5 = $5 bill, etc.): 1
Enter quarter value (1 = $0.25, 4 = $1): 4
Enter item price in pennies: 200
Dollar coins:      0
Quarters:          0
'''