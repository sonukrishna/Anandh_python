""" unction to compute the total number of lines of code, ignoring empty 
and comment lines, in all python files in the specified directory recursively """


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
    for i in res:
        if (i[0]!='#'and i[0]!=' """ ' and i[0]!='\n'):
	   # i=i.strip('\n')
            res1.append(i)

    print "total lines of code in %s is :"%dir,
    print len(res)
    print "total no.of lines after stripping command lines is:",
    return len(res1)

print findfiles('/home/sonu/python/anandh/chapter_5')

