def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [x if x != elemToReplace else substitutionElem for x in inputArray]


"""
Given an array of integers, replace all the occurrences of 
elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and 
substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""

inputArray = [1, 2, 1, 2, 1]
elemToReplace = 2
substitutionElem = 3
if __name__ == '__main__':
    arrayReplace(inputArray, elemToReplace, substitutionElem)
