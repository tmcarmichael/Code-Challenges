class Solution:
    def convert(self, s: str, n: int) -> str:
        if n <= 1: return s
        res = ['' for i in range(0, n)]
        for i, c in enumerate(s):
            row = i % (2 * n - 2)
            if row > n - 1:
                row = 2 * n - row - 2
            res[row] += c
        return ''.join(res)
