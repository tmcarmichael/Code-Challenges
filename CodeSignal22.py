def evenDigitsOnly(n):
    for i in range(len(str(n))):
        if n//10**i % 2 != 0:
            return False
    return True


"""
Check if all digits of the given integer are even.

Example

    For n = 248622, the output should be
    evenDigitsOnly(n) = true;
    For n = 642386, the output should be
    evenDigitsOnly(n) = false.
"""

n = 642386
if __name__ == '__main__':
    print(evenDigitsOnly(n))
