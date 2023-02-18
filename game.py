import random
ranNum = random.randint(10000, 100000)
print(ranNum)
# this will generate a random number from 10000 to 100000


def intake():
    uTemps = 0
    while True:
        try:
            uNum = int(input("Type a number:"))
            if (uNum > ranNum):
                print("my number is smaller than yours")
                print()
                uTemps += 1
            elif (uNum < ranNum):
                print("my number is greater than yours")
                print()
                uTemps += 1
            elif (uNum == ranNum):
                print("you got me")
                print()
                uTemps += 1
                print(f"You took {uTemps} attempt(s) to find my number")
        except:
            print("Type numbers only")


intake()
