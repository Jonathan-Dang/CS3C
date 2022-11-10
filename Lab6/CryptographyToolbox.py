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

#Alphabet constant in both upper and lower case. To be used within the defined functions below
LOWERALPHA = "abcdefghijklmnopqrstuvwxyz"
HIGHERALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

##
#   SINGLETON(str):
#       Input: A single word String
#       Output: The given word but with no repeating letters
#           EX: Cookie => Cokie
#
def SINGLETON(str):
    strList = list(str)
    for i in range(len(strList) - 1):
        for t in range(len(strList) - 1):
            if strList[i] == strList[t] and i is not t:
                strList.pop(t)
    return "".join(strList)

##
#   CreateDict(list1, list2):
#       Input: Two lists
#       Output: a dictionary with key = list1 and object = list2
#           EX: [1,2,3] , [a,b,c] => {1:a, 2:b, 3:c}
#
def CreateDict(list1, list2):
    res = {}
    for i in range(len(list1)):
        if (not res.get(list1[i])):
            res[list1[i]] = list2[i]
    return res

##
#   lowerCaseCypherset(key):
#       Input: a Key
#       Output: An alphabet cypher set to reflect the key and requirements from PP7.20 | LOWERCASE
#
def lowerCaseCypherset(key):
    tempstr = str.lower(key)
    lowerList = list(LOWERALPHA)
    lowerList.reverse()
    lowerCypher = list(tempstr)
    for c in lowerList:
        if lowerCypher.count(c) == 0:
            lowerCypher.append(c)
    return lowerCypher

##
#   upperCaseCypherset(key):
#       Input: a Key
#       Output: An alphabet cypher set to reflect the key and requirements from PP7.20 | UPPERCASE
#
def upperCaseCypherset(key):
    tempstr = str.upper(key)
    upperList = list(HIGHERALPHA)
    upperList.reverse()
    upperCypher = list(tempstr)
    for c in upperList:
        if upperCypher.count(c) == 0:
            upperCypher.append(c)
    return upperCypher

##
#   encode(message,key):
#       Input: A message in the form of a string and a key
#       Output: The message that has been encoded with the key
#
def encode(message, key):
    filteredKey = SINGLETON(key)
    upperset = upperCaseCypherset(filteredKey)
    lowerset = lowerCaseCypherset(filteredKey)
    uppers = CreateDict(list(HIGHERALPHA),upperset)
    lowers = CreateDict(list(LOWERALPHA),lowerset)
    string = ""
    for c in message:
        if str.isupper(c):
            string += uppers[c]
        elif str.islower(c):
            string += lowers[c]
        else:
            string += c
    return string

##
#   decode(message,key):
#       Input: A message in the form of a string that has been encoded and the key to decode it
#       Output: The message that has been decoded with the key | {DOES NOT CHECK FOR CORRECTNESS}
#
def decode(message, key):
    filteredKey = SINGLETON(key)
    upperset = upperCaseCypherset(filteredKey)
    lowerset = lowerCaseCypherset(filteredKey)
    uppers = CreateDict(upperset,list(HIGHERALPHA))
    lowers = CreateDict(lowerset,list(LOWERALPHA))
    string = ""
    for c in message:
        if str.isupper(c):
            string += uppers[c]
        elif str.islower(c):
            string += lowers[c]
        else:
            string += c
    return string