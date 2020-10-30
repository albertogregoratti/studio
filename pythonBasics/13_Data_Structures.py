#********************************
# Data Structures
#********************************
# Lists (lists are mutable). It is the equivalent of an array in other programming languages.
# It is represented by square brackets

li = [1, 2, 30, 4]
print('Element in position 1: ', li[1]) 
print('Elements in positions 1 to 3 (excluding 3): ', li[1:3])
print('Max value in th list: ' , max(li))

li.sort()   # arranging a list of integers in ascending order
print('Sorted list: ', li)

for i in li: print(i)
  
for i in li: print('nb in list: ' + str(i))

for i in li: print('nb in list: {}'.format(i))

lir = range(5)  # We can create a sequence using range
for i in lir: print(i)

lir2 = range(2, 10, 2) # Start - End - Step
for i in lir2:
    print(i)

#Lists are searchable
animals = ['lion', 'dog', 'cat']
myOne = animals.index('dog')
print('Search a list:', animals[myOne])

if 'dog' in animals:
    print('Testing if a value is in a list: OK')
else:
    print('Testing if a value is in a list: No')

# Tuple (it's like a list but immutable)
tu = (1, 2, 3)
print ('Print tuple element: ', tu[0])

mylist = list(tu)   # converts a tuple object into a list
print('Converting a tuple into a list: ', mylist)

    
# Dictionary (a searchable sequence of key-value pairs)

di = {'first': 1, 'sec': 2, 'third': 3}
for i in di: print(i)        # it prints the keys

print(di['sec'])   # Accessing a value: it prints the value corresponding to the key

myValue = di.get('sec')
print('Getting a value using get(): ', myValue)

for k, v in di.items(): print('key: ', k, ' - value: ',v)     # Looping through all keys and values
    
for k, v in di.items(): print('value: ',v)        # Looping through all values
    
# Dictionaries can be built using the dictionary constructor
di1 = dict(first = 1, sec = 2, third = 3)
print(di1)
for k in di1.keys(): print(k)
for v in di1.values(): print(v)
for k, v in di1.items(): print(k, v)

# Set (it's like a list but doesn't allow duplicates and are unordered
s = {1, 3, 5}