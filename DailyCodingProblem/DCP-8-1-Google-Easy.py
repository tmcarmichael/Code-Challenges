'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def adds_to_k(nums:list, k:int) -> bool:
    if len(nums) < 1: return False
    if len(nums) == 2:
        if nums[0] == k: return True
        else: return False
    difset = {k-i for i in nums}
    for i in nums:
        if i in difset:
            return True
    return False

nums = [10,15,3,7]
k = 17 # target number
print(adds_to_k(nums, k))
