##Modifying Lists

employees = ["Mark", "Tommy", "Jeremy", "Carrie", "Debbie"]
employees[0] = "Thomas"
print(employees)

#Indexing (changing 0 in list) Mark as Thomas

employees = employees + ["Jim"]
print(employees)

#Using operators ( + ) to modify the list

###   I'm not gonna do it, but 2 separate lists can be concatenated together
###   into a single list with all items from both lists


employees.insert(1, "Dave")
print(employees)

#inserting an item within a list

del employees[2]
print(employees)

#delete item from the list, by knowing the order of the list

employees.remove("Jim")
print(employees)

#delete an item from the list, without knowing the order

for x in employees:
    print(x)

#using a for loop to print out each item within the list

if "Carrie" in employees:
    print("Yes, Carrie does work here")
else:
    print("Carrie does not work here")

#used to determine whether carrie item is within the list

print(len(employees))

#gives you the amount of items in list



