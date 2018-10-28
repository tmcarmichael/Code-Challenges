def arrayMaxConsecutiveSum(inputArray, k):
    return max([ sum(inputArray[i:k+i]) for i in range(len(inputArray)-k+1)])


""" more efficient """
# local_sum = sum(inputArray[0:k])
# max_sum = local_sum
# for i in range(1, len(inputArray)-k+1):
#     local_sum = local_sum - inputArray[i-1] + inputArray[i+k-1]
#     if local_sum > max_sum:
#         max_sum = local_sum
# return max_sum

"""
Given array of integers, find the maximal possible sum of 
some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

    2 + 3 = 5;
    3 + 5 = 8;
    5 + 1 = 6;
    1 + 6 = 7.
    Thus, the answer is 8.

"""

inputArray = [1, 3, 4, 2, 4, 2, 4]
k = 4
if __name__ == '__main__':
    print(arrayMaxConsecutiveSum(inputArray, k))
