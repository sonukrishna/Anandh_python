'''	this function creates a 2_d array	'''


def array(a,b):
    return [['None']*b for i in range(a)]

print array(2,4)
aa=array(2,4)
aa[1][2]=7
aa[0][2]=4
aa[0][3]=5
print aa

