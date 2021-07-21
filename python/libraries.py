#Importing a library
import random

print(random.choice([1, 2, 3, 4, 'Hi', True, 50]))
print(random.randint(1, 10))

#Using an alias
import random as r

print(r.randint(1, 11))

#Importing only specific functions/classes
from random import randint, choice

print(randint(1, 100))
print(choice([1, 2, 3, 4, 5, 6]))