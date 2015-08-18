"""flatten a nested list """


def flatten(a,result=None):
    if result is None:
	result=[]
    for x in a:
	if isinstance(x,list):
	    print x
	    flatten(x,result)
	else:
	    result.append(x)
    return result


print flatten([1,[2,3,4],[5,6],7])

