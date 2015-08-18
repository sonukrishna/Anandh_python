""" function 'permute'
to compute all possible permutations of elements
of a given list.
>>> permute([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] """

import itertools
def permute(lst):
    return [x for x in itertools.permutations(lst)]

list1=[1,2,3,4]
print permute(list1)
