#Author: Jonathan Dang
#Assignment: Lab 6
#Academic Honesty Pledge:
#   This assignment was created and written with my own work
#   and I promise that we held academic integrity at all times during this assignment.
#   If I have been inclined to create something based of off another's work, I will include 
#   specific details pertaining to the assignment within the .py file of each project.
#   I did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
#   of this class.
#   -Jonathan Dang

from sys import argv

def main():
    #Constant alphabet
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    #Using a dictionary to act as a C++ map to count the frequency of a character | {Could also use an array or list and the ord() function}
    counter = dict(zip(list(ALPHA),[0]*26))
    letterCount = 0
    
    #Try and Except to check for valid/invalid input
    try:
        ins = argv[1]
    except:
        usage()
        return
    
    #Goes through each character and checks if it is an alphabet character
    #Then increments the value in the dictionary
    insFile = open(ins, "r")
    for line in insFile:
        lowerLine = str.lower(line)
        for c in lowerLine:
            if (c.isalpha()):
                counter[c] = counter[c] + 1
                letterCount += 1
                
    insFile.close()
    
    #Display the obtained data to console
    width = 5
    for c in ALPHA:
        if (width != 0):
            print(f"{c}:{(counter[c]/letterCount)*100:.0f}%", end = " ")
            width -= 1
        else:
            print(f"{c}:{(counter[c]/letterCount)*100:.0f}%")
            width = 5

def usage():
    print("Usage: py codeCracker.py inputfile")

main()

'''
Sample Output
>py codeCracker.py Encoded.txt

a:4% b:0% c:4% d:1% e:2% f:6%
g:3% h:12% i:1% j:2% k:10% l:6%
m:6% n:0% o:3% p:6% q:5% r:2%
s:2% t:3% u:3% v:4% w:1% x:1%
y:8% z:5%
'''