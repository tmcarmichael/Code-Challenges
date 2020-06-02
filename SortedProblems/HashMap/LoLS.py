class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        used = {}
        smax = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                smax = max(smax, i - start + 1)
            used[c] = i
        return smax
