"""program 'dirtree.py'
that takes a directory as argument and
prints all the files in that directory recursively as a tree. """

import os
def dirtree(dir):
    num=0
    filenames= os.listdir(dir)
    for i in filenames:
	if os.path.isdir(i):
	    print i+'/'
	    
	 #   num=num+1
	  #  dirtree(i)
#	else:

#	    print '|'*num+'---'+i

dirtree('/home/sonu/python/anandh')
