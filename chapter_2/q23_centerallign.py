'''		allign the sentences into center		'''



def center(filename):
    res=[]
    res1=[]
    with open (filename)as f:
	res.extend(f)
	for i in res:
	    res1.append(len(i))
	p=max(res1)
	print p
	for i in res:
	    #print res
	    if len(i)<=p :
		print(' '*((p-len(i))/2)+i)    


center('she.txt')
