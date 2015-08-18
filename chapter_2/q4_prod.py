"""		product of a list		"""


def prod(lst):
    p=1
    for i in lst:
	p=p*i
    return p

n=raw_input("enter the length of the list:")
l=[]
for i in range(int(n)):
    l.append(int((raw_input("enter the element %d :"% i))))
print "the product is:",
print prod(l)
