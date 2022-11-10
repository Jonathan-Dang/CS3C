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
from CryptographyToolbox import encode, decode

'''
https://nakamotoinstitute.org/mempool/crypto-anarchy-and-libertarian-entrepreneurship-2/
Sample Excerpt that was encrypted and decrypted is from the website above
Ironic huh
'''
def main():
    #Variable Declariations 
    key = ""
    decrypt = False
    ins = ""
    outs = ""
    files = 0
    
    try:
        for i in range(1,len(argv)):
            arg = argv[i]   #Assigning the current command to variable
            if arg[0] == "-":
                option = arg[1]
                if option == "d":
                    decrypt = not decrypt      #Inverse means to decrypt
                elif option == "k":
                    key = arg[2:]       #Create a substring that represents the key. starts at index 2
                    if key.isspace():
                        usage()
                        return
                else:
                    usage()
                    return
            else:
                files += 1
                if (files == 1):
                    ins = arg
                elif files == 2:
                    outs = arg
    except:
        usage()
        return
                
    if files != 2:
        usage()
        return
    
    insFile = open(ins, "r")    #"r" is a flag to tell the std::open() function to read only
    outsFile = open(outs, "w")  #"w" is a flag to tell the std::open() function to write only, It does reset the file entirely. [OVERWRIDE]
    
    for line in insFile:
        if not decrypt:
            #All processing is done outside of main function.
            outsFile.write(encode(line,key))
        else:
            outsFile.write(decode(line,key))
    
    #Ensures no file corruption.
    insFile.close()
    outsFile.close()
    return 0;

def usage():
    print("Usage: python encryption.py [-d] -k{key} infile outfile")
    
main()

'''
Sample output is in the form of text files provided
'''