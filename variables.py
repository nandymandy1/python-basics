#   A variable is a container for a value, which can be fo various types
#   This a multiline comment or docstring (used to define a function purpose)
#   can be single or double quotes.

#    Variable Rules
    # -  Variable name are case senstive (name and NAME are different variable)
    # -  Must Start with a latter or an underscore
    # -  Can have number but can not start with one

#   print('Hello world')
#   print(1)
# Integer
x = 1
print(x)

# Float
y = 4.5
print(y)

# String
name = "Narendra"
print(name)

# Boolean
is_cool = True

#  Multiple Assignment
x1, y1, name1, is_cool1 = (1,4.5,"Nandy Mandy", False)

#Print
print(x1, y1, name1, is_cool1)

# Basic mathematics
a = x1 + x
print(a)

# Check Type
print(type(y1))

# Type Casting
x = str(x)
print(type(x))

y = int(y)
print(y)
print(type(y))

x2 = float(x1)
print(type(x2))
print(x2)