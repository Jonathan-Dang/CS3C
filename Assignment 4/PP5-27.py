from types import NoneType
def main():
    ROMAN_NUMERAL_LITERALS = {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1,
    }
    TOTAL = 0
    TESTCASE = "MCMLXXVIII"
    print(f"Default Test Roman Numeral: {TESTCASE}")
    RomanNumber = input("Please input a roman numeral: ")

    print(RomanNumber)
    skip = False
    for i in range(len(RomanNumber)):
        if (skip):
            skip = False;
        #NoneType is a False value, Like NULL and other like data types
        elif (i + 1 < len(RomanNumber) and ROMAN_NUMERAL_LITERALS.get(RomanNumber[i] + RomanNumber[i + 1])):
            print(RomanNumber[i] + RomanNumber[i + 1], end = ' ')
            TOTAL += ROMAN_NUMERAL_LITERALS[RomanNumber[i] + RomanNumber[i + 1]]
            skip = True
        else:
            print(RomanNumber[i], end = ' ')
            TOTAL += ROMAN_NUMERAL_LITERALS[RomanNumber[i]]
        
    print(f"\nThe Roman Numeral is {TOTAL}")
main()
'''
Default Test Roman Numeral: MCMLXXVIII
Please input a roman numeral: MCMLXXVIII
MCMLXXVIII
M CM L X X V I I I
The Roman Numeral is 1978
'''