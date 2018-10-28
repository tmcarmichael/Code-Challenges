def alphabeticShift(inputString):
    return ''.join(list(map(lambda x: chr(ord(x)+1) if x != 'z' else 'a', inputString)))


"""
Given a string, replace each its character by the next 
one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".

"""

inputString = "aaaabbbccd"
if __name__ == '__main__':
    print(alphabeticShift(inputString))
