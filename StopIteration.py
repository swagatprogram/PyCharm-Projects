# initializing a list having heterogenous values
random_list = ['A', 'S', 5, 'Cat', ['x','y','z']]

# converting the list to an iterator.
iterator_list = iter(random_list)

next_element_1 = next(iterator_list)
print(next_element_1)

next_element_2 = next(iterator_list)
print(next_element_2)

next_element_3 = next(iterator_list)
print(next_element_3)

next_element_4 = next(iterator_list)
print(next_element_4)

next_element_5 = next(iterator_list)
print(next_element_5)

# This will raise StopIteration Exception as the iterator is exhausted.
next_element_error = next(iterator_list)
print(next_element_error)




































