'''	this parse can eliminate any delimiter and comments	'''

import string
def parse(file):
    res=[]
    for i in open(file):
	i=i.strip()
	for c in string.punctuation :
	    i=i.replace(c,',')
	i=i.split(',')
	res.append(i)
    return res

print parse('pars.txt')
