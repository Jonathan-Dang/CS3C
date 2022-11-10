#Jonathan Dang | PP2.16 | Assignment 1
#I Jonathan Dang do hereby certify that I have derived no assistance for this project or examination from any sources whatever, whether oral, written, or in print
#except from explicit descrestion from the source material itself.
#PP2.16 Write a program that reads a five-digit positive integer and breaks it into a sequence of individual digits. For example, the input 16384 is displayed as
#			1 6 3 8 4

#INPUT: 5 digit number
#OUTPUT: 5 numbers printed, space seperated


while(True):
    userInput = input("Please enter a 5 digit number[10000 -> 99999]: ")
    if(len(userInput) != 5):
        print("Invalid input")
    else:
        break;
first = userInput[0]; second = userInput[1]; third = userInput[2]; fourth = userInput[3]; fifth = userInput[4]
print(first + ' ' + second + ' ' + third + ' ' + fourth + ' ' + fifth)
'''
Please enter a 5 digit number[10000 -> 99999]: 16384
1 6 3 8 4
'''