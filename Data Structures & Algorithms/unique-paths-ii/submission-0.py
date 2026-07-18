class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        #array of size N+1 fill em with 0's
        dp = [0] * (N + 1)
        #make outermost column have 1 initial value so it can look right
        dp[N - 1] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                #if cell is non zero (so 1 an obstacle) set = 0 to remove path option
                if obstacleGrid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c + 1]
        return dp[0]