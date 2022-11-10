##
#   Author: Jonathan Dang
#   Project: PP8-25
#   Date: 3/14/2022
#   BUG: I am unable to sort the csv file using csv or the given sorted function. OR reading the csv doesn't register
#           scientific notation so my code does "Work" but doesn't show it properly.
#
'''
This assignment was created and written with my own work and I promise that I 
held academic integrity at all times during this assignment.
If I have been inclined to create something based of off another's work, I will include 
specific details pertaining to the assignment within the .py file of each project.
I did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
of this class.
-Jonathan Dang

CSV documentation : https://docs.python.org/3/library/csv.html
sorted documentation : https://docs.python.org/3/library/functions.html?highlight=sorted#sorted
'''

import csv
from operator import itemgetter

def main():
    try:
        filename = input("Please input a valid CSV file directory: ")
        
        showcaseAmount = int(input("Please enter an amount for display: "))
        if showcaseAmount <= 0 or showcaseAmount is None:
            showcaseAmount = 5
        
        print(obtainCsvKeys(filename)[1::])
        ViewingSet = []
        while 'done' not in ViewingSet:
            ViewingSet.append(input(f"Please input the desired catergories for the {showcaseAmount} high-low display [Enter \"done\" when finished]: "))
        ViewingSet.pop()
        
        dict = csvToDictionary(filename)
        for category in ViewingSet:
            #sorted sorts from least to greatest
            dict = sorted(dict, key = itemgetter(category))
            
            fulfilledTop = 0
            fulfilledBottom = 0
            pos = 0
            print(f"Top {showcaseAmount} in {category}")
            while True:
                item = dict[pos]
                if item[category].isdigit():
                    print(' '*5, end = '')
                    print(item["country"], end = ' ')
                    print(item[category])
                    fulfilledTop += 1
                if fulfilledTop == showcaseAmount:
                    break;
                pos += 1
                
            pos = 0
            print(f"Bottom {showcaseAmount} in {category}")
            while True:
                item = dict[pos]
                if "NA" not in item[category]:
                    print(' '*5, end = '')
                    print(item["country"], end = ' ')
                    print(item[category])
                    fulfilledBottom += 1
                if fulfilledBottom == showcaseAmount:
                    break;
                pos -= 1
    except Exception as e:
        print(e)
        return;
    
    
    
##
#    csvToDictionary(filename)
#         Input: a valid CSV file
#         Output: a list containing multiple dictionaries.
#
def csvToDictionary(filename):
    if filename[-4::] != ".csv":
        raise Exception(f"Wrong File Type! {filename[:-4:]} -> {filename[-4::]} Not .csv")

    with open(filename) as insfile:
        dict = csv.DictReader(insfile)
        listOfDictionaries = []
        for line in dict:
            listOfDictionaries.append(line)
        return listOfDictionaries
    
##
#   obtainCsvKeys(filename)
#       Input: A valid CSV File Directory
#       Output: a list containing the keys
#
def obtainCsvKeys(filename):
    if filename[-4::] != ".csv":
        raise Exception(f"Wrong File Type!! {filename[:-4:]} -> {filename[-4::]} Not .csv")
    
    with open(filename) as insfile:
        Read = csv.reader(insfile)
        for line in Read:
            return line;
        
##
#    printFormattedDictionary(dictionary)
#         Input: a dictionary
#         Output: Prints to screen a dictionary formatted differently than default print
#
def printFormattedDictionary(dictionary):
    for key in dictionary:
        print(key)
        print(' '*5, end = '')
        print(dictionary[key])
        
main()

'''
Please input a valid CSV file directory: Assignment_8\cia_factbook.csv
Please enter an amount for display: 5
['area', 'birth_rate', 'death_rate', 'infant_mortality_rate', 'internet_users', 'life_exp_at_birth', 'maternal_mortality_rate', 'net_migration_rate', 'population', 'population_growth_rate']
Please input the desired catergories for the 5 high-low display [Enter "done" when finished]: population     
Please input the desired catergories for the 5 high-low display [Enter "done" when finished]: done
Top 5 in population
     Cook Islands 10134
     Benin 10160556
     Saint Vincent and the Grenadines 102918
     Dominican Republic 10349741
     Burundi 10395931
Bottom 5 in population
     Cook Islands 10134
     Haiti 9996731
     Hungary 9919128
     Sweden 9723809
     Azerbaijan 9686210
'''