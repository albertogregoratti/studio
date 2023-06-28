# https://realpython.com/python-exceptions/

# Infinite Loop
#while True:
#    print('This is an infinite loop')

secret_psw = 'al'
attempt = 0
max_attempts = 3
psw = ' '
while psw != secret_psw:
    attempt = attempt + 1
    if attempt <= max_attempts:
        psw = input('Type your password: ')
    else:
        print('Max number of attempts exceeded.')
        break


        