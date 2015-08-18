'''		the zip function using list comprehensions	   '''



def zips(a,b):
    return [(a[x],b[y])for x in range(len(a)) for y in range(len(b)) if x==y]


lst1=[1,2,3,4]
lst2=list('sonu')
print zips(lst1,lst2)
