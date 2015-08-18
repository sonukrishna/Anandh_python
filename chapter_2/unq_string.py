'''		check the uniqness of words in alist		'''


def unq(lst,key):
    res=[]
    for i in sorted(lst):
	key=i.lower()
	if key not in res:
	    res.append(key)
    print res

aa=["s","p","Sonu","P","sonu","a","b","SOnU"]
unq(aa,key=lambda aa: aa.lower())
