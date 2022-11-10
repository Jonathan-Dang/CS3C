##
#   Assignment: Lab 10
#       Group 6
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

class Customer:
    def __init__(self):
        self._next_discount_ = 0.0; #Indicating to the heap that this value is a float
        self._discountNow_ = False;
    
    ##
    #   getCurrentDiscountProgress()
    #       INPUT: NONE
    #       OUTPUT: The Progress to the next discount
    #
    def getCurrentDiscountProgress(self):
        return self._next_discount_;
    
    ##
    #   getDiscountAvailable()
    #       INPUT: NONE
    #       OUTPUT: Whether or not the next purchase will have the discount
    #
    def getDiscountAvailable(self):
        return self._discountNow_
        
    ##
    #   makePurchase(price: float)
    #       INPUT: Price of any item above the cost of 0
    #       OUTPUT: NONE
    #
    def makePurchase(self, price: float):
        if price <= 0:
            raise RuntimeError("Invalid Price Inputed")
        if (self._discountNow_):
            newPrice = price - 10.0;
            self._next_discount_ += newPrice
            self._discountNow_ = False;
        else:
            self._next_discount_ += price
            self._discountReached_()
        
    ##
    #   _discountReached_()
    #       INPUT: NONE
    #       OUTPUT: Mutates the object to check discount availability
    #
    def _discountReached_(self):
        if self._next_discount_ - 100 >= 0:
            self._discountNow_ = True
            self._next_discount_ %= 100 #Ensures that we are below 100 every check.
            
def _Test_Customer_():
    print("=====ENTERING BASIC TESTING BLOCK=====")
    
    c1 = Customer();
    c1.makePurchase(100)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: 0 | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: TRUE | {c1.getDiscountAvailable()}")
    c1.makePurchase(100)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: 90 | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: FALSE | {c1.getDiscountAvailable()}")
    c1.makePurchase(100)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: 90 | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: TRUE | {c1.getDiscountAvailable()}")
    print("=====EXITING BASIC TESTING BLOCK=====")
    
    print("=====ENTERING EXCEPTION BLOCK=====")
    try:
        c2 = Customer()
        c2.makePurchase(-1000000)
        print("RUNTIME EXCEPTION WAS NOT CAUGHT! [FAILED TEST]")
    except RuntimeError as e:
        print("RUNTIME EXCEPTION CAUGHT! [SUCCESSFUL TEST]")
    finally:
        print("=====EXITING EXCEPTION BLOCK=====")
        
    print("COMPLETED TESTING")

_Test_Customer_()
    
'''
SAMPLE RUN
=====ENTERING BASIC TESTING BLOCK=====
EXPECTED CURRENT DISCOUNT PROGRESS: 0 | 0.0  
EXPECTED DISCOUNT AVAILABLITY: TRUE | True   
EXPECTED CURRENT DISCOUNT PROGRESS: 90 | 90.0
EXPECTED DISCOUNT AVAILABLITY: FALSE | False 
EXPECTED CURRENT DISCOUNT PROGRESS: 90 | 90.0
EXPECTED DISCOUNT AVAILABLITY: TRUE | True   
=====EXITING BASIC TESTING BLOCK=====
=====ENTERING EXCEPTION BLOCK=====
RUNTIME EXCEPTION CAUGHT! [SUCCESSFUL TEST]
=====EXITING EXCEPTION BLOCK=====
COMPLETED TESTING
'''