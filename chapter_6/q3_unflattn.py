""" >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4} """


def unflatten(dct):
    d={}
    d1={}
    d2={}
    res=[]
    res1=[]
    for key,value in dct.items():
	if '.' in key:
	    res.append(dct[key])
	    key=key.split('.')
	    res1.append(key)
	    frst=res1[0][0]
	   # print value
	    num=0
	    for i,j in res1:
		d1[j]=res[num]
		num=num+1
		d2[frst]=d1
    	#	unflatten(d1)
	else:
	    d[key]=value
    for i,j in d2.items():
	d[i]=j
    print d
			

	        
   
unflatten({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})

