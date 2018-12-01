# A function is a block of code which runs when it is called.
# In python, we do not use parameters and curly brackets, we use indentation with tabs or spaces


# Create Function
def sayHello():
    print('Hello World')

def sayName(name):
    print('Hello ' + name)

# With default value
def say_Name(name = 'Sam'):
    print('Hello ' + name)

# Function with o parameters passed
sayHello()

# Function with Parameters passed
sayName('Narendra')

# With default value
say_Name('Narendra')
say_Name()

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(2, 5.6))

# Another function
def addOneToNum(num):
    # Scope of this function variable is only used inside inside the function
    num += 1
    return num

print(addOneToNum(2.3))


# A lambda function is a small anoynmous function.
# A lambda function can take any number of arguements, but can only have one expression.
# Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(2,4.5))

addOneToNum = lambda num1 : num1 + 1
print(addOneToNum(3.3))