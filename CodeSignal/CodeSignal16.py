def palindromeRearranging(inputString):
    counts = dict()
    for i in inputString:
        counts[i] = counts.get(i, 0) + 1
    uniqueChar = 0
    for i, j in counts.items():
        if j%2 == 1:
            uniqueChar += 1
    if uniqueChar == 1 or uniqueChar == 0:
        return True
    return False

"""
You are given an array of integers. On each move you are allowed 
to increase exactly one of its element by one. Find the minimal 
number of moves required to obtain a strictly increasing sequence 
from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

"""

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa"
if __name__ == '__main__':
    palindromeRearranging(inputString)
