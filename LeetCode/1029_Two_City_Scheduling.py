"""
1029. Two City Scheduling

Q: https://leetcode.com/problems/two-city-scheduling/
"""


class Solution:
    def twoCitySchedCost(self, costs):
        res = 0
        l = int(len(costs)/2)
        costs.sort(key=lambda c: c[1] - c[0])
        for idx, costPair in enumerate(costs):
            if idx >= l:
                res += costPair[0]
            else:
                res += costPair[1]
        return res
