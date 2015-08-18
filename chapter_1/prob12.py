'''	this function find the no.of digits in a given number	    '''



def count_digits(n):
    count = 0
    while count <len(str(n)):
	count=count+1
    print "the no.of digits in %d:"% n ,
    return count


print count_digits(123456789528)
