""" The function izip works like this
>>>  for  x, y  in  itertools . izip(["a", "b", "c"], [1, 2, 3]):
...      print  x, y
...
a 1
b 2
c 3  """

def izip(list1,list2):
    i=0
    while i< len(list1):
	print list1[i],list2[i]
	i=i+1

#a=['a','b','c','d','f']
#b=[1,2,3,4]
c=list('abrakadabra')
d=list(range(len(c)))
#izip(a,b)
izip(c,d)
