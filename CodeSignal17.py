def arrayMaximalAdjacentDifference(arr):
    curr_max = 0
    for i in range(len(arr)-1):
        max_diff = abs(arr[i]-arr[i+1])
        if max_diff > curr_max:
            curr_max = max_diff
    return int(curr_max)


"""
Given an array of integers, find the maximal absolute 
difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

arr = [-1, 4, 10, 3, -2]
if __name__ == '__main__':
    arrayMaximalAdjacentDifference(arr)
