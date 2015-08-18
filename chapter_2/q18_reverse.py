'''	function print each line of a file in reverse order	'''



def rev(filename):
    res=[]
    f=open(filename)
    for i in f:
	   # line=i[::-1]
	i=i.split()
	y=i[::-1]
	reverse=" ".join(y)
	print reverse


rev('she.txt')
