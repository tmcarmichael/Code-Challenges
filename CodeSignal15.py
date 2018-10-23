def arrayChange(inputArray):
    ret, prev = 0, None
    for index, element in enumerate(inputArray):
        if index == 0:
            prev = element
            continue
        if prev + 1 - element > 0:
            ret += prev + 1 - element
            prev = prev + 1
        else:
            prev = element
    return ret

"""
You are given an array of integers. On each move you are allowed 
to increase exactly one of its element by one. Find the minimal 
number of moves required to obtain a strictly increasing sequence 
from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

"""

inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
if __name__ == '__main__':
    arrayChange(inputArray)
