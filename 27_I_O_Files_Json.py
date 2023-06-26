##########################################################################################################
# Loading a json file
###########################################################################################################
import json
import pprint
import os, sys

file_fd_credentials = 'C:/Dev/fd/fd_credentials.json'

# Method 1
fi = open(file_fd_credentials, 'r')
content = fi.read()
print('Input file content: ', content)

with open(file_fd_credentials, 'r') as fi:
    content = fi.read()
print('Input file content: ', content)
# loads
dict_obj = json.loads(content)  # loads is used to load a Json string into a Python dictionary
print('Json string decoded into a dictionary: ', dict_obj)

print("Domain value",  dict_obj.get('domain'))  # get domain value
print("Domain value",  dict_obj['domain'])  # get domain value
print("Domain value",  dict_obj.keys())  # get all keys
print("Domain value",  dict_obj.values())  # get all values

print('Dictionary key-value pairs: ')
for k, v in dict_obj.items(): print(k, v) 

# Method 2: using the json.load method
with open('C:/Dev/fd/fd_credentials.json', 'r') as j_file:
    content = json.load(j_file)     # load method loads a json file into a python object

print(type(content))
pprint.pprint(content)
print(content['api_key'])

# dumps and dump
# Converting Python data to JSON is called an Encoding operation. 
# Encoding is done with the help of JSON library method - dumps()
#
# load
with open(file_fd_credentials, 'r') as fi:  # load decodes the Json string into a Python dictionary
    content = json.load(fi)
print('Input file content: ', content)

x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print('Json string:')
print(sorted_string)

with open('text_test3.json', 'w') as fo:
    fo.write(sorted_string)
fo.close()
print('Json file created.')

# How creating a JSON file of the dictionary using the function dump()
with open('text_test4.json', 'w') as fo:
    json.dump(x, fo)  # write json data 'x' into file 'fo'
fo.close()
print('Json file created.')

# Dump other data structures into a json file
li1 = [5, 6, 7]
li2 = (8, 9, 10)
with open('text_test5.json', 'w') as fo:
    json.dump(li1, fo)  # dumps a list
    fo.write('\n')      # insert a new line
    json.dump(li2, fo)  # dumps a tuple
    

