import random
def sub_random():
    for i in range(1, 11):
        r1 = random.randint(2,12)
        r2 = random.randint(2,12)
        output = str(r1) + ' X ' + str(r2) + ' = '
        print(output)

sub_random()

