'''	this function seperates comma seperated value files	'''


def parse(file):
    res=[]
    with open (file)as a:
	for i in a:
	    i=i.strip()
	    i=i.split(',')
	    res.append(i)
	return res


print parse('parse.txt')
