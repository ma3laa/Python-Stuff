with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

a = open("demo.txt", "w")
a.write("What has happened now?")
a.close()

##Overwrting not appending "w" not "a"


####PRACTICE

b = open("practicefile.txt", "x")
b.write("some text \n")
b.write("another some text\n")
b.close()

b = open("practicefile.txt", "r")
print(b.read())
b.close()

#---------------------------------------------

b = open("practicefile1.txt", "a")
c = 1
while c < 4:
    b.write("Here is line " + str(c) + "\n")
    c += 1
b.close()

b = open("practicefile1.txt", "r")
print(b.read())
b.close()
