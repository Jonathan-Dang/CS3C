##
#   Assignment: Lab 7
#       Group 4: Jonathan Dang, Youhong Tong, Jihoon Son
#
##
#Academic Honesty Pledge:
#   This assignment was created and written with my own work (Or additionally with the help of this week's partner)
#   and we promise that we held academic integrity at all times during this assignment.
#   If we have been inclined to create something based of off another's work, we will include 
#   specific details pertaining to the assignment within the .py file of each project.
#   we did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
#   of this class.
#   -Jonathan Dang
import string
def fileReader(filename):
    try:
        ins = open(filename,"r")
        outs = open("Modified-Book.txt", "w")
        #1. Remove all words less than 3
        #2. remove all duplicate words
        #3. print out # of remaining unique words
        record = set()
        for line in ins:
            words = line.split(' ')
            for word in words:
                if not word.isnumeric():
                    #Standardize the word, lower and no punc
                    #.translate of the standard library function of string maps characters to the given parameter.
                    #str.maketrans essentially makes that "map" in which it dictates what characters are translated to what 
                    #other characters. Of course, this function itself is not a mutator, so resetting the variable
                    #is required. [https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string]
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    word = word.lower()
                    word = word.strip()
                    #Check within our record for unique words
                    if len(word) > 3 and not word.isnumeric():
                        if word not in record:
                            record.add(str(word))
                            outs.write(word)
                outs.write(' ')
            outs.write('\n')
        print(f"Final Amount of Unique Words: {len(record)}")
    except Exception as e:
        print ("Error: " + str(e))
    finally:
        ins.close()
        outs.close()

def main():
    print("="*70)
    print("START")
    print("="*70)
    filename = input("Input a filename: ")
    fileReader(filename=filename)
    print("="*70)
    print("END")
    print("="*70)

main()