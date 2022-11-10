import random
STRAT1 = 0 #STRAT1 is swapping
STRAT2 = 0 #STRAT2 is sticking
for i in range(10000):
    choices = [False, False, False]
    car = random.randint(0,2)
    choices[car] = True
    userChoice = random.randint(0,2)
    if car is not userChoice:
        STRAT1 += 1;
    else:
        STRAT2 += 1;
print(f"Times that Strategy 1 was Successful: {STRAT1}")
print(f"Times that Strategy 2 was Successful: {STRAT2}")

strat1WinPercentage = STRAT1/10000 * 100
strat2WinPercentage = STRAT2/10000 * 100

print(f"Strategy 1: {strat1WinPercentage:.2f}%")
print(f"Strategy 2: {strat2WinPercentage:.2f}%")

'''
Times that Strategy 1 was Successful: 6731
Times that Strategy 2 was Successful: 3269
Strategy 1: 67.31%
Strategy 2: 32.69%
'''