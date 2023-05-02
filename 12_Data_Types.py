#********************************
# Data Types
#********************************
# Strings
# Doc: https://docs.python.org/3/library/stdtypes.html#string-methods
name = 'al'
print(type(name))   # returns the variable type
print('my name is: ' + name)
print('my name is: {}'.format(name))
# Since a string is an object of String class, methods can be applied
# The format() method formats the specified value(s) and insert them inside the string's placeholder {}

nameC = 'al'.capitalize()
nameCC = 'al'.upper()
nameL = 'al'.lower()
print(nameC)
print(nameCC)
print(nameL)
print('ciao'.capitalize())

# Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}
myName = 'Al'
myAge = '57'
txt1 = "My name is {fname}, I'm {age}".format(fname = myName, age = myAge)
txt2 = "My name is {0}, I'm {1}".format(myName, myAge)
txt3 = "My name is {}, I'm {}".format(myName, myAge)

# Doc: https://docs.python.org/3/library/string.html
bigNumber = 5 * 12456
print('{:,}'.format(bigNumber)) # Format numbers as ,000

# Splitting a string into words: it returns a list of words
s = 'Name Surname'
print(s.split())
#Joining strings
l = s.split()
l2 = ';'.join(l)    # This joins the words in the list changing the separator to ';'
print(l2)

# Numeric

nb = 23
print('number: ' + str(nb))
print('number: {}'.format(nb))

# Prompting for a numerical input
in_str = input('Please insert your age: ')

print('Your age is: ' + in_str)
print('your age is: {}'.format(in_str))


# Functions doc: https://docs.python.org/3/library/functions.html

