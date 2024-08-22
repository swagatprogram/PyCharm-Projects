tempList = ["Welcome", "to", "scaler", "docs.", "Have", "a", "great", "day" ]

# fetching complete list
list1 = tempList[::]
print("list1:", list1)

# fetching list from 0th index to 6th index
list2 = tempList[0:6]
print("list2:",list2)

# jumping every third element from start to end
list3 = tempList[::3]
print("list3:",list3)

# jumping to every 2nd element starting from 1st index until 5th index
list4 = tempList[1:5:2]
print("list4:",list4)

# 8th index from end to 5th index from end
list5 = tempList[-8:-5]
print("list5:",list5)

# jumping every 3rd element in reverse
list6 = tempList[::-3]
print("list6:",list6)

# alternate implementation of list4
list7 = tempList[-7:-3:-2]
print("list7:",list7)

































