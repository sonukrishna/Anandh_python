""" a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree. """


import os
def findfiles(dir):
    res=[]
    for word in os.listdir(dir):
        path=os.path.join(dir,word)
        if os.path.isfile(path):
          #  print path
            res.append(path)
        else:
            findfiles(path)
    for i in res:
	print i

findfiles('/home/sonu/python')#/anandh/chapter_5')
