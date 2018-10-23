def checkPalindrome(inputString):
    rindex = len(inputString) - 1
    lindex = 0
    
    while rindex > lindex:
        if inputString[rindex] != inputString[lindex]:
            return False
        lindex += 1
        rindex -= 1
    return True

"""
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
        checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
        checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
        checkPalindrome(inputString) = true.
"""

inputString= "hlbeeykoqqqqokyeeblh"
if __name__ == '__main__':
    checkPalindrome(inputString)
