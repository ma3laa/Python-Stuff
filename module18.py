##Reading Console Inputs and Formatting Outputs


#txt = input("Can you see this? Yes or No?")
#print("You said ",txt)


#Trapping for errors

ttt = input("Give me a number: ")
try:
    num = int(ttt)
    print("The number you gave is: ",num)
except ValueError:
    print("Please put in a real number not a string.")


###Formatting Outputs
# {} used for formatting selected parts of a string

salary = 44000
txt = "You make {} dollars a year"
print(txt.format(salary))

#more parameters within the curly brackets
# {field_name:conversion}
#field_name specifies the index number of the argument to the str.format() method
#conversion refers to the conversion code of the data type that you're using with the formatter

# s is for string, d is for decimals, f is for floats  -    {0,s}

print("----------------------------------------------------------------------")
print("Multiple Curly Brackets/Braces")


string = "Dave teaches {} {}."
print(string.format("cyber", "security"))

string = "Dave loves {} {}, and has {} {}"
print(string.format("cyber", "security", 14, "certifications"))


print("----------------------------------------------------------------------")

#Without changing arguments, orderly

string = "Dave loves {1} {3}, and has {2} {0}"
print(string.format("kids", "cyber", 7, "security"))

string = "Bob likes to play {act} and eat {1}{0}."
print(string.format("dogs", "hot",act="games"))

####OR OR OR OR OR OR OR

print("Bob likes to play {act} and eat {1}{0}.".format("dogs", "hot",act="games"))



























