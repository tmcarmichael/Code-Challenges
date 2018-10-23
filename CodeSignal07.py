def allLongestStrings(i):
    return [x for x in i if len(x) == len(max(i, key=len))]


"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

"""

i = ["aba", "aa", "ad", "vcd", "aba"]
if __name__ == '__main__':
    allLongestStrings(i)
