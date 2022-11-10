def CheckAllCaps(s):
    if(not isinstance(s, str)):
        return False;
    for i in range(0,len(s)):
        if(s[i].islower() or not s[i].isalpha()):
            return False;
    return True

def CheckAllLower(s):
    if(not isinstance(s, str)):
        return False;
    for i in range(0,len(s)):
        if(s[i].isupper() or not s[i].isalpha()):
            return False;
    return True

def CheckChars(s):
    if(not isinstance(s, str)):
        return False;
    for i in range(0,len(s)):
        if(not s[i].isalpha()):
            return False;
    return True

def CheckDigit(s):
    for i in range(0,len(s)):
        if(not s[i].isdigit()):
            return False;
    return True
    

#Take Input
while(True):
    userInput = input("Please input a string: ")
    if(CheckAllCaps(userInput)):
        print("Contains Only Capital letters")
    if(CheckAllLower(userInput)):
        print("Contains Only Lowercase letters")
    if(CheckChars(userInput)):
        print("Contains only Letters")
    if(CheckDigit(userInput)):
        print("Contains only Numbers")
    if(userInput[0].isupper()):
        print("First Letter is Uppercase")
    if(userInput[len(userInput) - 1] == '.'):
        print("Ends with a period!")
        
    sentinal = input("Repeat the process? y/n:")
    if(sentinal == 'n' or sentinal == 'N'):
        break;
    
'''
Please input a string: HELLO
Contains Only Capital letters
Contains only Letters
First Letter is Uppercase
Repeat the process? y/n:y
Please input a string: Hello.
First Letter is Uppercase
Ends with a period!
Repeat the process? y/n:y
Please input a string: 12345
Contains only Numbers
Repeat the process? y/n:y
Please input a string: asdfg
Contains Only Lowercase letters
Contains only Letters
Repeat the process? y/n:n
'''
    