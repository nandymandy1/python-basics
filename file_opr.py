# Open file
myFile = open('myfile.txt', 'w')

# Get file info/contents
print('Name: ', myFile.name)
print('Is Colosed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I Love Python')
myFile.write('and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Reading a file
myFile = open('myfile.txt', 'r+')
text = myFile.read()
print(text)