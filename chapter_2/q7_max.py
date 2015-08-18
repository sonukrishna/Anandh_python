'''	find max and min in a list		'''


def maxmin(lst):
    max = min = lst[0]
    for i in lst[:]:
	if i< min :
	    min=i
	else:
	    max=i
    
    print "the max,min no. is:",
    return max,min


aa=[5,6,3,2,7,5,9,8,55,56]
print maxmin(aa) 
