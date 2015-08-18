"""flatten a nested dictionary by joining the keys with '.' character """



def flatten_dict(dct):
    d={}
    for key,value in dct.items():
	if isinstance(value,dict):
	    print key,value
	    for i,j in value.items():
		new_key=key+'.'+i
	        d[new_key]=j
		flatten_dict(d)
	else:
	    d[key]=value
    return d

print flatten_dict({'a':5,'b':{'x':6,'y':10},'c':9})
