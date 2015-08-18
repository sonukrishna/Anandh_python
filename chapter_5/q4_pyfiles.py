"""function to compute the number of python files (.py extension) in a specified directory recursively. """


import os
def findfiles(dir):
    res=[]
    for word in os.listdir(dir):
        path=os.path.join(dir,word)
        if os.path.isfile(path):
          #  print path
            res.append(word)
        else:
            findfiles(path)
#    print res
    py_files=[file for file in res if '.py' in file]
    print "no of .py file in %s is %d:"%(dir,len(py_files))

findfiles('/home/sonu/python/anandh')

