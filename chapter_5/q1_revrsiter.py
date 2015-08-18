"""This programm takes a list and iterates it from the reverse direction """


class Reverse:
    def __init__(self,n):
        self.n=n
        self.i=self.n
    def __iter__(self):
        return self
    def next(self):
        if self.i>0:
            i=self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()

x=Reverse(3)
print x.next()
print x.next()
print x.next()
#print x.next()
print list(Reverse(10))

