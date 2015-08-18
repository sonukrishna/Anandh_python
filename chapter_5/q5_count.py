"""a function to compute the total number of lines of code in all python files in the specified directory recursively. """

import os
import grep
def findfiles(dir):
    res=[]
    res1=[]
    files=os.listdir(dir)
    py_files=grep.greps('.py',files)
    py_files1=grep.readfiles(py_files)
    for i in py_files1:
	res.append(i)
    print "total lines of code in %s is :"%dir,
    return len(res)
    
        
print findfiles('/home/sonu/python/anandh/chapter_5')	
