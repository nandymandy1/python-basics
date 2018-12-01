# A module is basically a file containing a set of functions to include in your application. Thre are core python modules, modules you can install
# using pip package manager (including django and Flask) as well as custom modules

# Core Module

# DATE MODULE
# import datetime
import time
from datetime import date
# PIP Module
import camelcase
today = date.today()
print(today)

# TIME MODULE
timestamp = time.time()
print(timestamp)

# CamelCase Module
camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))

# Custom module import
# import validator
from validator import validate_email

email = '@gmail.com'
if validate_email(email):
    print("Email is valid")
else:
    print("Email is invalid")