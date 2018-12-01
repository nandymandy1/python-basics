# If else conditions to decide to do something based on something beign true or false

x = 6
y = 7


# Comparision Operators (==, !=, >, <, >=, <=) -- Used to compare values
if x == y:
    print(f'{x} is equal to {y}')

# IF/Else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')



# Elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')


# Nested If
if x > 2:
    if x <=10:
        print(f'{x} is less than 10 but greater than 2')


# Logical operators (and, or, not) -- Used to combine conditional statements

# and 
if x > 2 and x <=10:
    print(f'{x} is less than 10 but greater than 2')

#or
if x > 2 or x <=10:
    print(f'{x} is less than 10 or greater than 2')


#not
if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership Operators (not, no in) -- Membership operators are used to test if a sequence is presented in an object

# in 
numbers =  [1,2,3,4,5,7]

if x not in numbers:
    print(x in numbers)

#  Identity Operators (is, is not) -- Compare the objects, not if they are equal, but if they are actually the same object, with the same memory locations:
x = 7
y = 7

if x is y:
    print(x is y)

x = 7
y = 8

if x is y:
    print(x is not y)