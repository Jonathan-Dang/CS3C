'''
•• P4.3 Write programs that read a line of input as a string and print
		a.Only the uppercase letters in the string. √
		b.Every second letter of the string. √
		c.The string, with all vowels replaced by an underscore. √
		d.The number of digits in the string. √
		e.The positions of all vowels in the string. √
'''
#ASSUMPTIONS: Line of input will be interpreted as a string ended by a \n
#           : Every Second Letter is every word seperated by a space[' ']in the second space

VOWELS = ['a','e','i','o','u','y','A','E','I','O','U','Y']
secondLetter = []
upperCaseLetters = []
numOfDigits = 0
strNoVowels = ""
posOfVowels = []
flag = False
i = 0

while(True):
    str = input("Please input a line [To Exit, Please enter X]: ")
    if (str == "X" or str == "x"):
        break;
    for c in str:
        if (VOWELS.count(c)):
            posOfVowels.append(i)
            strNoVowels += '_'
        else:
            strNoVowels += c
        
        if (c.isupper() and upperCaseLetters.count(c) == 0):
            upperCaseLetters.append(c)
            
        if (c.isdigit()):
            numOfDigits += 1
        
        if ((i >= 2 and str[i - 2] == ' ' and str[i - 1].isalpha() and str[i] != ' ') or i == 1):
            secondLetter.append(c)
        i += 1
    
    print(str)
    print(strNoVowels)
    print(posOfVowels)
    print(upperCaseLetters)
    print(f"Number of Digits within the String: {numOfDigits}")
    print(f"2nd Letters of each word: {secondLetter}")
print("END OF PROGRAM")
'''
Arguement: This is a Sentence.
Please input a line [To Exit, Please enter X]: This is a Sentence.
This is a Sentence.
Th_s _s _ S_nt_nc_.
[2, 5, 8, 11, 14, 17]
['T', 'S']
Number of Digits within the String: 0
2nd Letters of each word: ['h', 's', 'e']
Please input a line [To Exit, Please enter X]: x
END OF PROGRAM
'''