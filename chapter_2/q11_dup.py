'''	the duplicates in alist		'''


def dup(lst):
    res=[]
    res1=[]
    for i in lst:
	if lst.count(i)>1:
		res.append(i)
    for i in res:
	if i not in res1:
	    res1.append(i)
    print "the duplicates in %s is:" % lst,
    print res1


aa=[1,2,1,3,4,3,45,4,5,4,5]
dup(aa)
