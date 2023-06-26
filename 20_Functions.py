#********************************
# Functions & Exceptions handling
# Ref: https://www.youtube.com/watch?v=u-OmVr_fT4s
#********************************
# Functions that perform  task
# Functions that calculate and return a value
import sys
##########################################
# Calling a function without an argument that performs a task
##########################################
def printList():    # def stands for definition
    for n in range(10):
        print(n, end=' ', flush=True)
printList()

#########################################
# Calling a function passing an argument
##########################################
def myFunction(par): # par = parameter
    '''When a parameter is present, an argument is mandatory other than if we set a default value'''
    print(f'Hi {par}' )

myFunction('Alb')    # Alb = argument


def myFunction(par=''):
    '''Set a default value avoids an error message when an argument is missing'''
    print(f'Hi {par}' )

myFunction()

##########################################
# Using a value returned by a function
##########################################
def myFunction(par):
    '''The function returns a value'''
    return f'Hi {par}'

message = myFunction('Alb')  # The value returned is used to create a message
print(message)               # The message is print


def myFunction2(n):
    y = n - 5
    return y

if __name__ == '__main__': print(myFunction2(10))

# Keyword arguments Vs Positional arguments
def main3(nome, cognome):
    print('Calling a function with keyword arguments: ', nome + '-' + cognome)
main3(nome = 'al', cognome = 'greg')

def main4(nome, cognome='No surname'):  # Using a default value
    print('Calling a function with positional arguments: ', nome + '-' + cognome)
main4('al', 'greg')
main4('al')


# Multiple Arguments
def printNumbers(*args): # * = it allows accepting any number of arguments
    for number in args:
        print(number)

printNumbers(1,3,5)


def multiply(*args):
    total = 1
    for n in args:
        total = n * total
    return total

print(multiply(2, 4, 7))

# Multiple arguments as key:value pairs
def get_users(**kwargs): # ** = accept any number of key:value pair arguments
    print(kwargs)

get_users(id=1, name='alb', sur='greg') # the result is a dictionary

##################################
# Handling exceptions
###################################
try:
    i = int('ciao')
    #i = 5
except:      # Using except I'm able to catch the error and continue
    print(f'There is an error: {sys.exc_info()}')    # Print the full error message
    print('There\'s an error: {}'.format(sys.exc_info()[1])) # Print just the description (element 1 in the list)
    print(f'There is an error: {sys.exc_info()[1]}')    
else:
    print('No errors: {} '.format(i))
