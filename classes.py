# A Class is like blueprint for creating objects. An object has properties and methods(functions)
# Associated with it. Almost everything in Python is an object



# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0.0

    # Set balance
    def set_balance(self, balance):
        self.balance = balance

    # Custom Method
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} years old"

    # Another custom method
    def has_birthday(self):
        self.age += 1



# Init User Object
nandy = User('Nandy', 'mauryanarendra09@gmail.com', 23)
nandy = User('Praveen Maurya', 'maurya.praveen@gmail.com', 21)

# Accessing the properties
print(nandy.name)
print(nandy.email)
print(nandy.age)

# Edit Property
nandy.name = "Narendra"

"""print(nandy.name)
print(nandy.email)
print(nandy.age)
print(nandy.greeting())

nandy.has_birthday()

print(nandy.age)

print(nandy.greeting())
print(nandy)"""



print(nandy.name)
print(nandy.balance)
nandy.set_balance(2000.00)
print(nandy.balance)