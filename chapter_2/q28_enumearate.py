'''	the function prints the index and value of the given list	'''

def enum(lst):
    return [(x,lst[y])for x in range(len(lst))for y in range(len(lst))if x==y]

aa=list('abrakadabra!')
print enum(aa)
