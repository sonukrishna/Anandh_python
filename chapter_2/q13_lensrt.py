'''		sort a list in order of length		'''


def lensort(lst):
    res=[]
    for i in sorted(lst,key=len):
	res.append(i)
    return res
aa=['python','is','simple','and','easy','to','learn']
print lensort(aa)


