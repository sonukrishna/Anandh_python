'''	    the function to cvompare two strings	   '''


def istrcmp(strng1,strng2):
    word1=strng1.upper()
    word2=strng2.upper()
    if word1==word2 :
	return True
    else:
	return False

print istrcmp('pthon','PythOn')
print istrcmp('latex','LatEx')
