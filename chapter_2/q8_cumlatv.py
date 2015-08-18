'''	cumulative sum of a list	'''


def cum(lst):
    res=[]
    sum=0
    for i in lst:
	sum=sum+i
	res.append(sum)
    print "the cumulative sum of %s is:" % lst,
    return res


aa=list(range(1000,2000,159))
print cum(aa)
