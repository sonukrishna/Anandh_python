"""operations on rational numbers """


class RationalNum:
    def __init__(self,numerator,denominator=1):
	self.num=numerator
	self.denom=denominator
    def __add__(self,other):
	if not isinstance(other,RationalNum):
	    other=RationalNum(other)
	numrtr=self.num*other.denom+self.denom*other.num
        dnmntr=self.denom*other.denom
	return RationalNum(numrtr,dnmntr)
    def __sub__(self,other):
	if not isinstance(other,RationalNum):
	    other=RationalNum(other)
        numrtr=self.num*other.denom+self.denom*other.num
	dnmntr=self.denom*other.denom
	return RationalNum(numrtr,dnmntr)
    def __mul__(self,other):
	if not isinstance(other,RationalNum):
	    other=RationalNum(other)
	numrtr=self.num*other.num
	dnmntr=self.denom*other.denom
	return RationalNum(numrtr,dnmntr)
    def __div__(self,other):
	if not isinstance(other,RationalNum):
	    other=RationalNum(other)
	numrtr=self.num*other.denom
	dnmntr=self.denom*other.num
	return RationalNum(numrtr,dnmntr)

    def __str__(self):
	return "%s/%s"%(self.num,self.denom)

a=RationalNum(1,3)
b=RationalNum(2,3)
print a+b
print a*b
#a=Rectangle(2,3)
#b=Rectangle(5,6)
#a.__add__(b)    
	
