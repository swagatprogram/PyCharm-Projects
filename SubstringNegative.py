s = "Welcome to scaler"
# -x means xth element from the end.
print("indexing syntax without step:", s[-16 : -4])

# using step to fetch every 2nd character from start index until end index
print("indexing syntax with step:", s[-16 : -4 : 2])

# replicating above code using slice object
sliceObj = slice(-16, -4)
print("slice object without step:", s[sliceObj])

sliceObj = slice(-16, -4, 2)
print("slice object with step:", s[sliceObj])



































