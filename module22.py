#Using Keyword and Positional Arguments
##Position of the arguments can be changed

def greet(name,msg="How are you today?"):
    print("Hey",name +","+msg)

#2 keyword arguments

greet(name = "Dave", msg = "How do you do?")

#2 Keyword arguments (out of order)

greet(msg = "How do you do?", name = "Dave")

#1 Positional, 1 Keyword argument

greet("Dave",msg = "How do you do?")


