##
#    Author: Jonathan Dang
#    Project: PP9-6 : Implement a Car class
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

##
#   Car(Fuel_effeciency = 27.5 ''' 27.5 is just used because that is the last time I saw a real synapsis of a car's Fuel Effeciency ''' )
#       FE: The car's fuel efficiency, defaulted to 27.5
#
class Car:
    def __init__(self, FE = 27.5):
        self._fuel_effeciency = FE
        self._fuel_level = 0
        
    ##
    #   Car.addGas(amount)
    #       Input: The amount, in gallons, of gas the user inputs
    #       Output: The object, but mutated a certain amount of fuel up.
    #
    def addGas(self, amount: float):
        if amount <= 0:
            return;
        self._fuel_level += amount;
        
    ##
    #   Car.drive(miles)
    #       Input: The distance in miles driven
    #       Output: The object, but mutated a certain amount of fuel down.
    #
    def drive(self, miles: float):
        gallonsUsed = miles / self._fuel_effeciency
        if gallonsUsed >= self._fuel_level:
            self._fuel_level = 0
        else:
            self._fuel_level -= gallonsUsed

    ##
    #   Car.getGasLevel()
    #       Input: None
    #       Output: A string version of the fuel, in gallons, left within the car.
    #
    def getGasLevel(self):
        return f"{self._fuel_level} gallons"
    
##
#   main()
#       Function: Driver code
#       NOTE: The sample code is taken DIRECTLY from the book
#
def main():
    Hybrid = Car(50)
    Hybrid.addGas(20)
    Hybrid.drive(100)
    print(Hybrid.getGasLevel())
        
main()

'''
SAMPLE RUN
18.0
'''