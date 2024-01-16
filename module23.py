#Handling Exceptions
##A type of error that occurs when the syntax is corect but the Python code
##results in an error

#Good Example is:
#0 obviously cannot be divided by 0, however syntax is correct

#print(0/0)

#Try and Except are keywords in python used to catch exceptions

import sys

try:
    print(0/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")


try:
    num = int(input("Enter a number 1-10"))
except ValueError:
    print("Please use numbers only")
    sys.exit()

print("You entered the number", num)


#Finally and else clause (both optional)

try:
    data = something_that_can_go_wrong
except IOError:
    handle_the_exception_error
else:
    doing_different_exception_handling
finally:
    print("Goodbye World..")
