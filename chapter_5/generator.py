"""an example for the use of generators """

def intiger():
    i=1
    while True:
	yield i
	i=i+1
def squares():
    for i in intiger():
	yield i*i
def take(n,seq):
    seq=iter(seq)
    res=[]
    try:
	for i in range(n):
	    res.append(seq.next())
    except StopIteration:
	pass
    return res

print take(10,intiger())
print take(6,squares())
