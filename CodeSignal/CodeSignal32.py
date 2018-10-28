import collections
def isBeautifulString(inputString):
    letter_container = collections.Counter()
    for i in list(inputString):
        letter_container[i] += 1
    u = inputString.count('a')
    p = inputString[0]
    for v, c in sorted(letter_container.most_common(len(inputString))):
        if c > u or ord(p)-ord(v) > 1:
            return False
        u = c
        p = v
    return True

"""
A string is said to be beautiful if b occurs in it no 
more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

    For inputString = "bbbaacdafe", the output should be
    isBeautifulString(inputString) = true;
    For inputString = "aabbb", the output should be
    isBeautifulString(inputString) = false;
    For inputString = "bbc", the output should be
    isBeautifulString(inputString) = false.

"""

inputString = "aabbb"
if __name__ == '__main__':
    print(isBeautifulString(inputString))
