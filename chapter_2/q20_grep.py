'''		the unix command grep(print all the lines in a file in which the given string is occured)	   '''


def grep(filename,word):
    res=[]
    for i in open(filename):
	if word in i:
	    print i



grep('she.txt','sure')
