""" This program returns first n pythagorean triplet using generator expressions """



def intiger():
    i=0
    while True:
	yield i
	i=i+1
def display(n,fun):
    fun=iter(fun)
    res=[]
    for i in range(n):
	res.append(fun.next())
    return res
def pyth():
    return ((x,y,z) for z in intiger() for y in range(1,z)for x in range(y,z) if x**2+y**2==z**2)

#python=pyth()
print display(10,pyth())
