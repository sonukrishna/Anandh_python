'''		unique elements in a list		'''


def unq(lst):
    res=[]
    for i in lst:
	if i not in res:
		res.append(i)
    print "the unique list is:",
    return res


aa=[1,2,5,6,45,6,75,6,5,4,75,22,1,2,5,6,75]
print unq(aa)
