#***********************
# File I/O
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.youtube.com/watch?v=Uh2ebFW8OYM
#***********************
import json
import os           # Doc @: https://www.geeksforgeeks.org/os-module-python-examples/
from os import path # The OS module in python provides functions for interacting with the operating system
import shutil       # Doc @: https://www.guru99.com/python-copy-file.html
import time

infile = open('text_test1.txt', 'r')    # The Open function returns a file object. It takes a file name and returns an object
outfile = open('text_test2.txt', 'w')
# r = read, w = write (creates a file), a = append mode (creates a file if it does not exist or append if it does exist)

# print(infile.read())    # The read method returns the whole content of a file

for line in infile:     # We can get one line at time instead of the full file in memory
    print(line)
    print(line.rstrip())
    #outfile.writelines(line)
    outfile.write(line)
    #print(line.rstrip(), file=outfile) # another way to write content into a file
outfile.close()
infile.close()
print('It\'s done')


# Reading a Json file

file_fd_credentials = 'C:/Dev/fd/fd_credentials.json'

# read credentials
with open(file_fd_credentials, "r") as read_file:   # using with makes the code cleaner and the file is closed automatically at the end
    data=read_file.read()

# decoding the Json string
obj = json.loads(data)
print(obj)
for k, v in obj.items(): print(k, v) 

api_key = obj['api_key']
domain = obj['domain']
password = obj['password']

print('key: {} domain: {} password: {} '.format(api_key, domain, password))
    
# os.path useful functions
print('Current directory:', os.getcwd())    # Current working directory
myFile = 'text_test1.txt'
#os.rename(myFile, 'text_test_new.txt')      # Rename a file
print('File \'', myFile, ' has been renamed')

# using path.exists() function to check whether a file exists
myFile = 'text_test1.txt'
print('File \'' + myFile + '\' exists.' + str(path.exists(myFile)))

#os.error
try:    # if the file does not exist, it would generate an IOError
    myFile = 'text_test_fake.txt'
    f = open(myFile, 'r')
    content = f.read()
    f.close
except IOError: # this way the script continues with the line after the try/except
    print('Problem opening file \'', myFile, '\'')

# shutil useful functions
src = path.realpath('text_test1.txt')
print('Full path of: ', src)
p, f = path.split(src)
print('Path: ', p, ' File: ', f)

backup_file = src + '.bak'  # Appends .bak to the file
shutil.copy(src, backup_file)   # Create a copy of src file assigning the new name
print('Created backup-file: \'', backup_file, '\'')

ft = time.ctime(path.getmtime('text_test1.txt'))    # Get modification time of a file
print('File time: ', ft)

################################################################
# Working with images

with open('c:/Temp/IMG_0942 corr.jpg', 'rb') as file_r:
    with open('c:/Temp/img_copy.jpg', 'wb') as file_w:
        brick_size = 4096
        r_brick = file_r.read(brick_size)
        while len(r_brick) > 0:
            file_w.write(r_brick)
            r_brick = file_r.read(brick_size)
