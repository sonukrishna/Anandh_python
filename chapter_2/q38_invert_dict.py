"""function
invertdict
to interchange keys and values in a dictionary  """


def invert(d):
    dict={}
    for i,j in d.items():
	dict[j]=i
    return dict

print invert({'x': 1, 'y': 2, 'z': 3})

