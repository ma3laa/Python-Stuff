#Reading Files
print("Reading Files")
print("--------------------------------------------------------------")
#To read or write to file, you need to open it - "open()" function

a = open("demo.txt", "r")
print(a.read())

#file object = open(file_name [, access_mode])
#mode argument is optional; 'r' will be assumed if it's omitted

## DIFFERENT MODES CAN BE USED FOR DIFFERENT REASONS
## R = READ, R+ = READ AND WRITE, W = WRITE, A = APPEND


print("--------------------------------------------------------------")
print("Reading Files - Readline")

a = open("demo.txt", "r")
print(a.readline())
a.close()

a = open("demo.txt", "r")
print(a.readline(2))
a.close()

print("--------------------------------------------------------------")
print("Reading Files - 'With'")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

print("--------------------------------------------------------------")
print("Reading Files - Write")

a = open("demo.txt", "a")
a.write("\nHere is another line in our text file")
a.close()

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)











