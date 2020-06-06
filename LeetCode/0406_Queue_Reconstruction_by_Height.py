"""
406. Queue Reconstruction by Height

https://leetcode.com/problems/queue-reconstruction-by-height/
"""
from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda a: (-a[0], a[1]))
        res: List = []
        for p in people:
            res.insert(p[1], p)
        return res
