##Defining Functions
#Function - Code that only runs when its called
#You can pass data, known as parameters, into a function
#Function is created using "def"


#Calling the module I created under "hello.py"
import hello


def first_function():
    x = 1
    while x < 4:
        print("Hello World!")
        x += 1

first_function()
print("\n")


def second_function(fname):
    print("Hello" + fname)

second_function("Dave")
second_function("Bob")
second_function("Cindy")
print("\n")


hello.greet()




























