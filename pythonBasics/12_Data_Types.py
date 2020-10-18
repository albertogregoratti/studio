#********************************
# Data Types
#********************************
# Strings
# Doc: https://docs.python.org/3/library/stdtypes.html#string-methods
name = 'al'
print('my name is: ' + name)
print('my name is: {}'.format(name)) # Since a string is an object of String class, methods can be applied

nameC = 'al'.capitalize()
nameCC = 'al'.upper()
nameL = 'al'.lower()
print(nameC)
print(nameCC)
print(nameL)
print('ciao'.capitalize())

n = len('alberto')
print('Lenght: {}'.format(n))   # {} = positional argument
print('Lenght: {myString}'.format(myString = n))

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

in_str = input('Please insert your age: ') # Prompting for a numerical input
in_nb = int(in_str)


# Functions doc: https://docs.python.org/3/library/functions.html

