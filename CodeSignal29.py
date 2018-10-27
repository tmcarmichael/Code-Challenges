def firstDigit(inputString):
    return ''.join([i for i in inputString if i.isdigit()])[:1]


"""
Find the leftmost digit that occurs in a given string.

Example

    For inputString = "var_1__Int", the output should be
    firstDigit(inputString) = '1';
    For inputString = "q2q-q", the output should be
    firstDigit(inputString) = '2';
    For inputString = "0ss", the output should be
    firstDigit(inputString) = '0'.

"""

inputString = "q2q-q"
if __name__ == '__main__':
    print(firstDigit(inputString))
