"""
1446. Consecutive Characters

Q: https://leetcode.com/problems/consecutive-characters/
"""


def maxPower(s):
    current = ''
    maxV = 1
    for ch in s:
        if ch != current:
            current = ch
            currentPower = 1
        else:
            currentPower += 1
            maxV = max(maxV, currentPower)
    return maxV
