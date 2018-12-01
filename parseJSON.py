# JSON is commonly used with data API's. Here how we can parse JSON into a Python Dictionary

import json

# Sample JSON
userJSON = '{"first_name": "Nandy", "last_name": "Mandy", "age": 23}'

# Parse to dictionary
user = json.loads(userJSON)
print(user)


# dictionary to JSON
car = {'make': 'Aston', 'model': 'Martin', 'year': 1990}
carJSON = json.dumps(car)
print(carJSON)