def buildPalindrome(st):
    if st[::-1] == st:
        return st
    for i in range(len(st)):
        if(st + st[::-1][len(st) - i::]) == (st + st[::-1][len(st) - i::])[::-1]:
            return st + st[::-1][len(st) - i::]
    return st + st[::-1][1::]
            

"""
Given a string, find the shortest possible string 
which can be achieved by adding characters to the 
end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""

# st = "ababab"
# st = "abaa"
st = "abcabc"
if __name__ == '__main__':
    print(buildPalindrome(st))
