first_name = "Nandy"
last_name = "Mandy"
age = 23

# Concatination
print('Hello, I am ' + first_name + last_name + ' and I am ' + str(age))

#String Formatting

# Arguments by Position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {0}, {2}'.format('a', 'b', 'c'))

# Arguments By Name
print('Hello, I am {name} and I am {age} years old.'.format(name='Nandy', age='37'))

# Arguments by placeholders
print(f'Hello, I am {first_name} and I am {age} years old.')

# String Methods
s = 'hello There world'

# Capitalize first letter
print(s.capitalize())
# Upper Case
print(s.upper())
# Lower Case
print(s.lower())
# Case Swapping
print(s.swapcase())
# Length of String
print(len(s))
# Replace something 
print(s.replace('world', first_name))
# Count number of characters or substring
sub = 'H'
print(s.count(sub))
# Starts with
print(s.startswith('hello'))
# End With
print(s.endswith('d'))
#Split
print(s.split())
# Find Position
print(s.find('r'))
# is all alphanumberic
print(s.isalnum())
# iS ALL ALPHABETIC
print(s.isalpha())
# Is all numeric
print(s.isnumeric())
