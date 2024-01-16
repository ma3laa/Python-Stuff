#Using Math and Random Modules

#all of the modules listed at https://docs.python.org/3/library/math.html

import math

num = int(input("Give me a number to find the square root for"))
print(math.sqrt(num))


#random modules https://docs.python.org/3/library/random.html

import random

print("Printing random number")
print(random.random())

#returns a float number between 0.0 and 1.0


print("Printing random integer ",random.randint(0,1000))
#random integer between 0 and 1000

print("Printing random integer ",random.randrange(0,500,2))
#random number within a range of 0 and 500 (only even)
