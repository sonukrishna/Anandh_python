""" The function 'profile' , which takes a function as argument and returns a
new function, which behaves exactly similar to the given function, except that it prints
the time consumed in executing it. """

import time
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#start=time.time()
def profile(f):
    def g(x):
	start=time.time()
        #print f.__name__,x
        value=f(x)
        end=time.time()-start
       # print 'return',repr(value)
        print 'time taken %s'% str(end)+'sec' 
        return value
    return g
    

fib=profile(fib)

print fib(20)

#print fib(27)
