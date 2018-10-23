def almostIncreasingSequence(s): # sequence = s[], O(n)
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            if i == 0:
                if s[i] >= s[i+1]: del s[i] 
                else: del s[i+1]
                break
            if s[i-1] == s[i+1]:
                if s[i] == s[i-1]: del s[i]
                else: del s[i+1]
                break
            else:
                if s[i] >= s[i+1] and i+2 != len(s): del s[i]
                else: del s[i+1]
                break
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            return False
    return True
"""
Given a sequence of integers as an array, determine whether it 
is possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.

Example

    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed 
    in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing 
    sequence [1, 2]. Alternately, you can remove 2 to get the strictly 
    increasing sequence [1, 3].

"""

s = [1, 3, 2, 1]
if __name__ == '__main__':
    almostIncreasingSequence(s)
