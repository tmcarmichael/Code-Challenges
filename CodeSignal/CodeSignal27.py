def constructArray(size):
    arr = []
    for i in range(size+1//2):
        if i%2==0:
            arr.append((i//2)+1)
        if i%2!=0:
            arr.append((size-i//2))
    return arr


"""
Given an integer size, return an array containing 
each integer from 1 to size in the following order:

1, size, 2, size - 1, 3, size - 2, 4, ...

Example

For size = 7, the output should be
constructArray(size) = [1, 7, 2, 6, 3, 5, 4].

"""

size = 7
if __name__ == '__main__':
    print(constructArray(size))
