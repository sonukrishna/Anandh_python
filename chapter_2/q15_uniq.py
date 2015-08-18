'''		unique elements using set		'''


def unq(n):
    res=set([])
    for i in n:
        key=i.lower()
        if key not in res:
            res.add(key)
    print res


aa={'6','6','2','sonu','5','SonU','pyThon','jAvA','Python'}
unq(aa)
