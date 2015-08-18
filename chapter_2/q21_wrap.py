'''		wrap  the file as per the given length		'''



def wrap(filename,n):
    for i in open(filename):
	if len(i)>n :
	    print i[0:n]
	    print i[n:len(i)]
	else:	
	    print i

wrap('she.txt',30)
