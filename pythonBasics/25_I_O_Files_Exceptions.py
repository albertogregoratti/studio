# File path: use forward slashes
file_fd_credentials_f = 'C:/Dev/fd/fd_credentials.json'


with open(file_fd_credentials_f, 'r') as f_f:
    content = f_f.read()
    print(content)

# Managing exception: basic
fake_file = 'C:/Dev/fd/fd_creds.json'

try:
    with open(fake_file, 'r') as rf:
        content = rf.read()
        print(content)
except FileNotFoundError:
    print('File not found!')
print('finished')

# Managing exception: best practices. The try block should only contain code that may cause an error.
# Any code that depends on the try block running successfully should be placed in the else block.
try:
    with open(fake_file, 'r') as rf:
        content = rf.read()
except FileNotFoundError:
    pass    # Failing silently: the program just continue running in case of an error message
else:
    print(content)
    print('finished')
print('finished')

# Using Exception
try:
    with open(fake_file, 'r') as rf:
        content = rf.read()
except Exception  as e: # In case of we are not sure about the exception to catch, use Exception.
    print(e, type(e))   
    pass    
else:
    print(content)
    print('finished')
print('finished')
