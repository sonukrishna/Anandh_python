""" multiply 2 numbers recursively using + and - operators only. """

def product(x,y):
    if y==0 or x==0:
	return 0
   # if abs(y)==1:
#	return 1
    if x<0 and y<0:
	return abs(x)+product(abs(x),abs(y)-1) 
    elif x<0 and y>0:
	return x+product(x,abs(y)-1)
    elif x>0 and y<0:
	return -x+product((-x),abs(y)-1)
    else:
	return x+product(x,y-1) 

print product(-11,-5)
