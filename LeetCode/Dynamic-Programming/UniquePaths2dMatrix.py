class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Setup DP table
        dp = [[1 for _ in range(m)]] + [[1 if i < 1 else 0 for i in range(m)] for _ in range(n-1)]
        # Solve Subproblems
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
