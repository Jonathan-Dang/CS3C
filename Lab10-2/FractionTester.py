from Fraction import Fraction
from random import randint

def main():
    print("ENTERING BASIC TESTING:")
    f1 = Fraction(1,1)
    f2 = Fraction(2,1)
    print(f"F1: {f1}")
    print(f"F2: {f2}")
    f3 = f2-f1
    print(' '*5, f"[f2 - f1]Expected: 1/1 : {f3}")
    f3 = f1 + f2
    print (' '*5, f"[f2 - f1]Expected: 3/1 : {f3}")
    
    print("EXPECTED: F2 > F1 | Calculation : [f1 > f2]")
    if (f1 > f2):
        print("F1 is greater than f2")
    else:
        print("F2 is greater than F1")
        
    print("EXPECTED: F2 != F1 | Calculation : [f1 == f2]")    
    if (f1 == f2):
        print("f1 == f2!")
    else:
        print("f1 != f2")
    
    print("EXCEPTION HANDLING")
    try:
        f4 = Fraction(1,0)
        print("EXCEPTION WAS NOT CAUGHT")
        exit(0)
    except:
        print(' '*5,"EXCEPTION CAUGHT")
    finally:
        print("Continuing with testing")
        
    print("ENTERING ADVANCED TESTING")
    for i in range(0,100000):
        #a / b and c / d
        #Testing ablity to process between [-10,000,000 ; 10,000,000]
        a = randint(-10000000,10000000)
        b = randint(-10000000,10000000)
        c = randint(-10000000,10000000)
        d = randint(-10000000,10000000)
        try:
            f1 = Fraction(a,b)
            f2 = Fraction(c,d)
            
            #Addition Block
            #============================================#
            resultNum = (a*d) + (c*b)
            resultDen = b * d
            result = resultNum / resultDen
            
            f3 = f2 + f1
            if (f3._numerator / f3._denominator) != result:
                raise Exception(f"Wrong calculation for {f3} as {f2} + {f1} contianed error | RESULT : {result} vs {f3._numerator / f3._denominator}")
            
            #Subtraction Block
            #============================================#
            resultNum = (a*d) - (c*b)
            resultDen = b * d
            result = resultNum / resultDen
            f3 = f1 - f2
            if (f3._numerator / f3._denominator) != result:
                raise Exception(f"Wrong calculation for {f3} as {f1} - {f2} contianed error | RESULT : {result} vs {f3._numerator / f3._denominator}")
            
        except Exception as e:
            if e is ZeroDivisionError:
                continue
            else:
                print(f"ERROR: {a}/{b} and {c}/{d} |>", e)
                return;
    
    print("TESTING COMPLETE")
    

if __name__ == "__main__":
    main()
    
'''
SUCCESSFUL TESTING PERIOD [3/24/2022]
ENTERING BASIC TESTING:
F1: 1/1
F2: 2/1
      [f2 - f1]Expected: 1/1 : 1/1
      [f2 - f1]Expected: 3/1 : 3/1
EXPECTED: F2 > F1 | Calculation : [f1 > f2]
F2 is greater than F1
EXPECTED: F2 != F1 | Calculation : [f1 == f2]
f1 != f2
EXCEPTION HANDLING
      EXCEPTION CAUGHT
Continuing with testing
ENTERING ADVANCED TESTING
TESTING COMPLETE
'''