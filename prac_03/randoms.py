import random

"""
Prints a random number between 5 and 20 inclusive
Smallest number is 5, and largest number is 20
"""
print(random.randint(5, 20))

"""
Smallest number is 3, and largest number is 9
It will not produce 4 because the random number has a range 3 to 10 and skip size of 2
"""
print(random.randrange(3, 10, 2))

"""
Smallest number is 2.5, and largest number is 5.5
"""
print(random.uniform(2.5, 5.5))

"""
Prints random number between 1-100 inclusive
"""
print(random(1, 100))
