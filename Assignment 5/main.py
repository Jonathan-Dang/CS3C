#Author: Jonathan Dang
#Assignment: Assignment 5 - Chapter 6
#Academic Honesty Pledge:
#   This assignment was created and written with my own work (Or additionally with the help of this week's partner)
#   and I(we) promise that we held academic integrity at all times during this assignment.
#   If I(we) have been inclined to create something based of off another's work, I(we) will include 
#   specific details pertaining to the assignment within the .py file of each project.
#   I(we) did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
#   of this class.
#   -Jonathan Dang

from random import randint

def PP6_16():
    print("Programing Project 6.16: Finding Longest Sequence")
    print('='*75)
    list = []
    for i in range(20):
        list.append(randint(1,6))
        
    sample = 1; index = -1; max = 0
    for i in range(1, len(list) - 1):
        if list[i] == list[i - 1]:
            sample += 1
        elif list[i] != list[i - 1]:
            if sample > max:
                max = sample;
                index = i
            sample = 1
    
    start = index - max
    for i in range(len(list)):
        if i == start:
            print("(", end=' ')
        elif i == index:
            print(")",end=' ')
        print(list[i],end=' ')
    print()
    print('='*75)
    
    
        

def PP6_15():
    print("Programing Project 6.15: Finding Sequences")
    print('='*75)
    list = []
    for i in range(20):
        list.append(randint(1,6))
        
    inRun = False
    for i in range(len(list) - 1):
        if inRun:
            if list[i] != list[i - 1]:
                print(')',end=' ')
                inRun = False
        if not inRun:
            if list[i] == list[i + 1]:
                print('(',end=' ')
                inRun = True
        print(list[i],end=' ')
    if inRun:
        print(')',end='')
    print()
    print('='*75)
            

def main():
    PP6_15()
    PP6_16()
    
if __name__ == '__main__':
    main()
    
'''
SAMPLE RUN:
Programing Project 6.15: Finding Sequences
===========================================================================
4 3 2 4 ( 5 5 5 ) 2 6 1 4 1 ( 4 4 ) 5 2 5 ( 2 2 )
===========================================================================
Programing Project 6.16: Finding Longest Sequence
===========================================================================
1 2 5 5 3 1 2 4 3 ( 2 2 2 2 ) 3 6 5 5 6 3 1
===========================================================================
'''