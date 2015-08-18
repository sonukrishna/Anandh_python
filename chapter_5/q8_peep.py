"""akes an iterator as argument and returns the
first element and an equivalant iterator.
>>> it  =  iter(range(5))
>>> x, it1  =  peep(it)
>>>  print  x, list(it1)
0 [0, 1, 2, 3, 4]  """

def peep(it):
    it1=list(it)
    x=it1[0]
    return x,it1
it=iter(range(5))
x,it1= peep(it)
print x, it1
