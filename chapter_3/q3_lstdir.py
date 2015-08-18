"""list all the files in the given directory along with their length and last modification time """


from __future__ import print_function
import os
import time
def list_dir(files):
    res=[]
    for i in os.listdir(files):
	print (i,len(i),time.ctime(os.path.getmtime(files)),sep='\t\t')

list_dir('/home/sonu/python/anandh/chapter_2')
