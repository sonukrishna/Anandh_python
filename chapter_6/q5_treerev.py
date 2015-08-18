"""reverse elements of a nested-list recursively
>>> tree_reverse([[1, 2], [3, [4, 5]], 6])
[6, [[5, 4], 3], [2, 1]] """


def revers(lst):
   # lst= lst[::-1]
    lst.reverse()
    for i in lst:
	if isinstance(i,list):
	    revers(i)
    return lst

print revers([[1, 2], [3, [4, 5]], 6])

