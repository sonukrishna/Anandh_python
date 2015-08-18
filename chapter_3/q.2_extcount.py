"""count number of files for each extension in
the given directory"""

import os
def extcount(dir):
    d={}
    for i in os.listdir(dir):
	a=i.split('.')
	b=a[1:]
        for j in b:
	    d[j]=d.get(j,0)+1
    return d

print extcount('/home/sonu/python/anandh/chapter_1')

