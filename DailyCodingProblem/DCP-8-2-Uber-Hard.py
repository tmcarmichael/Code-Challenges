'''
Daily Coding Problem: 8/2 - Hard - Uber Question

Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all of the numbers in the original array except the one at i.

For example, if our input was [1,2,3,4,5], the expected output would be [120,60,40,30,24]. 
If our input was [3,2,1], the expected output would be [2,3,6].
'''

# ! Without using division
def DCPArrProducts(n):
    # TODO: Base cases
    nums = str(n)[1:-1].replace(', ', '*')+'*' # 1*2*3*4*5*
    for i in range(len(n)):
        n[i] = eval(nums.replace(str(n[i])+'*','')[:-1])
    return n # return v: [120, 60, 40, 30, 24]

# Golf version:
# def DCPArrProducts(n):
#     return [eval(str(n)[1:-1].replace(', ', '*')+'*'.replace(str(n[i])+'*','')[:-1]) for i in range(len(n))]

nums = [1,2,3,4,5] # result expected: [120,60,40,30,24]
print(DCPArrProducts(nums))
