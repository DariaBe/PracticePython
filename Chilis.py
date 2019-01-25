# 1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out
# that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string
# "\n is the same as pressing the ENTER button)

import datetime


def name_year():
    name = input('Provide your name: ')
    age = int(input('Provide your age: '))
    number = int(input('How many times you want to see a message: '))
    now = datetime.datetime.now()

    hundred_birthday = 100 - age + now.year

    print(('Hello {}, in {} you will be 100! \n'.format(name, hundred_birthday)) * number)
    return hundred_birthday


name_year()


# 2. Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = float(input('Please provide a number: '))
check = num % 2
check_2 = num % 4

if check == 0 and check_2 == 0:
    print('The number that you provide is even and can be divided by 2 and 4.')
elif check == 0:
    print('The number that you provide is even and can be divided by 2')
else:
    print('The provided number is odd.')


num_2 = float(input('Please provide a number that you want to divide: '))
divide_by = float(input('Please provide a number that you want to divide by: '))
check_3 = num_2 % divide_by

if check_3 == 0:
    print('The result of your dividing gives a even number.')
else:
    print('Provided number {} cannot be divided by {} evenly.'.format(num_2, divide_by))

# 3. Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.
#
#

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []
for item in a:
    if item < 5:
        b.append(item)

print(b)

num = int(input('Please, provide a number: '))
c = []
for item in a:
    if item < num:
        c.append(item)

print(c)

# 4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input('Provide a number: '))

x = list(range(1, num + 1))
# print(x)

y = []

for item in x:
    if num % item == 0:
        y.append(item)

print(y)






