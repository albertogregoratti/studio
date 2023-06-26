#********************************
# Data Structures
# https://www.w3schools.com/python/python_lists.asp
# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4
#********************************
#########################################################################################
# Lists (lists are mutable). It is the equivalent of an array in other programming languages.
# It is represented by square brackets. Note that in a list we have both index and value.
#########################################################################################

li = [1, 2, 30, 4]
print (li)  # print all values in a list
print('Element in position 1: ', li[1]) # print the value corresponding to index/position = 1
print('Elements in positions 1 to 3 (excluding 3): ', li[1:3])
print('Max value in th list: ' , max(li))

# The enumerate function allows using both index and values
for index, val in enumerate(li):
    print(index, val)

li.sort()   # arranging a list of integers in ascending order
print('Sorted list: ', li)

print(li[-1]) # negative index to start from the end of the list

for item in li: print(item)
  
for item in li: print('nb in list: ' + str(item))

for item in li: print('nb in list: {}'.format(item))

for i in range(len(li)):
    print(li[i])

# TRansforming a list into a string (, separated)
li_str = ', '.join(li)
print(li_str)

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

######################################################################################
# Tuple (it's like a list but immutable)
######################################################################################
tu = (1, 2, 3)
print ('Print tuple element: ', tu[0])

mylist = list(tu)   # converts a tuple object into a list
print('Converting a tuple into a list: ', mylist)

#######################################################################################
# Dictionary (a searchable sequence of key-value pairs)
#######################################################################################
di = {'first': 1, 'sec': 'due', 'third': ['uno', 'due']}
for i in di: print(i)        # it prints the keys

print(di['sec'])   # Accessing a value: it prints the value corresponding to the key

myValue = di.get('sec')  # same result but using the method get
print('Getting a value using get(): ', myValue)

for k, v in di.items(): print(k, v)     # Looping through all keys and values
    
for k, v in di.items(): print(v)        # Looping through all values
    
# Dictionaries can be built using the dictionary constructor
di1 = dict(first = 1, sec = 2, third = 3)
print(di1)
for k in di1.keys(): print(k)
for v in di1.values(): print(v)
for k, v in di1.items(): print(k, v)

# Set (like a list but doesn't allow duplicates and are unordered
s = {1, 3, 5}

# To 'pretty' print a dictionary, import pprint module and use pprint.pprint(dictionaryName)

###########################################################################################
# Working with string and json data using the json module
# https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47
###########################################################################################
import json
import pprint

people_string = '''
{
"people": [
    {   "name": "al",
        "age": 50,
        "email": ["al.g@g.com", "alg.y.com"]
    },
        {   "name": "isa",
        "age": 49,
        "email": ["isa.b@g.com"]
    }
]
}
'''

people_dict = json.loads(people_string) # the loads method loads a string into a dictionary
# print(type(people_dict))
# pprint.pprint(people_dict)
people_list = people_dict['people']
for p in people_list: print(p)
for p in people_list: print(p['name'])

for p in people_list: del(p['age'])
# for p in people_list: print(p)
new_people_string = json.dumps(people_dict, indent=2, sort_keys=True)   # the dumps method convert a dictionary object into a string

print(new_people_string)