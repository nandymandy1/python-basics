# A loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Jhon', 'Brad', 'Shawn', 'Nandy', 'Alex', 'Doe']

for person in people:
    print('Current Person: ',person)

# Break out of the loop
for person in people:
    if person == 'Nandy':
        break
    print('Current Person: ',person)

# Continue
for person in people:
    if person == 'Alex':
        continue
    print('Current Person: ',person)

# Range
for i in range(len(people)):
    print('Current Person: ',people[i])

# Manual range
for i in range(0, 11):
    print('Number', i)

# While loop
count = 0 
while count <=10:
    print('Count: ', count)
    count += 1