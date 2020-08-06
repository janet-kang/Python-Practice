# Created July 6, 2020
# Asks for input for range of numbers and generates a randome number within that range

# Modules
import random

# Classes
class MinAndMax:
    def __init__(self, min, max):
        self.min = min
        self.max = max

# Functions
def askForInput():
    print('This program generates a random integer between an inputted min and max value.')
    start = input('Min number in range:')
    end = input('Max number in range:')
    inputRange = MinAndMax(start, end)
    return inputRange

def generateRandom(minandmax):
    return random.randint(int(minandmax.min), int(minandmax.max))

def main():
    x = askForInput()
    ret = generateRandom(x)
    return ret

ret = main()
print(ret)


