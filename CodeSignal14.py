from operator import is_not
from functools import partial
def areSimilar(a, b):
    lst = [i if a[i] != b[i] else '@' for i in range(len(a))]
    lst = list(filter(partial(is_not, '@'), lst))
    return len(lst) == 0 or len(lst) == 2 and a[lst[0]] == b[lst[1]] and b[lst[0]] == a[lst[1]]

"""
Two arrays are called similar if one can be obtained from another 
by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    areSimilar(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    areSimilar(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    areSimilar(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal.

"""

a = [1, 2, 2]
b = [2, 1, 1]
if __name__ == '__main__':
    areSimilar(a, b)
