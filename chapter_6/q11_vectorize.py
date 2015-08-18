""" function 'vectorize' which takes a function, which takes a list as argument and calls
result as a list. e>>>  def   square (x):  return  x  *  x
...
>>> f  =  vectorize(square)
>>> f([1, 2, 3])
[1, 4, 9]
>>> g  =  vectorize(len)
>>> g(["hello", "world"])
[5, 5]
>>> g([[1, 2], [2, 3, 4]])
[2, 3] """


def sqr(x):
    return x*x
def cube(x):
    return x*x*x

def vectorize(f):
    def g(x):
	res=[]
	for i in x:
	    value=f(i)
	    res.append(value)
	return res
    return g


sqr=vectorize(sqr)
cube=vectorize(cube)
print cube([1,2,3,4,5])
print sqr([1,2,3,4,5])
