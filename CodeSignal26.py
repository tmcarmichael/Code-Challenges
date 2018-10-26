def absoluteValuesSumMinimization(a):
    sums = [sum(abs(e1 - e2) for e1 in a) for e2 in a]
    min_index_sums = sums.index(min(sums))
    return a[min_index_sums]


"""
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

is the smallest possible (here abs denotes the absolute value).
If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be
absoluteValuesSumMinimization(a) = 4.

"""

a = [2, 4, 7]
if __name__ == '__main__':
    print(absoluteValuesSumMinimization(a))
