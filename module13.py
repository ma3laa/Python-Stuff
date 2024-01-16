#While loops

a = 1
while a < 6:
    print(a)
    a += 1


x = "Hello World"
y = 1
while y <= 3:
    print(x)
    y += 1


#Now using continue Statements

x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

#4 is skipped, can use other operators to exclude everything but 4, e.g. (!=) 


a = 1
while a < 14:
    print(a)
    if a == 4:
        break
    a += 1

# even though the condition is 14, the condition 4 breaks it from the if statement

##PRACTICE TIME BABY


gj = "Great Job!"
y = 0

while y < 3:
    print(gj)
    y += 1



x = 1

while x < 10:
    print(x)
    if x == 6:
        break
    x += 1
















