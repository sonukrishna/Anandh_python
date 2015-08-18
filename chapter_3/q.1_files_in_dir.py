"""	This program list all files in the given directory	"""


import os
def files(dir):
    res=[]
    for i in os.listdir(dir):
	res.append(i)
    return res

print files('/home/sonu/python/anandh/chapter_2') 
