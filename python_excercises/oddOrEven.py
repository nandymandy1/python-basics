# Odd or Even
import random
"""
num1 = int(input("Enter a number"))

if(num1 % 2 == 0):
    print("The number is even")
else:
    print("The Number is odd")
"""
# Cas see kid teenager or Adult

"""
age = int(input("Enter your age"))

if age > 19:
    print("He is a adult")
elif age < 19 and age > 12:
    print("He is a Teenage")
else:
    print("He is a Kid")
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
# Traditional method
for i in range(len(a)):
    if a[i] < 5:
        print(a[i])
"""

"""
a2 = []
num = int(input('Enter a number '))
# looping through list
for temp in a:
    if temp < num:
        a2.append(temp)

print(a2)
"""
"""

num = int(input('Enter a number '))
divisors = []

for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)

print(divisors)

"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in b:
    for j in a:
        if i == j:
            c.append(i)

print(c)
"""
"""
# Palindrome
str1 = input("Enter a string ")

str2 = str1[::-1]

if str1 == str2:
    print("Its a palindrome String")
"""
"""
# Only even Elements of string in one line
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]
print(b)
"""
"""
# Rock Paper Scissors

def rps():
    print("Enter S for Scissors, P for Paper and T for Stone")
    a = input("Enter Player One Option ")
    b = input("Enter Player Two Option ")

    if a == 'S' and b == 'T':
        print("Player two won")
    elif a == 'T' and b == 'S':
        print("Player one won")
    elif a == 'P' and b == 'S':
        print("Player two won")
    elif a == 'S' and b == 'P':
        print("Player one won")
    elif a == 'P' and b == 'T':
        print("Player one won")
    elif a == 'T' and b == 'P':
        print("Player two won")

    ch = input("Do you want to continue. Press y to continue otherwise x ")
    if ch == 'y':
        rps()

rps()
"""
"""
# Guess work accuracy
def guess():
    usr_num = int(input("Enter a number between 1 to 9 "))
    rand_int = random.randint(1, 10)
    print(rand_int)
    if usr_num == rand_int:
        print("You have guessed it correctly")
    else:
        if usr_num < rand_int:
            print("You very low")
        if usr_num > rand_int:
            print("You very high")

    opt = input("do you want to continue then type yes otherwise type exit ")
    if opt == 'yes':
        guess()


guess()
"""

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
c = []

for i in a:
    for j in b:
        if i == j:
            if i in c:
                continue
            else:
                c.append(i)

print(c)
