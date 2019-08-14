class Solution:
    def numRollsToTarget(self, d, f, t):
        dp = [[1 if i < f else 0 for i in range(t)]] + [[ 0 for _ in range(t)] for _ in range(d-1)]
        for i in range(1,d):
            for j in range(1,t):
                dp[i][j] = sum(dp[i-1][j-k] for k in range(1,min(j,f)+1))
        return dp[d-1][t-1]
