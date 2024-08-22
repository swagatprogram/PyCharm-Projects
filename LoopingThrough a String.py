# Python program to iterate over a string using a for loop
string_var = 'Interviewbit'
# Method 1: Iterating over a string
for character in string_var:
    print(character, end = ' ')
print('\n')

# Method 2: Iterating using indexing
for i in range(len(string_var)):
    print(string_var[i], end=' ')
print('\n')

# Method 3: Iterating using enumerate()
for k, v in  enumerate(string_var):
    print(v, end=' ')




























