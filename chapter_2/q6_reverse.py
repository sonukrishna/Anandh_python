'''		reverse a list without using string slicing		'''


def rev(n):
    res=[]
    l=len(n)-1
    for i in n:
	res.append(n[l])
        l=l-1
    print "the string %s reversed to:"% n,
    return res


n=raw_input("enter the length of the list:")
l=[]
for i in range(int(n)):
    l.append(int(raw_input("enter the elements%d:"% i)))
print rev(l)
