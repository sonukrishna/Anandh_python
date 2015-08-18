''' function takes 2 numbers as command line arguments and prints its sum '''


import sys
def add(x1,x2):
    return int(x1)+int(x2)

print add(sys.argv[1],sys.argv[2])

