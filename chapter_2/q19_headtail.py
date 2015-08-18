'''		unix commands head and tail		'''


def head(filename):
    res=[]
    for i in open(filename):
	res.append(i)
    head=res[0:5]
    for i in head:
	print i
	
def tail(filename):
    res=[]
    for i in open(filename):
	res.append(i)
    size=len(res)
    tail=res[size-5:size]
    for i in tail:
	print i
print "the head is :"
head('py.txt')
print "the tail is :"
tail('py.txt')
