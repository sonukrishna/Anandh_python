""" function 'treemap'
to map a function over nested list.
>>> treemap( lambda  x: x * x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]] """

def treemap(f,lst):
    res=[]
    for i in range(len(lst)):
	if isinstance(lst[i],list):
	    treemap(f,lst[i])
	else:
	    fun=f(lst[i])
	   # res.append(fun)
	    lst.remove(lst[i])
	    lst.insert(i,fun)
    return lst 
print treemap( lambda  x: x * x, [1, 2, [3, 4, [5]]])

