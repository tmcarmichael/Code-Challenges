def adjacentElementsProduct(inputArray):
    currmax = -1000000 # initialize with lowest possible product
    for i in range(len(inputArray) - 1):
        if inputArray[i]*inputArray[i+1] > currmax:
            currmax = inputArray[i]*inputArray[i+1]
    return currmax

"""
Given an array of integers, find the pair of adjacent 
elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""

inputArray = [3, 6, -2, -5, 7, 3]
if __name__ == '__main__':
    adjacentElementsProduct(inputArray)
