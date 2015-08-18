'''		factorial of a number		'''


def fact(n):
    fact=1
    if n==0:
	return 1
    if n==1:
	return 1
    for num in range(1,n+1):
	fact=fact*num
    return fact


print fact(0)
print fact(1)
print fact(9)
