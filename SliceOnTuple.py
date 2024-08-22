temptuple =  ("Welcome", "to", "scaler", "docs.", "Have", "a", "great", "day")
tuple1 = temptuple[::] # fetching complete tuple
print("tuple1:",tuple1)

tuple2 = temptuple[0:6] # fetching tuple from 0th index to 6th index
print("tuple2:",tuple2)

tuple3 = temptuple[::3]  # jumping every third element from start to end
print("tuple3:",tuple3)

tuple4 = temptuple[1:5:2] # jumping to every 2nd element starting from 1st index until 5th index
print("tuple4:",tuple4)

tuple5 = temptuple[-8:-5]  # 8th index from end to 5th index from end
print("tuple5:",tuple5)

tuple6 = temptuple[::-3] # jumping every 3rd element in reverse
print("tuple6:",tuple6)

tuple7 = temptuple[-7:-3:2]  # alternate implementation of tuple4
print("tuple7:",tuple7)































