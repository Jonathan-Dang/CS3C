income = int(input("What is your Taxable input: "))
married = input("Are you married? y/n:") == 'y' 
tax = 0
if (married == 'y' or married == 'Y'):
    married = True
else:
    married = False

if(married):
    if(income > 64000):
        tax = 8800 + income*.25   
    elif(income < 64000 and income > 16000):
        tax = 1600 + income*.15
    elif(income <= 16000):
        tax = income*.1
else:    
    if(income > 32000):
        tax = 4400 + income*.25   
    elif(income < 32000 and income > 8000):
        tax = 800 + income*.15
    elif(income <= 8000):
        tax = income*.1
    
print (f"Your Tax is : {tax}")

'''
What is your Taxable input: 8000
Are you married? y/n:n
Your Tax is : 800.0
===================================
What is your Taxable input: 65000
Are you married? y/n:y
Your Tax is : 20650.0
'''