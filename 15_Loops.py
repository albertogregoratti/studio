#***********************
# Loops
#***********************
# While: it does use a condition to control the loop 
somewords = ['io','mi ','chiamo','al']
i = 0
while (i <= 3):
    print(somewords[i])
    i += 1

secret_psw = 'secret'
psw = ' '
while psw != secret_psw:
    psw = input('Type your password: ')

# For: it does use a sequence to control the loop
i = 0
for i in somewords:
    print(i)
    
for i in range(1, 9):
    print(i)

# Loops controls: break
psw = ' '
count = 0
max_attempts = 3

while psw != secret_psw:
    count = count + 1
    if count <= max_attempts:
        psw = input('Type your password: ')
    else:
        print('Max number of attempts exceeded.')
        break

# Loops controls: continue
while psw != secret_psw:
    count = count + 1
    if count <= max_attempts:
        if count == 2: continue     # Skip count = 2 and continue 
        psw = input('Type your password: ')
    else:
        print('Max number of attempts exceeded.')
        break

# Enumerate function: is used for numbering members in a list
li = ('al', 'ma', 'an')
for i, n in enumerate (li):
    print(i, n)

