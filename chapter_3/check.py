"""	this program checking the working of module num		"""

import num
def foo(x):
    print "the square of %d:"% x
    a=num.sqr(x)
    print a
    b=num.cube(x)
    c=num.qud(x)
    d=num.pent(x)
    print "the cube of %d is %d"%(x,b)
    print "the quad of %d is %d"%(x,c)
    print "the pent of %d is %d"%(x,d)

foo(5)
