'''	cumulative product of a list		'''


def cum_product(lst):
    res=[]
    prod=1
    for i in lst:
	prod=prod * i
	res.append(prod)
    print "the cumulative product of %s is:"% lst,
    return res


aa=list(range(1,31,6))
print cum_product(aa)
