def addBorder(picture):
    i, j = (len(picture[0])+2, len(picture[:])+2)
    return ['*'*i]+['*'+i+'*' for i in picture]+['*'*i]

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

"""

picture = ["abc",
           "ded"]
if __name__ == '__main__':
    addBorder(picture)
