# List is a collection which is ordereed and changeable. Allows duplicate members

# numbers = [1,2,3,4,5]
# Using Constructor
numbers = list((1,2,3,4,5))

print(type(numbers))
print(numbers)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(fruits)

# Get Value at first index
print(fruits[1])
# length of List
print(len(fruits))

# Adding a value to list
fruits.append('Mangos')
print(fruits)

# Removing Value From List
fruits.remove('Grapes')
print(fruits)

# Insert it to Specific Position
fruits.insert(2, 'Strawberry')
print(fruits)

# Remove from Specific Position
fruits.pop(1)
print(fruits)

# Reverse the order of list
fruits.reverse()
print(fruits)

# Sort List
fruits.sort()
print(fruits)

# Reverse Sort
fruits.sort(reverse=True)
print(fruits)

