from collections import Counter
def commonCharacterCount(s1, s2):
    total = Counter(s1) & Counter(s2)
    return sum(total.values())

"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

"""

s1 = "aabcc"
s2 = "adcaa"
if __name__ == '__main__':
    commonCharacterCount(s1, s2)
