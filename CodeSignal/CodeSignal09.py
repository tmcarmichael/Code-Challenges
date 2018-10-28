def isLucky(n):
    lst = [int(i) for i in str(n)]
    lst1 = lst[:len(lst)//2]
    lst2 = lst[len(lst)//2:]
    return True if sum(lst1) == sum(lst2) else False

"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.


"""

n = 239017
if __name__ == '__main__':
    isLucky(n)
