'''		sort a string as per extension		'''


def extsrt(lst):
    res=[]
    res1=[]
    for i in lst:
	i=i.split('.')
	res.append(i)
    res.sort(key=lambda i: i[1])
   # print res
    for i in res:
	i=".".join(i)
	res1.append(i)
    return res1
aa=['a.c','b.py','c.java']
print extsrt(aa)
