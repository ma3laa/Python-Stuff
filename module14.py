#Nesting loops
##The inner loop will be executed each time for each outer one


outer= ["o1", "o2", "o3", "o4"]
nest = ["n1", "n2", "n3"]

for x in outer:
    for y in nest:
        print(x,y)
    print("\n")



num = [1,2,3]
let = ["a", "b", "c"]

for x in num:
    print(x)
    for y in let:
        print(y)
    print("\n")
    
#prints the outer once and the inners all underneath


##PRACTICE TIME




outprac = [1,2,3]
fiveprac = ["a", "b", "c", "d", "e"]

for x in outprac:
    print(x)
    for y in fiveprac:
        print(y)
    print("\n")
