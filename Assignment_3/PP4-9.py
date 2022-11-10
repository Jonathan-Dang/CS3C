'''
•• P4.9 Write a program that reads a word and prints the word in reverse. For example, if the user provides the input "Harry", the program prints
		yrraH
'''
while(True):
    str = input("Please input a word [To Exit, Please enter X]: ")
    if (str == "X" or str == "x"):
        break;
    revList = []
    revStr = ""
    for c in str:
        revList.insert(0,c)
    for c in revList:
        revStr += c;
        
    print(revStr)
print("END OF PROGRAM")

'''
Argument: Test
Please input a word [To Exit, Please enter X]: Test
tseT
Please input a word [To Exit, Please enter X]: x
END OF PROGRAM
'''