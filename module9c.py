#Identity operators
# Used to compare objects, not to see if they are equal
#But to see if they are aactually the same object
#within the same memory location
print("Identity Operators - is ")

a = 2
b = 6
c = a

print(a is b)
print(a is c)

#a is c because c = a, a is obviously not b
print("Identity Operators - is NOT")

a = 2
b = 6
c = a
print(a is not b)
print(a is not c)

#we've gone through how NOT works, just find the answer and reverse it

print("---------------------------------------------------------------------")

print("Membership Operators - in ")

numbers = [1,2,3,4]
print(2 in numbers)

colors = ['blue', 'red', 'yellow']
print('green' in colors)


print("Membership Operators - NOT in")

colors = ['blue', 'red', 'yellow']
print('green' not in colors)

nums = [1,2,3,4]
print(2 not in nums)


print("---------------------------------------------------------------------")

print("Bitwise Operators")

# & = AND
# | = OR
# ^ = XOR


a = 24
b = 60

print(bin(a))
print(bin(b))

print("---------------------------------------------------------------------")

print(" Bitwise - AND")

a = 24
b = 60
print(a & b)

x = 223
y = 111
print(x & y)

print("Bitwise - OR")

a = 24
b = 60
print(a | b)


x = 223
y = 111
print(x | y)

print("Bitwise - XOR")

a = 24
b = 60
print(a ^ b)

x = 223
y = 111
print(x ^ y)










