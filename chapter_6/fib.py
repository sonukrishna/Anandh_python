""" simple example of using decorators and higher order functions """

def trace(f):
    def g(x):
        print f.__name__,x
        value=f(x)
        print 'return',repr(value)
        return value
    return g

@trace
def fib(n):
    if n is 0 or n is 1:
	return 1
    else:
	return fib(n-1)+fib(n-2)

def memoize(f):
    cache={}
    def g(x):
	if x not in cache:
	    cache[x]=f(x)
	return cache[x]
    return g
#fib=trace(fib)
fib=memoize(fib)
print fib(4)

fib=trace(fib)
print fib(4)
