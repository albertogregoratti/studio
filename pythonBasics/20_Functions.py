#********************************
# Functions & Exceptions handling
#********************************
import sys
# Calling a function passing an argument

def myFunction(n):
    print(n)

myFunction(53)

# Calling a function without an argument
def printList():
    for n in range(10):
        print(n, end=' ', flush=True)
printList()
print('')

# Using a value returned by a function 
def main():
    x = myFunction2(25)
    print('Value returned by a function: ', x)

def myFunction2(n):
    y = n - 5
    return y

if __name__ == '__main__': main() 

# Keyword arguments Vs Positional arguments
def main3(nome, cognome):
    print('Calling a function with keyword arguments: ', nome + '-' + cognome)
main3(nome = 'al', cognome = 'greg')

def main4(nome, cognome='No surname'):  # Using a default value
    print('Calling a function with positional arguments: ', nome + '-' + cognome)
main4('al', 'greg')
main4('al')


# Arguments list
def main2():
    ls = ('arg1', 'arg2', 'arg3')   
    sub(*ls)

def sub(*args):
    for i in args:
        print(i)
main2()

# Handling exceptions
try:
    i = int('ciao')
    #i = 5
except:      # Using except I'm able to catch the error and continue
    print(f'There is an error: {sys.exc_info()}')    # Print the full error message
    print('There\'s an error: {}'.format(sys.exc_info()[1])) # Print just the description (element 1 in the list)
    print(f'There is an error: {sys.exc_info()[1]}')    
else:
    print('No errors: {} '.format(i))
