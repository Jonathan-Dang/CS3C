from random import shuffle

def scramble(word):
    substr = word[1:len(word)-1:]
    l = list(substr)
    shuffle(l)
    return word[0] + "".join(l) + word[len(word) - 1]

def main():
    str = input("Please input a single word: ")
    shuffledStr = scramble(str)
    print(shuffledStr)
    
main()

'''
Please input a single word: Middle  
Mdidle
'''