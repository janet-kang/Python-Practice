# Created July 6, 2020
# Rolls a die and gives a random number between 1-6

# Modules
import random

# Function definitions
def roll_dice():
    return random.randint(1,6)

ret = roll_dice()
print(ret)