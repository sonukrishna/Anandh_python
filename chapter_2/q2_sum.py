'''		sum of a list		'''


def sum1(lst):
    s=0
    for i in lst:
	s=s+i
    print "the sum of list is:",
    print i

lst1=list(range(0,1000,33))
sum1(lst1)
