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
        self._shopTracker_ = [False] * 20 # 1-20 is basically 0-19 in COMPSCI
    
    ##
    #   getCurrentDiscountProgress()
    #       INPUT: NONE
    #       OUTPUT: The Progress to the next discount and if 3 shops has been shopped at.
    #
    def getCurrentDiscountProgress(self):
        return [self._next_discount_, self._checkShopValidity_()]
    
    ##
    #   _checkShopValidity_()
    #       INPUT: NONE
    #       OUTPUT: BOOLEAN | True if there are atleast 3 shops that has been shopped at.
    #
    def _checkShopValidity_(self):
        track = 0
        for val in self._shopTracker_:
            if val is True:
                track += 1
        if track >= 3:
            return True;
        else:
            return False;
    
    ##
    #   getDiscountAvailable()
    #       INPUT: NONE
    #       OUTPUT: Whether or not the next purchase will have the discount
    #
    def getDiscountAvailable(self):
        return self._discountNow_
        
    ##
    #   makePurchase(price: float , shop: int)
    #       INPUT: Price of the item and the shop number they shopped at.
    #       OUTPUT: NONE
    #
    def makePurchase(self, price: float, shop: int):
        if price <= 0:
            raise RuntimeError("Invalid Price Inputed")
        if shop < 1 or shop > 20:
            raise RuntimeError("Invalid Shop Inputed")
        if (self._discountNow_):
            newPrice = price - 10.0;
            self._next_discount_ += newPrice
            self._discountNow_ = False;
        else:
            self._next_discount_ += price
            self._shopTracker_[shop - 1] = True
            self._discountReached_()
        
    ##
    #   _discountReached_()
    #       INPUT: NONE
    #       OUTPUT: Mutates the object to check discount availability
    #
    def _discountReached_(self):
        if self._next_discount_ - 100 >= 0 and self._checkShopValidity_():
            self._discountNow_ = True
            self._next_discount_ %= 100 #Ensures that we are below 100 every check.

#DEPRECATED [Only Valid for use of PP9.26]
'''def _Test_Customer_():
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
        
    print("COMPLETED TESTING")'''

def _Test_MultiShop_Customer_():
    print("=====ENTERING BASIC TESTING BLOCK=====")
    c1 = Customer()
    c1.makePurchase(34, 1)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: [34,FALSE] | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: FALSE | {c1.getDiscountAvailable()}")
    c1.makePurchase(34, 2)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: [68,FALSE] | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: FALSE | {c1.getDiscountAvailable()}")
    c1.makePurchase(34, 3)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: [2,TRUE] | {c1.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: TRUE | {c1.getDiscountAvailable()}")
    print("=====EXITING BASIC TESTING BLOCK=====")
    
    print("=====ENTERING EXCEPTION BLOCK=====")
    try:
        c2 = Customer()
        c2.makePurchase(1000,-1)
        print("RUNTIME EXCEPTION WAS NOT CAUGHT! [FAILED TEST]")
    except RuntimeError as e:
        print("RUNTIME EXCEPTION CAUGHT! [SUCCESSFUL TEST]")
    finally:
        print("=====EXITING EXCEPTION BLOCK=====")
        
    print("=====ENTERING ONLY 2 SHOPS BLOCK=====")
    c3 = Customer()
    c3.makePurchase(price = 50,shop = 1)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: [50,FALSE] | {c3.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: FALSE | {c3.getDiscountAvailable()}")
    c3.makePurchase(price = 50,shop = 2)
    print(f"EXPECTED CURRENT DISCOUNT PROGRESS: [100,FALSE] | {c3.getCurrentDiscountProgress()}")
    print(f"EXPECTED DISCOUNT AVAILABLITY: FALSE | {c3.getDiscountAvailable()}")
    print("=====EXITING ONLY 2 SHOPPS BLOCK=====")
    print("COMPLETED TESTING")
    

_Test_MultiShop_Customer_()
    
'''
SAMPLE RUN
=====ENTERING BASIC TESTING BLOCK=====
EXPECTED CURRENT DISCOUNT PROGRESS: [34,FALSE] | [34.0, False]
EXPECTED DISCOUNT AVAILABLITY: FALSE | False
EXPECTED CURRENT DISCOUNT PROGRESS: [68,FALSE] | [68.0, False]
EXPECTED DISCOUNT AVAILABLITY: FALSE | False
EXPECTED CURRENT DISCOUNT PROGRESS: [2,TRUE] | [2.0, True]
EXPECTED DISCOUNT AVAILABLITY: TRUE | True
=====EXITING BASIC TESTING BLOCK=====
=====ENTERING EXCEPTION BLOCK=====
RUNTIME EXCEPTION CAUGHT! [SUCCESSFUL TEST]
=====EXITING EXCEPTION BLOCK=====
=====ENTERING ONLY 2 SHOPS BLOCK=====
EXPECTED CURRENT DISCOUNT PROGRESS: [50,FALSE] | [50.0, False]
EXPECTED DISCOUNT AVAILABLITY: FALSE | False
EXPECTED CURRENT DISCOUNT PROGRESS: [100,FALSE] | [100.0, False]
EXPECTED DISCOUNT AVAILABLITY: FALSE | False
=====EXITING ONLY 2 SHOPPS BLOCK=====
COMPLETED TESTING
'''