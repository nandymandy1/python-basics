# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
# fruit_tuple = ('Apple', 'Mango', 'Orange')

# Using Constructor
fruit_tuple = tuple(('Apple', 'Mango', 'Orange'))

print(fruit_tuple)

# Get Single Value
print(fruit_tuple[1])

# Tuple with one value should have trailing comma
fruit_tuple_2 = ('Apple',)
print(fruit_tuple_2)
print(len(fruit_tuple_2))

# Delete the Tuple
del fruit_tuple_2



# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)
# Check for a value in set
print('Apple' in fruit_set)
print('Apples' in fruit_set)
# Adding Into set
fruit_set.add('Grape')
print(fruit_set)
# Removing from set
fruit_set.remove('Grape')
print(fruit_set)
# Clear the set
fruit_set.clear()
print(fruit_set)
# Delete the set
del fruit_set
print(fruit_set)
