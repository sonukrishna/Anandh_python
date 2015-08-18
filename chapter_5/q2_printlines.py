""" The program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters. """


import grep
"""previously i created a grep module with little functions"""
def printlines(filenames):
    read=grep.readfiles(filenames)
    for i in read:
	if len(i)>40:
	    print i

printlines(['txt1.txt','txt2.txt','txt2.txt'])
