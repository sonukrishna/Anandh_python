'''	map function using list comprehension	   '''



def sqr(x):
    return x*x
def cube(x):
    return x*x*x
def maps(f,a):
    return [f(a[x])for x in range(len(a))]

aa=range(0,33,4)
print maps(sqr,aa)
