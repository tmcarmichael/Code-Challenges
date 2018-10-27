def digitDegree(n):
    stringify = str(n)
    count = 0
    while len(stringify) > 1:
        stringify = str(sum(list(map(int, stringify))))
        n = sum(list(map(int, stringify)))
        count += 1
    return count


"""
Let's define digit degree of some positive integer 
as the number of times we need to replace this number 
with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

    For n = 5, the output should be
    digitDegree(n) = 0;
    For n = 100, the output should be
    digitDegree(n) = 1.
    1 + 0 + 0 = 1.
    For n = 91, the output should be
    digitDegree(n) = 2.
    9 + 1 = 10 -> 1 + 0 = 1.
"""

n = 91
if __name__ == '__main__':
    print(digitDegree(n))
