""" a simple iteration using class """


class Yrange:
    def __init__(self,n):
	self.n=n
	self.i=0
    def __iter__(self):
	return self
    def next(self):
	if self.i<self.n:
	    i=self.i
	    self.i += 1
	    return i
	else:
	    raise StopIteration()

x=Yrange(3)
print x.next()
print x.next()
print x.next()
#print x.next()
print list(Yrange(10))
