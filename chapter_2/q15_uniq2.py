'''		find unique elements in a list		'''


def uniq(lst):
    res=[]
    for i in lst:
	x=list(set(lst))
    print x


aa=[1,2,1,2,1,2,3,4,5,6,2,5,6]
uniq(aa)
