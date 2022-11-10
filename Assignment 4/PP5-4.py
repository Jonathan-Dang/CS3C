def middle(s):
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1:len(s)//2 + 1:]
    else:
        return s[len(s)//2]
    
def main():
    str = input("Please enter two words, one even and one odd in length seperated by a space: ")
    strlist = str.split(' ')
    string1 = strlist[0]
    string2 = strlist[1]
    print(middle(string1))
    print(middle(string2))
    
main()

'''
Please enter two words, one even and one odd in length seperated by a space: Middle Old
dd
l
'''