# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members
# Similar to JSON

# Creating simple dictionary
person_a = {
    'first_name': 'Nandy',
    'last_name' : 'Mandy',
    'age': 23
}

# Using contructor
person_b = dict(
    first_name = 'Brad',
    last_name = 'Traversy',
    age = 30
)

print(person_a)
print(person_b)

# Accessign Single value
print(person_a['first_name'])
print(person_a.get('last_name'))

# adding new Key to the Disctionary
person_a['phone'] = '636-053-5414'
print(person_a)

# Get all the keys of the Distionary
print(person_a.keys())
# Get only all the key valeus
print(person_a.items())

# MAking Copy
person_c = person_a.copy()

person_c['city'] = 'San Francisco'
print(person_c)

# Removing and Item
del(person_c['age'])
print(person_c)

person_c.pop('phone')
print(person_c)

# Clear Distionary
person_c.clear()

print(len(person_b))


# List of Dictionaries

people = [
    {'name': 'Nandy Mandy', 'age': 23, 'city': 'San Jose'},
    {'name': 'Brad Traversy', 'age': 36, 'city': 'Boston'},
    {'name': 'Joe Morris', 'age': 28, 'city': 'New York'},
    {'name': 'Shawn Ninja', 'age': 26, 'city': 'London'}
]

print(people)
print(people[1])
print(people[1]['name'])