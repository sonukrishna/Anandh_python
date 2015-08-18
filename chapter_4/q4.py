"""raise-except,inside a function """


def foo():
    try:
	print "a"
#	raise Exception('doom')
	return
    except:
	print "b"
    else:
	print "c"
    finally:
	print "d"

foo()
