'''		wrap each sentences in the file as per the given length		'''


def wrap(filename,n):
    for i in open(filename):
	if len(i)>n :
	    if i[n-1]!=' ' :
		for j in range(n-1):
		    if i[:n-1][-j]==' ':
			print i[0:n-1+(-j)]
			print i[n-1+(-j):len(i)]
			break	
	    
	    else:
		print i[0:n-1]
		print i[n-1:len(i)]


wrap('she.txt',25)
