##
#    Author: Jonathan Dang
#    Project: PP9-10 : Implement a VotingMachine class
#    Date: 3/21/2022
#
'''
This assignment was created and written with my own work 
and I promise that I held academic integrity at all times during this assignment.
If I have been inclined to create something based of off another's work, I will include 
specific details pertaining to the assignment within the .py file of each project.
I did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
of this class.
-Jonathan Dang
'''
import string
import random

##
#   VotingMachine(parties)
#       Input: A list of parties to vote for, defaulted to the two primary political parties of the USA as of 2022
#
class VotingMachine:
    def __init__(self, parties: list = ["Democrats", "Republicans"]):
        self._votingSelections = parties;
        self._ballets = [0]*len(self._votingSelections)
        
    ##
    #   VotingMachine.vote(party)
    #       Input: The name of the party that the user is voting for.
    #       Output: The object records the vote internally
    #
    def vote(self, Party: string):
        try:
            index = self._votingSelections.index(Party)
            self._ballets[index] += 1
            return True;
        except ValueError as e:
            return False;
    
    ##
    #   VotingMachine.clearBallots()
    #       Input: None
    #       Output: Clears the ballots
    #
    def clearBallots(self):
        for i in range(0,len(self._ballets)):
            self._ballets[i] = 0
            
    ##
    #   VotingMachine.getParties()
    #       Input: None
    #       Output: Returns the available parties to vote for.
    #
    def getParties(self):
        return self._votingSelections;
            
    ##
    #   VotingMachine.getBallotResults()
    #       Input: None
    #       Output: The results of the voting duration in dictionary form.
    #
    def getBallotResults(self):
        return dict(zip(self._votingSelections, self._ballets));
        
##
#   VotingDriver(VotingMachine, Iterations)
#       Input: A VotingMachine object and the amount of total votes in the simulation
#       Output: Provides a simulation of the amount of people voting for something. 
#
def VotingDriver(VotingMachine: VotingMachine, iterations: int = 8850000):
    parties = VotingMachine.getParties()
    numOfParties = len(parties)
    for i in range(iterations):
        party = random.randint(0,numOfParties - 1)
        VotingMachine.vote(parties[party])
    
    results = VotingMachine.getBallotResults()
    print(results)
    VotingMachine.clearBallots()
    return;

##
#   main()
#       Function: Driver code
#    
def main():
    vote = VotingMachine()
    VotingDriver(vote)
    
main()

'''
SAMPLE RUN
{'Democrats': 4424386, 'Republicans': 4425614}
'''