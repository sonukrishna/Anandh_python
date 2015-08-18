""" validate the phone number """



import re
def phone():
    print "the phone number:",
    num=raw_input()
    val=re.match(r'\d\d\d\d\d\d\d\d\d\d',num)
    if val:
	print "the no: is validate",val.group()
    else:
        print "not validate"

phone()
