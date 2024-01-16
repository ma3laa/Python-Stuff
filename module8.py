#Slicing lists

nums = [1, 2, 3, 4, 5, 6]
print(nums[2:5])

#slicing 3,4,5 - item 2 until 5 (doesnt count the one before)


players = ["bob", "steve", "michael", "tom", "eli"]
print("Here are the first three players on my team: ")
for player in players[2:5]:
    print(player.title())

#for looping slicing list


numlist = [1,2,3,4,5,6,7,8,9]
print(numlist[1:8:2])

#items 1 through 8, but every other number (essentially even numbers)

