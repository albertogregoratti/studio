# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# Doc @: https://www.w3schools.com/python/python_regex.asp
# Doc @: https://www.guru99.com/python-regular-expressions-complete-tutorial.html
import re

# The split() function returns a list where the string has been split at each match (\s = matches a blank space):
phrase = 'we are splitting the words'
print('Split: ', re.split('\s', phrase))

# The search() function searches the string for a match, and returns a Match object if there is a match.
found = re.search('are', phrase)
if found != None:
    print('Search OK')
else:
    print('Not found')

# The sub() function replaces the matches with the text of your choice
x = re.sub('\s','9', phrase)
print('Reaplaced 9 to space: ', x)

# The Match Object is an object containing information about the search and the result.
found = re.search('are', phrase)
print(found)

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match