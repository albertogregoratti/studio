# General doc: https://docs.python.org/3/library/index.html
# Tutorial @: https://www.guru99.com/python-tutorials.html
# Tutorial @: https://www.w3schools.com/python/default.asp
# Tutorial @: https://www.geeksforgeeks.org/python-programming-language/

#***********************
# Arithmetic Operators
#***********************
# // Integer Division
# %  Remainder(Modulo)
# ** Exponent

x = 5//2
y = 5%2
z = 5**2
print(x, y, z)
print('5//2 = {}, 5%2 = {}, 5**2 = {}'.format(x, y, z))

#***********************
# Boolean Operators
#***********************
a = True
b = False
r = (1, 2, 3, 4)
s = range(1, 4)

if a and b:
    print('The condition is True!')
else:
    print('The condition is false!')

if a or b:
    print('The condition is True!')
else:
    print('The condition is false!')

i = 5
if i in r:
    print('{} is in the list!'.format(i))
else:
    print('{} is NOT in the list!'.format(i))

i = 5
if i in s:
    print('{} is in the range!'.format(i))
else:
    print('{} is NOT in the range!'.format(i))

#************************************
# Conditions and Comparison operators
#************************************
x = 5
y = 6
if x < y:
    print(str(x) + " is lower than " + str(y))
elif x == y:
    print(str(x) + " and " + str(y) + ' are equal')
elif x != y:
    print(str(x) + " and " + str(y) + ' are not equal')
else:
    print(str(x) + " is bigger than " + str(y))

# Conditional assignment
c = False
s = 'This is really true!' if c else 'This is not true at all!' # Note: else is mandatory
print(s)
