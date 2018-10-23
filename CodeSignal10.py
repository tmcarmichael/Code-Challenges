def sortByHeight(a):
    b = sorted([x for x in a if x != -1])
    b_counter = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b[b_counter]
            b_counter += 1
    return a

"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""

a = [-1, 150, 190, 170, -1, -1, 160, 180]
if __name__ == '__main__':
    sortByHeight(a)
