'''	filter the elements as per the function		'''


def my_filter(f,a):
    return [x for x in a if f(x)]
def even(x):
    return x%2==0

aa=range(15)
print my_filter(even,aa)
