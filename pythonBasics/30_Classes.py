#***********************
# Classes
#***********************
import os
# In Python a Class is a definition and an object is an instance of a class

# Definition of a class
class Papero:           # Name of the class
    walking = 'I\'m walking!'   # Variable
    
    def quack(self):    # Method: a function define a Class method. Note the argument for a method is 'self'.
        print('Quaaack')
        
    def walk(self):
        print(self.walking)

def main():
    paperino = Papero()     # A variable called paperino which is an object of the class Papero
    paperino.quack()
    paperino.walk()
    
if __name__ == '__main__': main()





