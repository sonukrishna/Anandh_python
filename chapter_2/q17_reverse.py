'''		print lines of a file in reverse order		'''


def rev(filename):
    res=[]
    with open(filename)as f:
	for i in f:
	    res.append(i)
        reverse=res[::-1]
	i="".join(reverse)
	return i

print rev('she.txt')
