s = "welcome to scaler"

# reversing complete string
s1 = s[::-1]
print("s1:",s1)

# reversing complete string by stepping to every 2nd element
s2 = s[::-2]
print("s2:",s2)

# reversing from 10th index until start, 'stop' index here automatically will be till starting of the string
s3 = s[10::-1]
print("s3:",s3)

# reversing from end until 10th index, 'start' index will automatically be the first element
s4 = s[:10:-1]
print("s4:",s4)

# reversing from 16th index till 10th index
s5 = s[16:10:-1]
print("s5:",s5)

# this will return empty, as we're not reversing here. But NOTE that this 'start' cannot be greater than ‘stop’ until & unless we're reversing
s6 = s[11:2]
print("s6:",s6)

# reversing from 14th index from the end until 4th index from the end.
s7 = s[-4:-14:--1]
print("s7:",s7)

































