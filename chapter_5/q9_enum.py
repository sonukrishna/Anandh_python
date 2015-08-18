""" the function enumerate """

import itertools
def enume(list):
    for x,y in itertools.izip(range(len(list)),list):
	print x,y

lst1=list('abrakadabra')
enume(lst1)
