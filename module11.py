#Working with IF statements

x = 12
y = 3

if x > y:
    print("X is greater than y")
elif x == y:
    print("X is equal to Y")
else:
    print("X is not greater than y")
    
#elif and else are "Compound Conditional Statements"

#Creating a program without using if statements that use options

req_opt = ['leather', 'sunroof']

if "leather" in req_opt:
    print("Nice leather interior")
if "alarm" in req_opt:
    print("Keeping the bad guys away")
if "sunroof" in req_opt:
    print("Letting the sun in")

print("\nFinished making your car")


#PRACTICE

temp = 12

if temp > 28:
    print("Wow it's hot outside")
elif temp == 28:
    print("Thats a nice temperature")
else:
    print("The weather isn't great, keep the AC on")
    
